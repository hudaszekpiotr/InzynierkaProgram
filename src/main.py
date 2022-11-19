import json

from src.optimization import Optimization
from src.utils import parse_resources, load_files


def main():
    resources, fields, cultivation_types = load_files()
    optimization = Optimization(resources, fields, cultivation_types)
    optimization.evolution_algorithm()


if __name__ == "__main__":
    main()