from dataclasses import dataclass
from datetime import date
from typing import Literal


@dataclass
class Parameters:
    max_iter: int
    max_iter_no_progress: int

    start_date: date
    num_days: int

    mutation_probability: float
    mutation_type: Literal["only adding", "removing/adding"]
    crossover_type: Literal["days", "fields"]

    initial_population_type: Literal["empty solutions", "partially filled solutions"]
    population_size: int

    unacceptable_fix_type: Literal["penalty", "fixup"]
    penalty_multiplier_first: float
    penalty_multiplier_last: float

    selection_type: Literal["roulette wheel", "tournament", "ranking"]
    mating_pool_percent: float
    elite_percent: float
    tournament_size: int



