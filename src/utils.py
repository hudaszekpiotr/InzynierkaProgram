import json
import re

# "profit": ["1*5","3*5","5*20"],
#not used now
def parse_price(list_of_dicts):
    for cultivation in range(len(list_of_dicts)):
        price = list_of_dicts[cultivation]["price"]
        i = 0
        while i < len(price):
            if isinstance(price[i], str):
                if re.search("""^\d*\*\d*$""", price[i]) is not None:
                    amount, multiplier = price[i].split("*")
                    del price[i]
                    for k in range(int(multiplier)):
                        price.insert(i, int(amount))
                        i += 1
                    i -= 1

            i += 1

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
    json_cultivation_types = open('../sample_data/cultivation_types.json')
    cultivation_types = json.load(json_cultivation_types)
    json_cultivation_types.close()

    # print(json.dumps(cultivation_types, indent=2))
    # print("\nparsed:")
    # parse_price(cultivation_types)
    parse_resources(cultivation_types)
    # print(json.dumps(cultivation_types, indent=2))
    # for i in cultivation_types:
    #     print(i)

    json_fields = open('../sample_data/fields.json')
    fields = json.load(json_fields)
    json_fields.close()
    # print(json.dumps(fields, indent=2))

    json_resources = open('../sample_data/resources.json')
    resources = json.load(json_resources)
    json_resources.close()
    # print(json.dumps(resources, indent=2))

    return resources, fields, cultivation_types