from matplotlib import pyplot as plt


import datetime

import pandas as pd
from pandas import DataFrame

from src.optimization import Optimization
from src.parameters import Parameters

optimization = Optimization('dataset-standard.json')
parameters = Parameters(max_iter=0, max_iter_no_progress=100000, start_date=datetime.date(2022, 4, 1),
                        num_days=60, crossover_type="fields", mutation_probability=0.5,
                        initial_population_type="partially filled solutions", population_size=100,
                        unacceptable_fix_type="fixup", penalty_multiplier_first=1,
                        penalty_multiplier_last=1, selection_type="ranking",
                        mating_pool_percent=40, elite_percent=0, tournament_size=2,
                        mutation_type="only adding")

selection_types = ["roulette wheel", "tournament", "ranking"]
polish_names = {"roulette wheel": "metoda ruletki",
                "tournament": "turniejowa",
                "ranking": "rankingowa"}


for selection_type in selection_types:
    parameters.selection_type = selection_type
    parameters.max_iter = 2000
    _, _, _, best_results = optimization.run_algorithm(parameters, False)

    plt.plot(best_results, label=polish_names[selection_type])

plt.xlabel("iteracja")
plt.ylabel("zysk")
plt.title("Metody selekcji")
plt.legend()
plt.show()


