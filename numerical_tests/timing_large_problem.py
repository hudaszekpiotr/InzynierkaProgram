import datetime
import time
import timeit

import pandas as pd
from pandas import DataFrame

from src.optimization import Optimization
from src.parameters import Parameters

optimization = Optimization('dataset-large.json')
parameters = Parameters(max_iter=0, max_iter_no_progress=100000, start_date=datetime.date(2022, 4, 1),
                        num_days=180, crossover_type="fields", mutation_probability=0.5,
                        initial_population_type="partially filled solutions", population_size=100,
                        unacceptable_fix_type="fixup", penalty_multiplier_first=1,
                        penalty_multiplier_last=1, selection_type="ranking",
                        mating_pool_percent=40, elite_percent=0, tournament_size=2,
                        mutation_type="only adding")


max_iter_list = [100, 250, 500, 1000, 2000]
repeat_times = 10

df = DataFrame()

average_result = []
average_time = []
for max_iter in max_iter_list:
    parameters.max_iter = max_iter
    results = []
    times = []
    print(max_iter)
    for i in range(repeat_times):
        t0 = time.perf_counter()
        _, _, _, best_results = optimization.run_algorithm(parameters, False)
        t1 = time.perf_counter()
        times.append(t1 - t0)
        results.append(max(best_results))
    average_result.append(sum(results) / len(results))
    average_time.append(sum(times) / len(times))
    print(average_result)
    print(average_time)


print(average_result)
print(average_time)
