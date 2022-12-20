import datetime
import timeit

import pandas as pd
from pandas import DataFrame

from src.optimization import Optimization
from src.parameters import Parameters


parameters = Parameters(max_iter=1000, max_iter_no_progress=100000, start_date=datetime.date(2022, 4, 1),
                         num_days=60, crossover_type="fields", mutation_probability=0.5,
                         initial_population_type="partially filled solutions", population_size=100,
                         unacceptable_fix_type="fixup", penalty_multiplier_first=20,
                         penalty_multiplier_last=20, selection_type="ranking",
                         mating_pool_size=40, elite_size=0, tournament_size=2,
                         mutation_type="removing/adding")

#"only adding", "removing/adding"

#filenames = ["dataset-few-resources.json", "dataset-standard-amount-resources.json", "dataset-many-resources.json"]
filenames = ["dataset-few-resources.json", "dataset-standard-amount-resources.json"]
#unacceptable_fix_types = ["penalty-only-adding", "penalty-removing/adding", "fixup-only-adding", "fixup-removing/adding"]
unacceptable_fix_types = ["penalty-only-adding", "penalty-removing/adding"]
repeat_times = 10

data = {}
for filename in filenames:
    average = []
    for unacceptable_fix_type in unacceptable_fix_types:
        if unacceptable_fix_type == "penalty-removing/adding":
            parameters.unacceptable_fix_type = "penalty"
            parameters.mutation_type = "removing/adding"
        elif unacceptable_fix_type == "penalty-only-adding":
            parameters.unacceptable_fix_type = "penalty"
            parameters.mutation_type = "only adding"
        elif unacceptable_fix_type == "fixup-removing/adding":
            parameters.unacceptable_fix_type = "fixup"
            parameters.mutation_type = "removing/adding"
        else:
            parameters.unacceptable_fix_type = "fixup"
            parameters.mutation_type = "only adding"
        optimization = Optimization(filename)
        results = []
        print(str(unacceptable_fix_type)+ " "+ filename)
        for i in range(repeat_times):
            _, df_resources, period_df, best_results = optimization.run_algorithm(parameters, False)
            df_resources = df_resources > 100
            period_df = period_df > 100
            if df_resources.any(axis=None):
                print("unnacceptable daily resources")
            if period_df.any(axis=None):
                print("unnacceptable period resources")
            results.append(max(best_results))
        average.append(sum(results) / len(results))

    data[filename] = pd.Series(average, dtype='float64')
df = pd.DataFrame(data=data)
print(df)

