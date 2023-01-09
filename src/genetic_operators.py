import random

from src.solution_classes import Solution

import copy


def mutate_solution(solution, mutation_consider_fit, mutation_type, cultivation_types, fields):
    remove = False
    num_fields = solution.num_fields

    if mutation_type == "removing/adding":
        remove = random.choice([True, False])
    if remove:
        remove_random_cultivation_from_solution(solution)
    else:
        crop_type = random.randint(0, len(cultivation_types) - 1)
        if mutation_consider_fit:
            crop_name = cultivation_types[crop_type]["name"]
            fields_indexes = list(range(num_fields))
            weights = [fields[elem]["coefficients"][crop_name] for elem in fields_indexes]
            field = random.choices(fields_indexes, weights=weights)[0]
        else:
            field = random.randint(0, num_fields - 1)
        day = random.randint(*cultivation_types[crop_type]["start_date"])
        duration = cultivation_types[crop_type]["duration"]

        clear_slot(solution, day, duration, field, cultivation_types)
        add_to_solution(solution, day, field, crop_type)


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
        selection_probs = [c / acc_fitness for c in fitness_list]

        mating_pool = []
        for i in range(mating_pool_size):
            mating_pool.append(population[random.choices(range(len(population)), weights=selection_probs)[0]])
            #mating_pool.append(population[np.random.choice(len(population), p=selection_probs)])

        return mating_pool

    def rank_selection(population, mating_pool_size, is_sorted):
        if not is_sorted:
            population = sorted(population, key=lambda x: x.fitness)
        return population[-mating_pool_size:]

    def tournament_selection(population, mating_pool_size, tournament_size):
        mating_pool = []
        population_size = len(population)
        for i in range(mating_pool_size):
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


def crossover(solution1: Solution, solution2: Solution, method, cultivation_types):
    def crossover_days(sol1, sol2):
        num_days = sol1.num_days
        num_fields = sol1.num_fields
        child = Solution(num_fields, num_days)
        for field_index in range(num_fields):
            edge = None

            sol1_field_crops = sol1.data[field_index]

            for index, crop in enumerate(sol1_field_crops):
                if crop[1] > num_days // 2:
                    if index:
                        child.data[field_index] = copy.deepcopy(sol1_field_crops[:index])
                        edge = child.data[field_index][-1][1] + cultivation_types[child.data[field_index][-1][0]]["duration"]
                    break
                if crop[1] + cultivation_types[crop[0]]["duration"] > num_days // 2:
                    if index:
                        child.data[field_index] = copy.deepcopy(sol1_field_crops[:index + 1])
                        edge = child.data[field_index][-1][1] + cultivation_types[child.data[field_index][-1][0]]["duration"]
                    break
            if edge is None:
                edge = num_days // 2
            for index2, crop2 in enumerate(sol2.data[field_index]):
                if crop2[1] > edge:
                    child.data[field_index].extend(copy.deepcopy(sol2.data[field_index][index2:]))
                    break
        return child

    def crossover_fields(sol1, sol2):
        child1_crossing = copy.deepcopy(sol1)
        child2_crossing = copy.deepcopy(sol2)
        num_fields = sol1.num_fields

        for field in range(num_fields):
            if field % 2 == 0:
                child1_crossing.data[field] = copy.deepcopy(sol2.data[field])
                child2_crossing.data[field] = copy.deepcopy(sol1.data[field])
        return child1_crossing, child2_crossing

    if method == "days":
        child1 = crossover_days(solution1, solution2)
        child2 = crossover_days(solution2, solution1)
        return child1, child2
    else:
        return crossover_fields(solution1, solution2)


def add_to_solution(solution, day, field, crop_type):
    inserted = False
    for index, crop in enumerate(solution.data[field]):
        if day < crop[1]:
            solution.data[field].insert(index, (crop_type, day))
            inserted = True
            break
    if not inserted:
        solution.data[field].append((crop_type, day))


def clear_slot(solution, start_day, duration, field, cultivation_types):
    """
    removes any crop from solution from specified field within interval (start_day, start_day + duration)
    """
    index = 0
    end_day = start_day + duration
    while index < len(solution.data[field]):
        crop = solution.data[field][index]
        if start_day <= crop[1] + cultivation_types[crop[0]]["duration"] <= end_day \
                or start_day <= crop[1] <= end_day \
                or (crop[1] < start_day and crop[1] + cultivation_types[crop[0]]["duration"] > end_day):
            del crop
            solution.data[field].pop(index)
        else:
            index += 1


def remove_random_cultivation_from_solution(solution):
    all_crops = []
    for field_index, field in enumerate(solution.data):
        for index, crop in enumerate(field):
            all_crops.append((field_index, index))
    if all_crops:
        field_index, index = random.choice(all_crops)
        solution.data[field_index].pop(index)
