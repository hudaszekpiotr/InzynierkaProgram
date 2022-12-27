import random

from src.genetic_operators import crossover, add_to_solution, clear_slot, remove_random_cultivation_from_solution, \
    mutate_solution, selection
from src.solution_classes import Solution, SolutionAndFitness


def test_crossover_fields():
    solution1 = Solution(num_fields=5, num_days=30)
    solution2 = Solution(num_fields=5, num_days=30)
    solution1.data = [[(0, 0)], [(0, 2)], [(0, 4)], [(0, 6)], [(0, 8)]]
    solution2.data = [[(1, 1)], [(1, 3)], [(1, 5)], [(1, 7)], [(1, 9)]]

    child1, child2 = crossover(solution1, solution2, "fields", None)

    child1_expected = Solution(num_fields=5, num_days=30)
    child2_expected = Solution(num_fields=5, num_days=30)
    child1_expected.data = [[(1, 1)], [(0, 2)], [(1, 5)], [(0, 6)], [(1, 9)]]
    child2_expected.data = [[(0, 0)], [(1, 3)], [(0, 4)], [(1, 7)], [(0, 8)]]
    assert child1.data == child1_expected.data
    assert child2.data == child2_expected.data


def test_crossover_days_not_overlapping():
    cultivation_types = [{"name": "type1",
                          "duration": 5},
                         {"name": "type2",
                          "duration": 7}]
    solution1 = Solution(num_fields=2, num_days=30)
    solution2 = Solution(num_fields=2, num_days=30)
    solution1.data = [[(0, 0), (0, 17)], [(0, 1), (0, 18)]]
    solution2.data = [[(1, 0), (1, 17)], [(1, 1), (1, 18)]]

    child1, child2 = crossover(solution1, solution2, "days", cultivation_types)

    child1_expected = Solution(num_fields=2, num_days=30)
    child2_expected = Solution(num_fields=2, num_days=30)
    child1_expected.data = [[(0, 0), (1, 17)], [(0, 1), (1, 18)]]
    child2_expected.data = [[(1, 0), (0, 17)], [(1, 1), (0, 18)]]
    assert child1.data == child1_expected.data
    assert child2.data == child2_expected.data


def test_crossover_days_overlapping():
    cultivation_types = [{"name": "type1",
                          "duration": 5},
                         {"name": "type2",
                          "duration": 7}]
    solution1 = Solution(num_fields=2, num_days=30)
    solution2 = Solution(num_fields=2, num_days=30)
    solution1.data = [[(0, 0), (0, 14), (0, 24)], [(0, 0), (0, 14), (0, 24)]]
    solution2.data = [[(1, 0), (1, 17), (1, 24)], [(1, 1), (1, 17), (1, 24)]]

    child1, child2 = crossover(solution1, solution2, "days", cultivation_types)

    child1_expected = Solution(num_fields=2, num_days=30)
    child2_expected = Solution(num_fields=2, num_days=30)
    child1_expected.data = [[(0, 0), (0, 14), (1, 24)], [(0, 0), (0, 14), (1, 24)]]
    child2_expected.data = [[(1, 0), (0, 14), (0, 24)], [(1, 1), (0, 14), (0, 24)]]
    assert child1.data == child1_expected.data
    assert child2.data == child2_expected.data


def test_add_to_solution():
    solution = Solution(num_fields=2, num_days=30)
    solution.data = [[(0, 0), (0, 17)], [(0, 1), (0, 18)]]

    day = 12
    field = 0
    crop_type = 3

    add_to_solution(solution, day, field, crop_type)

    assert solution.data == [[(0, 0), (3, 12), (0, 17)], [(0, 1), (0, 18)]]


def test_clear_slot():
    solution = Solution(num_fields=2, num_days=30)
    solution.data = [[(0, 0), (0, 12), (0, 17), (0, 25)], [(0, 1), (0, 18)]]
    cultivation_types = [{"name": "type1",
                          "duration": 4},
                         {"name": "type2",
                          "duration": 7}]
    start_day = 14
    duration = 5
    field = 0

    clear_slot(solution, start_day, duration, field, cultivation_types)

    assert solution.data == [[(0, 0), (0, 25)], [(0, 1), (0, 18)]]


def test_remove_random_cultivation_from_solution():
    solution = Solution(num_fields=2, num_days=30)
    solution.data = [[(0, 0), (0, 17)], [(0, 1), (0, 18)]]

    random.seed(0)
    remove_random_cultivation_from_solution(solution)

    assert solution.data == [[(0, 0), (0, 17)], [(0, 1)]]


def test_mutate_solution():
    solution = Solution(num_fields=2, num_days=30)
    solution.data = [[(0, 0), (0, 25)], [(0, 1), (0, 18)]]
    cultivation_types = [{"name": "type1",
                          "start_date": [1, 30],
                          "duration": 4},
                         {"name": "type2",
                          "start_date": [1, 30],
                          "duration": 7}]
    fields = [{"coefficients": {"type1": 1.5,
                                "type2": 1.3}},
              {"coefficients": {"type1": 1.0,
                                "type2": 2.0}}]

    random.seed(0)
    mutate_solution(solution, True, "only adding", cultivation_types, fields)
    assert solution.data == [[(0, 0), (0, 25)], [(0, 1), (1, 14)]]


def test_selection_ranking():
    sol1 = SolutionAndFitness(solution=None, fitness=10)
    sol2 = SolutionAndFitness(solution=None, fitness=-3)
    sol3 = SolutionAndFitness(solution=None, fitness=-9)
    sol4 = SolutionAndFitness(solution=None, fitness=-1)
    population = [sol1, sol2, sol3, sol4]

    mating_pool = selection(population, mating_pool_size=2, selection_type="ranking", tournament_size=2, is_sorted=False)

    assert mating_pool == [sol1, sol4] or mating_pool == [sol4, sol1]

def test_selection_roulette():
    sol1 = SolutionAndFitness(solution=None, fitness=10)
    sol2 = SolutionAndFitness(solution=None, fitness=-3)
    sol3 = SolutionAndFitness(solution=None, fitness=-9)
    sol4 = SolutionAndFitness(solution=None, fitness=-1)
    population = [sol1, sol2, sol3, sol4]

    random.seed(1)
    mating_pool = selection(population, mating_pool_size=2, selection_type="roulette wheel", tournament_size=2, is_sorted=False)

    assert mating_pool == [sol1, sol4]

def test_selection_tournament():
    sol1 = SolutionAndFitness(solution=None, fitness=10)
    sol2 = SolutionAndFitness(solution=None, fitness=-3)
    sol3 = SolutionAndFitness(solution=None, fitness=-9)
    sol4 = SolutionAndFitness(solution=None, fitness=-1)
    population = [sol1, sol2, sol3, sol4]

    random.seed(0)
    mating_pool = selection(population, mating_pool_size=2, selection_type="tournament", tournament_size=2, is_sorted=False)

    assert mating_pool == [sol2, sol1]
