import datetime

from src.optimization import Optimization
from src.model_data_operations import load_files
from src.parameters import Parameters


def main():
    optimization = Optimization('../numerical_tests/dataset-standard.json')
    parameters = Parameters(max_iter=200, max_iter_no_progress=100000, start_date=datetime.date(2022, 4, 1),
                            num_days=60, crossover_type="fields", mutation_probability=0.5,
                            initial_population_type="partially filled solutions", population_size=100,
                            unacceptable_fix_type="fixup", penalty_multiplier_first=1,
                            penalty_multiplier_last=1, selection_type="ranking",
                            mating_pool_percent=40, elite_percent=0, tournament_size=2,
                            mutation_type="only adding")

    df, df_resources, period_df, best_results = optimization.run_algorithm(parameters, True)


if __name__ == "__main__":
    main()
