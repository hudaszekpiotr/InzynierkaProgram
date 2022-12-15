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




def load_files():
    json_model_data = open('../data/model_data.json')
    model_data = json.load(json_model_data)
    json_model_data.close()
    cultivation_types = model_data["cultivation_types"]
    resources = model_data["resources"]
    fields = model_data["fields"]
    parse_resources(cultivation_types)


    return resources, fields, cultivation_types