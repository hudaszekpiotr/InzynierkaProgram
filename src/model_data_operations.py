import json
from datetime import date


def parse_resources(list_of_dicts):
    for cultivation in list_of_dicts:
        resources = cultivation["daily_resources"]
        i = 0
        while i < len(resources):
            if "duration" in resources[i]:
                duration = resources[i]["duration"]
                raw_resources = resources[i]["values"]
                del resources[i]
                for k in range(int(duration)):
                    resources.insert(i, raw_resources)
                    i += 1
                i -= 1
            i += 1

        while i < cultivation["duration"]:
            resources.append({})
            i += 1


def elite_and_mating_sizes(mating_pool_percent, elite_percent, population_size):
    mating_pool_size = int(mating_pool_percent * 0.01 * population_size)
    if mating_pool_size <= 1:
        mating_pool_size = 2
    if mating_pool_size == population_size:
        mating_pool_size = population_size - 1

    elite_size = int(elite_percent * 0.01 * population_size)
    if elite_size == 0 and elite_percent > 0:
        elite_size = 1
    if elite_size == population_size:
        elite_size = population_size - 1

    return mating_pool_size, elite_size


def load_files(file_name):
    with open(file_name) as file:
        model_data = json.load(file)
    cultivation_types = model_data["cultivation_types"]
    resources = model_data["resources"]
    fields = model_data["fields"]
    parse_resources(cultivation_types)
    return resources, fields, cultivation_types


def transform_cult_types_start_date(cultivation_types, alg_start_date):
    for i in cultivation_types:
        cult_type_start_date = date(alg_start_date.year, i["start_date"]["month"], i["start_date"]["day"])
        delta = cult_type_start_date - alg_start_date
        plus_minus_days = i["start_date"]["plus_minus_days"]
        i["start_date"] = [delta.days - plus_minus_days, delta.days + plus_minus_days]
