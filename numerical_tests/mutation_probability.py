import datetime

import pandas as pd
from pandas import DataFrame

from src.optimization import Optimization
from src.parameters import Parameters

optimization = Optimization('dataset-standard.json')
parameters = Parameters(max_iter=0, max_iter_no_progress=100000, start_date=datetime.date(2022, 4, 1),
                        num_days=60, crossover_type="fields", mutation_probability=0,
                        initial_population_type="partially filled solutions", population_size=100,
                        unacceptable_fix_type="fixup", penalty_multiplier_first=1,
                        penalty_multiplier_last=1, selection_type="ranking",
                        mating_pool_percent=40, elite_percent=0, tournament_size=2,
                        mutation_type="only adding")

#df, df_resources, period_df, best_results = optimization.run_algorithm(parameters)

max_iter_list = [100, 250, 500, 1000, 2000]
mutation_probability_list = [0.3, 0.4, 0.5, 0.6, 0.7]
repeat_times = 10

df = DataFrame()

data = {}
for max_iter in max_iter_list:
    parameters.max_iter = max_iter
    average = []
    print("\nmax iter "+str(max_iter))
    for mutation_probability in mutation_probability_list:
        parameters.mutation_probability = mutation_probability
        results = []
        print("mutation_probability "+str(mutation_probability))
        for i in range(repeat_times):
            _, _, _, best_results = optimization.run_algorithm(parameters, False)
            results.append(max(best_results))
        average.append(sum(results) / len(results))

    data[max_iter] = pd.Series(average, dtype='float64')
    print(data)
df = pd.DataFrame(data=data)

print(df)
