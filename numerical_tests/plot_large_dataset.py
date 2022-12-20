from matplotlib import pyplot as plt


import datetime

import pandas as pd
from pandas import DataFrame

from src.optimization import Optimization
from src.parameters import Parameters


parameters = Parameters(max_iter=0, max_iter_no_progress=100000, start_date=datetime.date(2022, 4, 1),
                        num_days=180, crossover_type="fields", mutation_probability=0.5,
                        initial_population_type="partially filled solutions", population_size=100,
                        unacceptable_fix_type="fixup", penalty_multiplier_first=1,
                        penalty_multiplier_last=1, selection_type="ranking",
                        mating_pool_size=40, elite_size=0, tournament_size=2,
                        mutation_type="only adding")

optimization = Optimization('dataset-large.json')
parameters.max_iter = 2000

_, _, _, best_results = optimization.run_algorithm(parameters, False)

plt.plot(best_results)

plt.xlabel("iteracja")
plt.ylabel("zysk")
plt.title("Zysk dla instrukcji testowej o dużym rozmiarze")
plt.show()


