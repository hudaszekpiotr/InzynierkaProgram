from dataclasses import dataclass
from datetime import date
from typing import Literal


@dataclass
class Parameters:
    max_iter: int
    max_iter_no_progress: int
    #_______________________
    start_date: date
    num_days: int
    #_____________________
    mutation_probability: float
    crossover_type: Literal["days", "fields"]
    #______________________________________
    initial_population_type: Literal["empty solutions", "partially filled solutions"]
    population_size: int
    #______________________________
    unacceptable_fix_type: Literal["penalty", "fixup"]
    penalty_multiplier_first: float
    penalty_multiplier_last: float
    #____________________________
    selection_type: Literal["roulette wheel", "tournament", "ranking"]
    mating_pool_size: float #percent
    elite_size: float #percent
    tournament_size: int



