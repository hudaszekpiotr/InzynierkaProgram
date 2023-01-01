#!/usr/bin/python
# -*- coding: utf-8 -*-

import copy

from src.exceptions import NoValidCultivationTypesException
from src.genetic_operators import crossover, selection, add_to_solution, mutate_solution
from src.solution_classes import Solution, SolutionAndFitness
from src.resources_calculations import penalty, resources_percent, fixup

import random

from src.model_data_operations import load_files, transform_cult_types_start_date, elite_and_mating_sizes


class Optimization:
    def __init__(self, filename='data/model_data.json'):
        resources, fields, cultivation_types = load_files(filename)
        # self.num_days = resources["time"]
        self.num_fields = len(fields)
        self.resources = resources
        self.fields = fields
        self.cultivation_types = cultivation_types
        self.org_cultivation_types = copy.deepcopy(cultivation_types)

    def generate_initial_population(self, num_days, population_size, method):
        def remove_impossible_cult_types():
            valid_cult_types = []
            for i in range(len(self.cultivation_types)):
                begin, end = self.cultivation_types[i]["start_date"]
                duration = self.cultivation_types[i]["duration"]
                if begin > end: raise ValueError()
                if end < 0 or begin > num_days:
                    continue
                if end > num_days:
                    end = num_days - 1
                if begin < 0:
                    begin = 0
                if begin + duration > num_days:
                    continue
                latest_possible_end = num_days - duration
                if latest_possible_end < end:
                    end = latest_possible_end

                self.cultivation_types[i]["start_date"] = [begin, end]
                valid_cult_types.append(self.cultivation_types[i])
            if len(valid_cult_types) == 0:
                raise NoValidCultivationTypesException
            self.cultivation_types = valid_cult_types

        def fill_in_solution(solution):
            fields_shuffled_num = list(range(solution.num_fields))
            random.shuffle(fields_shuffled_num)
            for i in fields_shuffled_num:
                type = random.randint(0, len(self.cultivation_types) - 1)
                day = random.randint(*self.cultivation_types[type]["start_date"])
                add_to_solution(solution, day, i, type)
                if penalty(solution, self.cultivation_types, self.resources, 1, self.fields) > 0:
                    solution.data[i].pop()
            return solution

        remove_impossible_cult_types()
        sol_list = []
        for _ in range(population_size):
            solution = Solution(self.num_fields, num_days)
            if method == "partially filled solutions":
                solution = fill_in_solution(solution)
            sol_list.append(solution)

        return sol_list

    def calculate_objective_fun(self, solution: Solution, do_penalty, multiplier):
        profit = 0

        for field_index, field in enumerate(solution.data):
            for crop in field:
                crop_type = self.cultivation_types[crop[0]]
                field_type = self.fields[field_index]
                profit += crop_type["profit"] * field_type["coefficients"][crop_type["name"]] * field_type["area"]

        if do_penalty:
            pass
            profit -= penalty(solution, self.cultivation_types, self.resources, multiplier, self.fields)
        return profit

    @staticmethod
    def find_best_solution(population):
        best_so_far = population[0]
        for index, sol in enumerate(population):
            if sol.fitness > best_so_far.fitness:
                best_so_far = sol
        return best_so_far

    def run_algorithm(self, parameters, verbose=True, info_about_population=False):
        do_fixup = parameters.unacceptable_fix_type == "fixup"
        do_penalty = parameters.unacceptable_fix_type == "penalty"
        is_sorted = False
        iter_with_no_progress = 0
        iteration = 0
        best_results = []
        all_results = []
        best_solution = None
        elite_pool = []
        mating_pool_size, elite_size = elite_and_mating_sizes(parameters.mating_pool_percent, parameters.elite_percent,
                                                              parameters.population_size)

        probability = parameters.mutation_probability

        self.cultivation_types = copy.deepcopy(self.org_cultivation_types)
        transform_cult_types_start_date(self.cultivation_types, parameters.start_date)

        population = []
        solutions = self.generate_initial_population(parameters.num_days, parameters.population_size,
                                                     parameters.initial_population_type)

        for sol in solutions:
            population.append(SolutionAndFitness(sol, self.calculate_objective_fun(sol, do_penalty, parameters.penalty_multiplier_first)))

        if parameters.elite_percent > 0:
            is_sorted = True
            population = sorted(population, key=lambda x: x.fitness)

        #with cProfile.Profile() as pr:
        while iter_with_no_progress <= parameters.max_iter_no_progress and iteration <= parameters.max_iter:

            mating_pool = selection(population, mating_pool_size, parameters.selection_type, parameters.tournament_size,
                                    is_sorted)

            if elite_size:
                population = sorted(population, key=lambda x: x.fitness)
                elite_pool = copy.deepcopy(population[-elite_size:])

            del population
            population = []
            if elite_size:
                population.extend(elite_pool)

            i = 0
            while len(population) < parameters.population_size:
                parents_selected = False
                if i == mating_pool_size - 1:
                    parent1 = mating_pool[i].solution
                    parent2 = mating_pool[0].solution
                    i = 1
                    parents_selected = True
                if i >= mating_pool_size:
                    i = 0
                if not parents_selected:
                    parent1 = mating_pool[i].solution
                    parent2 = mating_pool[i + 1].solution
                child1, child2 = crossover(parent1, parent2,
                                           method=parameters.crossover_type, cultivation_types=self.cultivation_types)

                if random.random() < probability:
                    mutate_solution(child1, True, parameters.mutation_type, self.cultivation_types, self.fields)
                if random.random() < probability:
                    mutate_solution(child2, True, parameters.mutation_type, self.cultivation_types, self.fields)
                if do_fixup:
                    fixup(child1, self.cultivation_types, self.resources, self.fields)
                    fixup(child2, self.cultivation_types, self.resources, self.fields)
                multiplier = None
                if do_penalty:
                    a = (parameters.penalty_multiplier_last - parameters.penalty_multiplier_first) / parameters.max_iter
                    b = parameters.penalty_multiplier_first
                    multiplier = a * iteration + b

                population.append(SolutionAndFitness(child1, self.calculate_objective_fun(child1, do_penalty, multiplier)))
                population.append(SolutionAndFitness(child2, self.calculate_objective_fun(child2, do_penalty, multiplier)))
                i += 2

            if len(population) > parameters.population_size:
                population.pop()

            best_in_iter = self.find_best_solution(population)
            best_results.append(best_in_iter.fitness)

            if info_about_population:
                all_results.append([elem.fitness for elem in population])

            iter_with_no_progress += 1
            if best_solution is None or best_solution.fitness < best_in_iter.fitness:
                best_solution = best_in_iter
                iter_with_no_progress = 0

            iteration += 1
        #pr.print_stats()
        if verbose:
            print(best_results)
            print(best_solution.fitness)
            print(best_solution.solution.data)
            print(best_solution.solution.to_dataframe(self.cultivation_types))

        df = best_solution.solution.to_dataframe(self.cultivation_types)
        df_resources, period_df = resources_percent(best_solution.solution, self.cultivation_types, self.resources, self.fields)

        if info_about_population:
            return df, df_resources, period_df, best_results, all_results
        return df, df_resources, period_df, best_results
