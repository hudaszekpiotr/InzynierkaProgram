#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List, Callable
from solution_classes import Solution
from src.model_limits import daily_resources_ok
from utils import parse_price, parse_resources

from copy import deepcopy
import math
import numpy as np
import random
import json


def main():
    json_cultivation_types = open('../sample_data/cultivation_types.json')
    cultivation_types = json.load(json_cultivation_types)
    json_cultivation_types.close()

    print(json.dumps(cultivation_types, indent=2))
    print("\nparsed:")
    #parse_price(cultivation_types)
    parse_resources(cultivation_types)
    # print(json.dumps(cultivation_types, indent=2))
    for i in cultivation_types:
        print(i)

    json_fields = open('../sample_data/fields.json')
    fields = json.load(json_fields)
    json_fields.close()
    print(json.dumps(fields, indent=2))

    json_resources = open('../sample_data/resources.json')
    resources = json.load(json_resources)
    json_resources.close()
    print(json.dumps(resources, indent=2))

    optimization = Optimization(resources, fields, cultivation_types)
    optimization.genetic_algorithm()





class Optimization:
    def __init__(self, resources, fields, cultivation_types):
        self.num_days = resources["time"]
        self.num_fields = len(fields)
        self.resources = resources
        self.fields = fields
        self.cultivation_types = cultivation_types

    def generate_initial_population(self, population_size=1):
        def fill_in_solution(solution):
            for i in range(solution.num_fields):

                type = random.randint(0, len(self.cultivation_types)-1)
                day = random.randint(*self.cultivation_types[type]["start_date"])

                for k in range(self.cultivation_types[type]["duration"]):
                    solution.days[day+k].field[i] = type, k
            return solution


        sol_list = []
        for _ in range(population_size):
            solution = Solution(self.num_fields, self.num_days)
            solution = fill_in_solution(solution)
            #print(solution)
            sol_list.append(solution)
            daily_resources_ok(solution, self.resources, self.cultivation_types)




    def check_if_sol_acceptable(self, solution: Solution) -> bool:
        """
        Sprawdza wszystkie ograniczenia dla danego rozwiązania w najprostszej wersji
        zwraca bool, w bardziej skomplikowanej informacje gdzie błąd i ewentualnie kara

        :param solution:
        :return:
        """
        pass

    def calculate_objective_fun(self, solution: Solution):
        """
        Funckja oblicza wartośc funkcji celu dla rozwiązania
        :param solution: obiekt reprezentujący rozwiązanie
        :return: profit - wartośc funkcji celu
        """
        profit = 0

        for day_id, day in enumerate(solution.days):
            for _ in range():
                pass

        return profit

    # losuje dopuszcalnego sąsiada
    def draw_solution(self, initial_solution):

        def neighbourhood_1(org_solution):
            solution = deepcopy(org_solution)
            prev_solution = deepcopy(org_solution)
            day = random.randint(0, self.num_days - 1)

            return solution

        # próbuje znalezc sasiada jesli w ciagu 100 losowan nie znajdzie akceptowalnego rzuca wyjątek
        for _ in range(100):
            sol = neighbourhood_1(initial_solution)
            if self.check_if_sol_acceptable(sol):
                return sol

        raise Exception("error nie znaleziono otoczenia")

    # metoda wybierająca rodziców
    def selection(self, population):
        parents = []
        while len(parents) < 2:
            # losuje dwóch kandydatów do listy rodziców
            candidate1 = random.randint(0, len(population) - 1)
            candidate2 = random.randint(0, len(population) - 1)
            while candidate1 == candidate2:
                # w przypadku, gdy wylosowano dwóch takich samych 
                # kandydatów, losowanie jest powtarzane 
                candidate2 = random.randint(0, len(population) - 1)
            if population[candidate1][1] > population[candidate2][1]:
                parents.append(population[candidate1])
                # do listy rodziców dodawany jest kandydat
                # dający większą wartość funkcji celu
            else:
                parents.append(population[candidate2])
        return parents

    # metoda krzyżująca dwa rozwiązania sol1 i sol2
    def crossover(self, sol1: Solution, sol2: Solution, bruteforce_comapre=False):
        if (not self.check_if_sol_acceptable(sol1)) or (not self.check_if_sol_acceptable(sol2)):
            raise Exception("error podano niedopuszczalne rozw. do skrzyżowania")

        for _ in range(100):
            pass
            child = None
            if self.check_if_sol_acceptable(child):
                return child
        return None

    def genetic_algorithm(self, max_iter_no_progress=10, max_iter=0, replacement_rate=0.5, mutation_proba=0.2):
        """
        :param max_iter_no_progress: Maksymalna ilość iteracji bez poprawy funkcji celu
        :param max_iter: Łączna maksymalna ilość iteracji algorytmu
        :param replacement_rate: Procent populacji jaki jest zastępowany przez potomków
                                w każdej iteracji algorytmu (liczba z zakresu 0-1).
        :param mutation_proba: Prawdopodobieństwo wystąpienia mutacji u dziecka
                               (liczba z zakresu 0-1).

        :return: Znalezione rozwiązanie, koszt rozwiązania, ilość wykonanych iteracji
        """
        solutions = self.generate_initial_population()

        # population to lista list, w której przechowujemy rozwiązania.
        # Poszczególne elementy listy population to dwuelementowe
        # listy o następującej postaci [rozwiązanie, funkcja celu dla rozwiązania]

        #population = [[sol[0], self.calculate_objective_fun(sol[0])] for sol in solutions]

        # sortowanie populacji po wartości funkcji celu
        # population = sorted(population, key=lambda x: x[1])
        #
        # # licznik iteracji bez poprawy funkcji celu
        # iter_with_no_progress = 0
        # # licznik wszystkich iteracji
        # iterations = 0
        # # wartość funkcji celu dla najleoszego rozwiązania
        # best_cost = -np.inf
        #
        # # lista best_results przechowuje najlepsze wyniki w każdej iteracji
        # best_results = []
        #
        # while iter_with_no_progress <= max_iter_no_progress and iterations <= max_iter:
        #     # Kryterium stopu algorytmu jest osiągnięcie maksymalnej liczby iteracji bez poprawy
        #     # lub osiągnięcie maksymalnej iteracji w ogóle.
        #     iterations += 1
        #
        #     # licznik dzieci utworzonych w danej iteracji
        #     children_count = 0
        #     # lista przechowująca nowe rozwiązania (dzieci)
        #     children = []
        #     # aktualny procent populacji, która zostanie
        #     # zastąpiona przez nowych członków
        #     replaced = 0
        #
        #     while replaced < replacement_rate:
        #         # wybieramy rodzicow i tworzymy dziecko
        #
        #         pass
        #
        #         # następnie losujemy liczbę z zakresu 0-1 i sprawdzamy
        #         # czy mamy dokonać mutacji dziecka.

        #return population[-1][0], population[-1][1], iterations, best_results


if __name__ == "__main__":
    main()