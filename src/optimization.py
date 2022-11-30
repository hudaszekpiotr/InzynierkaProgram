#!/usr/bin/python
# -*- coding: utf-8 -*-
import copy
from typing import List, Callable

from matplotlib import pyplot as plt

from src.solution_classes import Solution, SolutionAndFitness
from src.model_limits import daily_resources_ok, resources_df, penalty, resources_percent

from copy import deepcopy
import math
import numpy as np
import random
import json

class Optimization:
    def __init__(self, resources, fields, cultivation_types):
        self.num_days = resources["time"]
        self.num_fields = len(fields)
        self.resources = resources
        self.fields = fields
        self.cultivation_types = cultivation_types

    def generate_initial_population(self, population_size=1, method = "filled"):
        def fill_in_solution(solution):
            for i in range(solution.num_fields):

                type = random.randint(0, len(self.cultivation_types)-1)
                day = random.randint(*self.cultivation_types[type]["start_date"])

                self.add_to_solution(solution, day, i, type)
                # for k in range(self.cultivation_types[type]["duration"]):
                #     solution.days[day+k].field[i] = type, k
            return solution

        sol_list = []
        for _ in range(population_size):
            solution = Solution(self.num_fields, self.num_days)
            if method == "filled":
                solution = fill_in_solution(solution)
            sol_list.append(solution)

        return sol_list
            #daily_resources_ok(solution, self.resources, self.cultivation_types)

    def add_to_solution(self, solution, day, field, crop_type):
        for k in range(self.cultivation_types[crop_type]["duration"]):
            solution.days[day + k].field[field] = crop_type, k

    def check_slot(self, solution, start_day, duration, field):
        for day in range(start_day, start_day + duration):
            if len(solution.days) <= day:
                return False
            crop = solution.days[day].field[field]
            if crop:
                return False
        return True

    def clear_slot(self, solution, start_day, duration, field):
        for day in range(start_day, start_day + duration):
            if len(solution.days) <= day:
                return False
            crop = solution.days[day].field[field]

            if crop and day == start_day:
                day_iter_back = day - 1
                prev = crop[1]
                while solution.days[day_iter_back].field[field] is not None and prev > solution.days[day_iter_back].field[field][1]:
                    solution.days[day_iter_back+1].field[field] = None
                    prev = solution.days[day_iter_back].field[field][1]
                    day_iter_back -= 1
                solution.days[day_iter_back+1].field[field] = None

            if crop and day == start_day + duration - 1:
                day_iter_forward = day + 1
                prev = crop[1]
                while solution.days[day_iter_forward].field[field] is not None and prev < solution.days[day_iter_forward].field[field][1]:
                    solution.days[day_iter_forward-1].field[field] = None
                    prev = solution.days[day_iter_forward].field[field][1]
                    day_iter_forward += 1
                solution.days[day_iter_forward-1].field[field] = None

            solution.days[day].field[field] = None
        return True

    def check_if_sol_acceptable(self, solution: Solution) -> bool:
        pass

    def calculate_objective_fun(self, solution: Solution):
        profit = 0

        for day in solution.days:
            for field_count, field in enumerate(day.field):
                if field is not None and field[1] == 0:
                    crop_type = self.cultivation_types[field[0]]
                    field_type = self.fields[field_count]
                    profit += crop_type["profit"] * field_type["coeficients"][crop_type["name"]] * field_type["area"]

        profit -= penalty(solution, self.cultivation_types, self.resources)
        return profit

    def mutate_solution(self, initial_solution):

        def mutation_smart_fit(org_solution):
            solution = deepcopy(org_solution)
            prev_solution = deepcopy(org_solution)
            type = random.randint(0, len(self.cultivation_types) - 1)
            day = random.randint(*self.cultivation_types[type]["start_date"])
            duration = self.cultivation_types[type]["duration"]

            fields_shuffled_list = list(range(self.num_fields))
            random.shuffle(fields_shuffled_list)
            for field in fields_shuffled_list:
                slot_empty = self.check_slot(solution, day, duration, field)
                if slot_empty:
                    self.add_to_solution(solution, day, field, type)
                    return solution

            field = random.randint(0, self.num_fields - 1)
            success = self.clear_slot(solution, day, duration, field)
            if success:
                self.add_to_solution(solution, day, field, type)
            return solution

        def mutation_force_fit(org_solution):
            solution = deepcopy(org_solution)
            prev_solution = deepcopy(org_solution)
            field = random.randint(0, self.num_fields - 1)
            crop_type = random.randint(0, len(self.cultivation_types) - 1)
            day = random.randint(*self.cultivation_types[crop_type]["start_date"])
            duration = self.cultivation_types[crop_type]["duration"]
            self.clear_slot(solution, day, duration, field)
            self.add_to_solution(solution, day, field, crop_type)
            return solution

        return mutation_smart_fit(initial_solution)

    def selection(self, population):
        pass

    def rulete_wheel_select_one(self, population):
        acc_fitness = sum([c.fitness for c in population])
        if acc_fitness == 0:
            return population[np.random.choice(len(population))]
        selection_probs = [c.fitness / acc_fitness for c in population]
        return population[np.random.choice(len(population), p=selection_probs)]

    def select_parents_SUS(self, population):
        pass

    def crossover(self, solution1: Solution, solution2: Solution, method = "days"):
        def crossover_days(sol1, sol2):
            child = copy.deepcopy(sol1)

            for field in range(self.num_fields):
                edge = True
                sol2_valid = False
                for day in range(self.num_days // 2, self.num_days):
                    if sol1.days[day].field[field] is None or sol1.days[day].field[field][1] == 0:
                        edge = False
                    if not edge and (sol2.days[day].field[field] is None or sol2.days[day].field[field][1] == 0):
                        sol2_valid = True
                    if sol2_valid:
                        child.days[day].field[field] = sol2.days[day].field[field]
            return child

        def crossover_fields(sol1, sol2):
            child1 = copy.deepcopy(sol1)
            child2 = copy.deepcopy(sol2)

            for day in range(self.num_days):
                for field in range(self.num_fields):
                    if field % 2 == 0:
                        child1.days[day].field[field] = sol2.days[day].field[field]
                    else:
                        child2.days[day].field[field] = sol1.days[day].field[field]
            return child1, child2

        if method == "days":
            child1 = crossover_days(solution1, solution2)
            child2 = crossover_days(solution2, solution1)
            return child1, child2
        else:
            return crossover_fields(solution1, solution2)

    def evolution_algorithm(self, par = None):
        """
        :param max_iter_no_progress: Maksymalna ilość iteracji bez poprawy funkcji celu
        :param max_iter: Łączna maksymalna ilość iteracji algorytmu
        :param replacement_rate: Procent populacji jaki jest zastępowany przez potomków
                                w każdej iteracji algorytmu (liczba z zakresu 0-1).
        :param mutation_proba: Prawdopodobieństwo wystąpienia mutacji u dziecka
                               (liczba z zakresu 0-1).

        :return: Znalezione rozwiązanie, koszt rozwiązania, ilość wykonanych iteracji
        """

        max_iter_no_progress = 2
        max_iter = 2
        replacement_rate = 0.5
        mutation_proba = 0.2
        if par is not None:
            max_iter = par.max_iter

        solutions = self.generate_initial_population(2, method = "filled")
        population = []

        for sol in solutions:
            #print(sol.to_dataframe())
            population.append(SolutionAndFitness(sol, self.calculate_objective_fun(sol)))

        iter_with_no_progress = 0

        iterations = 0

        best_profit = -np.inf

        best_results = []
        best_solution = None

        while iter_with_no_progress <= max_iter_no_progress and iterations <= max_iter:

            iterations += 1
            num_children = 0
            children = []
            while replacement_rate > num_children/len(population):
                parent1 = self.rulete_wheel_select_one(population)
                parent2 = self.rulete_wheel_select_one(population)
                child1, child2 = self.crossover(parent1.solution, parent2.solution)
                child1 = self.mutate_solution(child1)
                population.append(SolutionAndFitness(child1, self.calculate_objective_fun(child1)))
                population.append(SolutionAndFitness(child2, self.calculate_objective_fun(child2)))
                num_children +=2
                population = sorted(population, key=lambda x: x.fitness)
                population = population[2:]
            population = sorted(population, key=lambda x: x.fitness)
            best_results.append(population[-1].fitness)
            if best_solution is None or best_solution.fitness < population[-1].fitness:
                best_solution = population[-1]
            for sol in population:
                #print(sol.solution.to_dataframe())
                #df, period_dict = resources_df(sol.solution, self.cultivation_types)
                #print(df)
                #print(period_dict)
                pass
                #print("_________________")
            # num_children = num_children*replacement_rate
            # children = self.select_parents_SUS(population, num_children)

        print(best_results)
        #print(best_solution.solution.to_dataframe())
        df = best_solution.solution.to_simple_dataframe()
        #print(df)
        df_resources, period_dict = resources_percent(best_solution.solution, self.cultivation_types, self.resources)
        #print(df_resources)
        #best_solution.solution.to_simple_dataframe().plot()

        return df, df_resources, best_results

