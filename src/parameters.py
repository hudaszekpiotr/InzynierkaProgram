from dataclasses import dataclass
from datetime import date

@dataclass
class Parameters:
    max_iter: int
    max_iter_no_progress: int
    start_date: date
    #mutation_probability: float
    #crossover_type: str
    #unacceptable_fix_type: str # penalty_function
    #selection_type: str # roulette_wheel
    #initial_population_type: str # empty_solutions partially_filled_solutions

