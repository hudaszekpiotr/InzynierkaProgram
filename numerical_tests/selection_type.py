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
                        mating_pool_size=40, elite_size=0, tournament_size=2,
                        mutation_type="only adding")

#df, df_resources, period_df, best_results = optimization.run_algorithm(parameters)

max_iter_list = [100, 250, 500, 1000, 2000]
selection_types = ["roulette wheel", "tournament", "ranking"]
repeat_times = 10

df = DataFrame()

data = {}
for max_iter in max_iter_list:
    parameters.max_iter = max_iter
    average = []
    print("\nmax iter "+str(max_iter))
    for selection_type in selection_types:
        parameters.selection_type = selection_type
        results = []
        print("mutation_probability "+str(selection_type))
        for i in range(repeat_times):
            _, _, _, best_results = optimization.run_algorithm(parameters, False)
            results.append(max(best_results))
        average.append(sum(results) / len(results))

    data[max_iter] = pd.Series(average, dtype='float64')
    print(data)
df = pd.DataFrame(data=data)

print(df)
