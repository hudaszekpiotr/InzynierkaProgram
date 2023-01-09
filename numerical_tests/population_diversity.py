import datetime

from matplotlib import pyplot as plt

from src.optimization import Optimization
from src.parameters import Parameters

optimization = Optimization('dataset-standard.json')

max_iter = 2000
parameters = Parameters(max_iter=max_iter, max_iter_no_progress=100000, start_date=datetime.date(2022, 4, 1),
                        num_days=60, crossover_type="fields", mutation_probability=0.5,
                        initial_population_type="partially filled solutions", population_size=100,
                        unacceptable_fix_type="fixup", penalty_multiplier_first=1,
                        penalty_multiplier_last=1, selection_type="ranking",
                        mating_pool_percent=40, elite_percent=0, tournament_size=2,
                        mutation_type="only adding")


#selection_types = ["tournament"]
selection_types = ["ranking"]

data = {}
average = []

for selection_type in selection_types:
    parameters.selection_type = selection_type
    results = []
    _, _, _, best_results, all_results = optimization.run_algorithm(parameters, False, info_about_population=True)
    average_results = [sum(elem)/len(elem) for elem in all_results]
    worst_results = [min(elem) for elem in all_results]
    plt.plot(average_results, label="średni wynik")
    plt.fill_between(range(max_iter+1), worst_results, best_results, alpha=0.6, label="przedział dla populacji")

plt.xlabel("iteracja")
plt.ylabel("zysk")
plt.legend()
plt.title("Różnorodność populacji dla selekcji rankingowej")
plt.show()

