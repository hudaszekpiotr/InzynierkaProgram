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
    num_fields = solution.num_fields
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

def crossover(solution1: Solution, solution2: Solution, method, cultivation_types, have_to_copy):
    def crossover_days(sol1, sol2):
        child = copy.deepcopy(sol1)
        num_days = sol1.num_days
        num_fields = sol1.num_fields
        for field_index in range(num_fields):
            edge = None
            field_left = child.data[field_index]
            field_right = sol2.data[field_index]
            for index in range(len(field_left)):
                if field_left[index][1] > num_days//2:
                    field_left = field_left[:index]
                    edge = field_left[1] + cultivation_types[field_left[index][0]]["duration"]
                    break
            if edge is None:
                edge = num_days//2
            for index in range(len(field_right)):
                if field_right[index][1] > edge:
                    child.data[field_index].append(field_right[index])
        return child

    def crossover_fields(sol1, sol2):
        child1 = copy.deepcopy(sol1)
        child2 = copy.deepcopy(sol2)
        num_days = sol1.num_days
        num_fields = sol1.num_fields

        for field in range(num_fields):
            if field % 2 == 0:
                child1.data[field] = sol2.data[field]
            else:
                child2.data[field] = sol1.data[field]
        return child1, child2

    if method == "days":
        child1 = crossover_days(solution1, solution2)
        child2 = crossover_days(solution2, solution1)
        return child1, child2
    else:
        return crossover_fields(solution1, solution2)

def add_to_solution(solution, day, field, crop_type, crop_duration):
    inserted = False
    for index in range(len(solution.data[field])):
        if day < solution.data[field][index][1]:
            solution.data[field].insert(index, (crop_type, day))
            inserted = True
            break
    if not inserted:
        solution.data[field].append((crop_type, day))

# def check_slot(solution, start_day, duration, field):
#     for day in range(start_day, start_day + duration):
#         if solution.num_days <= day:
#             return False
#         crop = solution.matrix[field, day]
#         if crop is not None:
#             return False
#     return True

def clear_slot(solution, start_day, duration, field, cultivation_types):
    index = 0
    end_day = start_day + duration
    while index < solution.data[field]:
        crop = solution.data[field][index]
        if start_day <= crop[1] + cultivation_types[crop[0]]["duration"] <= end_day \
                or start_day <= crop[1] <= end_day\
                or (crop[1] < start_day and crop[1] + cultivation_types[crop[0]]["duration"] > end_day):
            del crop
            solution.data[field].pop(index)
        else:
            index += 1

    return True
