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


max_iter_list = [100, 250, 500, 1000, 2000]
crossover_types = ["days", "fields"]
repeat_times = 10


data = {}
for max_iter in max_iter_list:
    parameters.max_iter = max_iter
    average = []
    print(f"\nmax iter {max_iter}")
    for crossover_type in crossover_types:
        parameters.crossover_type = crossover_type
        results = []
        print(f"crossover_type {crossover_type}")
        for i in range(repeat_times):
            _, _, _, best_results = optimization.run_algorithm(parameters, False)
            results.append(max(best_results))
        average.append(sum(results) / len(results))

    data[max_iter] = pd.Series(average, dtype='float64')
    print(data)
df = pd.DataFrame(data=data)

print(df)
