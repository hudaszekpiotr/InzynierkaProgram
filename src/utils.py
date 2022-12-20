import json


def parse_resources(list_of_dicts):
    for cultivation in range(len(list_of_dicts)):
        resources = list_of_dicts[cultivation]["daily_resources"]
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

        while i < list_of_dicts[cultivation]["duration"]:
            resources.append({})
            i += 1


def find_best_solution(population):
    best_so_far = population[0]
    for index, sol in enumerate(population):
        if sol.fitness > best_so_far.fitness:
            best_so_far = sol
    return best_so_far


def load_files(file_name):
    json_model_data = open(file_name)
    model_data = json.load(json_model_data)
    json_model_data.close()
    cultivation_types = model_data["cultivation_types"]
    resources = model_data["resources"]
    fields = model_data["fields"]
    parse_resources(cultivation_types)


    return resources, fields, cultivation_types