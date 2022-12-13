import random

import numpy as np

from src.solution_classes import Solution

import copy


def mutate_solution(solution, cultivation_types):

    def mutation_force_fit(solution):
        field = random.randint(0, num_fields - 1)
        crop_type = random.randint(0, len(cultivation_types) - 1)
        day = random.randint(*cultivation_types[crop_type]["start_date"])
        duration = cultivation_types[crop_type]["duration"]

        clear_slot(solution, day, duration, field)
        add_to_solution(solution, day, field, crop_type, duration)
        # return solution

    # return mutation_force_fit(solution)
    num_fields = len(solution.days[0].fields)
    mutation_force_fit(solution)


def selection(population, mating_pool_size, selection_type, tournament_size, is_sorted):
    def roulette_wheel_selection(population, mating_pool_size):
        negative = 0
        acc_fitness = 0
        for solution in population:
            if solution.fitness < 0:
                if negative > solution.fitness:
                    negative = solution.fitness

        fitness_list = [c.fitness + abs(negative) for c in population]
        acc_fitness = sum(fitness_list)
        if acc_fitness == 0:
            return population[0:mating_pool_size]
            # return population[np.random.choice(len(population))]
        selection_probs = [c / acc_fitness for c in fitness_list]

        mating_pool = []
        for i in range(mating_pool_size):
            mating_pool.append(population[np.random.choice(len(population), p=selection_probs)])
        return mating_pool

    def rank_selection(population, mating_pool_size, is_sorted):
        if not is_sorted:
            population = sorted(population, key=lambda x: x.fitness)
        return population[-mating_pool_size:]

    def tournament_selection(population, mating_pool_size, tournament_size):
        mating_pool = []
        population_size = len(population)
        for i in range(mating_pool_size):
            # <todo> tournament_size > population size
            tournament = random.sample(range(0, population_size - 1), tournament_size)
            solution = max(tournament, key=lambda k: population[k].fitness)
            mating_pool.append(population[solution])
        return mating_pool

    if selection_type == "roulette wheel":
        return roulette_wheel_selection(population, mating_pool_size)
    elif selection_type == "tournament":
        return tournament_selection(population, mating_pool_size, tournament_size)
    elif selection_type == "ranking":
        return rank_selection(population, mating_pool_size, is_sorted)
    else:
        raise ValueError()

def crossover(solution1: Solution, solution2: Solution, method, have_to_copy):
    def crossover_days(sol1, sol2):
        child = copy.deepcopy(sol1)
        num_days = len(sol1.days)
        num_fields = len(sol1.days[0].fields)
        for field in range(num_fields):
            edge = True
            sol2_valid = False
            for day in range(num_days // 2, num_days):
                if sol1.days[day].fields[field] is None or sol1.days[day].fields[field][1] == 0:
                    edge = False
                if not edge and (sol2.days[day].fields[field] is None or sol2.days[day].fields[field][1] == 0):
                    sol2_valid = True
                if sol2_valid:
                    child.days[day].fields[field] = sol2.days[day].fields[field]
                    child.days[day].fields[field] = sol2.days[day].fields[field]
        return child

    def crossover_fields(sol1, sol2):
        child1 = copy.deepcopy(sol1)
        child2 = copy.deepcopy(sol2)
        num_days = len(sol1.days)
        num_fields = len(sol1.days[0].fields)
        for day in range(num_days):
            for field in range(num_fields):
                if field % 2 == 0:
                    child1.days[day].fields[field] = sol2.days[day].fields[field]
                else:
                    child2.days[day].fields[field] = sol1.days[day].fields[field]
        return child1, child2

    if method == "days":
        child1 = crossover_days(solution1, solution2)
        child2 = crossover_days(solution2, solution1)
        return child1, child2
    else:
        return crossover_fields(solution1, solution2)

def add_to_solution(solution, day, field, crop_type, crop_duration):
    for k in range(crop_duration):
        solution.days[day + k].fields[field] = crop_type, k

def check_slot(solution, start_day, duration, field):
    for day in range(start_day, start_day + duration):
        if len(solution.days) <= day:
            return False
        crop = solution.days[day].fields[field]
        if crop is not None:
            return False
    return True

def clear_slot(solution, start_day, duration, field):
    for day in range(start_day, start_day + duration):
        if len(solution.days) <= day:
            return False
        crop = solution.days[day].fields[field]

        if crop and day == start_day:
            day_iter_back = day - 1
            prev = crop[1]
            while solution.days[day_iter_back].fields[field] is not None and prev > solution.days[day_iter_back].fields[field][1]:
                solution.days[day_iter_back+1].fields[field] = None
                prev = solution.days[day_iter_back].fields[field][1]
                day_iter_back -= 1
            solution.days[day_iter_back+1].fields[field] = None

        if crop and day == start_day + duration - 1:
            day_iter_forward = day + 1
            prev = crop[1]
            while solution.days[day_iter_forward].fields[field] is not None and prev < solution.days[day_iter_forward].fields[field][1]:
                solution.days[day_iter_forward-1].fields[field] = None
                prev = solution.days[day_iter_forward].fields[field][1]
                day_iter_forward += 1
            solution.days[day_iter_forward-1].fields[field] = None

        solution.days[day].fields[field] = None
    return True
