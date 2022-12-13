#!/usr/bin/python
# -*- coding: utf-8 -*-
import cProfile
import copy
from datetime import date
from typing import List, Callable

from matplotlib import pyplot as plt

from src.genetic_operators import crossover, selection, add_to_solution, mutate_solution
from src.solution_classes import Solution, SolutionAndFitness
from src.model_limits import resources_df, penalty, resources_percent, fixup

from copy import deepcopy
import math
import numpy as np
import random
import json

class Optimization:
    def __init__(self, resources, fields, cultivation_types):
        #self.num_days = resources["time"]
        self.num_fields = len(fields)
        self.resources = resources
        self.fields = fields
        self.cultivation_types = cultivation_types

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
                raise ValueError()
            self.cultivation_types = valid_cult_types


        def fill_in_solution(solution):
            for i in range(solution.num_fields):
                type = random.randint(0, len(self.cultivation_types)-1)
                day = random.randint(*self.cultivation_types[type]["start_date"])
                duration = self.cultivation_types[type]["duration"]
                add_to_solution(solution, day, i, type, duration)
            return solution

        remove_impossible_cult_types()
        sol_list = []
        for _ in range(population_size):
            solution = Solution(self.num_fields, num_days)
            if method == "partially filled solutions":
                solution = fill_in_solution(solution)
            sol_list.append(solution)

        return sol_list

    def calculate_objective_fun(self, solution: Solution, do_penalty):
        profit = 0

        for field_index, field in enumerate(solution.matrix):
            for crop in field:
                #todo skipping indexes based on duration
                if crop is not None and crop[1] == 0:
                    crop_type = self.cultivation_types[crop[0]]
                    field_type = self.fields[field_index]
                    profit += crop_type["profit"] * field_type["coefficients"][crop_type["name"]] * field_type["area"]

        # for day in solution.days:
        #     for field_count, field in enumerate(day.fields):
        #         if field is not None and field[1] == 0:
        #             crop_type = self.cultivation_types[field[0]]
        #             field_type = self.fields[field_count]
        #             profit += crop_type["profit"] * field_type["coefficients"][crop_type["name"]] * field_type["area"]

        if do_penalty:
            profit -= penalty(solution, self.cultivation_types, self.resources)
        return profit


    def transform_cult_types_start_date(self, alg_start_date):

        for i in self.cultivation_types:
            cult_type_start_date = date(alg_start_date.year, i["start_date"]["month"], i["start_date"]["day"])
            #cult_type_start_date = date(i["start_date"]["year"], i["start_date"]["month"], i["start_date"]["day"])
            delta = cult_type_start_date - alg_start_date
            plus_minus_days = i["start_date"]["plus_minus_days"]
            i["start_date"] = [delta.days - plus_minus_days, delta.days + plus_minus_days]

    def find_best_solution(self, population):
        best_so_far = population[0]
        for index, sol in enumerate(population):
            if sol.fitness > best_so_far.fitness:
                best_so_far = sol
        return best_so_far


    def evolution_algorithm(self, parameters):
        self.transform_cult_types_start_date(parameters.start_date)

        #population = []
        population = set()
        solutions = self.generate_initial_population(parameters.num_days, parameters.population_size, parameters.initial_population_type)

        do_fixup = parameters.unacceptable_fix_type == "fixup"
        do_penalty = parameters.unacceptable_fix_type == "penalty"

        for sol in solutions:
            if do_fixup:
                fixup(sol, self.cultivation_types, self.resources)
            #population.append(SolutionAndFitness(sol, self.calculate_objective_fun(sol, do_penalty)))
            population.add(SolutionAndFitness(sol, self.calculate_objective_fun(sol, do_penalty)))

        is_sorted = False
        if parameters.elite_size > 0:
            is_sorted = True
            population = sorted(population, key=lambda x: x.fitness)

        iter_with_no_progress = 0
        iteration = 0
        best_profit = -np.inf
        best_results = []
        best_solution = None
        elite_pool = []
        mating_pool_size = int(parameters.mating_pool_size * 0.01 * parameters.population_size)
        if mating_pool_size == 0:
            mating_pool_size = 2
        if mating_pool_size == parameters.population_size:
            mating_pool_size = parameters.population_size - 1

        elite_size = int(parameters.elite_size * 0.01 * parameters.population_size)
        if elite_size == 0 and parameters.elite_size > 0:
            elite_size = 1
        if elite_size == parameters.population_size:
            elite_size = parameters.population_size - 1

        probability = parameters.mutation_probability

        with cProfile.Profile() as pr:
            while iter_with_no_progress <= parameters.max_iter_no_progress and iteration <= parameters.max_iter:

                mating_pool = selection(population, mating_pool_size, parameters.selection_type, parameters.tournament_size, is_sorted)


                if is_sorted:
                    population = sorted(population, key=lambda x: x.fitness)
                    elite_pool = population[-elite_size:]

                del population
                population = []
                if elite_size > 0:
                    population.extend(elite_pool)

                i = 0
                while len(population) < parameters.population_size:
                    have_to_copy = (parameters.population_size - len(population) > mating_pool_size)
                    if i >= mating_pool_size - 2:
                        mating_pool.extend(mating_pool)
                    child1, child2 = crossover(mating_pool[i].solution, mating_pool[i+1].solution,
                                                    method=parameters.crossover_type, have_to_copy = have_to_copy)

                    if random.random() < probability:
                        mutate_solution(child1, self.cultivation_types)
                    if random.random() < probability:
                        mutate_solution(child2, self.cultivation_types)
                    if do_fixup:
                        fixup(child1, self.cultivation_types, self.resources)
                        fixup(child2, self.cultivation_types, self.resources)
                    #population.append(SolutionAndFitness(child1, self.calculate_objective_fun(child1, do_penalty)))
                    #population.append(SolutionAndFitness(child2, self.calculate_objective_fun(child2, do_penalty)))
                    population.add(SolutionAndFitness(child1, self.calculate_objective_fun(child1, do_penalty)))
                    population.add(SolutionAndFitness(child2, self.calculate_objective_fun(child2, do_penalty)))
                    i += 2

                if len(population) > parameters.population_size:
                    population.pop()

                best_in_iter = self.find_best_solution(population)
                best_results.append(best_in_iter.fitness)

                iter_with_no_progress += 1
                if best_solution is None or best_solution.fitness < best_in_iter.fitness:
                    best_solution = best_in_iter
                    iter_with_no_progress = 0

                iteration += 1
        pr.print_stats()
        print(best_results)
        df = best_solution.solution.to_simple_dataframe()
        df_resources, period_dict = resources_percent(best_solution.solution, self.cultivation_types, self.resources)

        return df, df_resources, best_results

