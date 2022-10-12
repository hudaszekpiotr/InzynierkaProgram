import json
import re

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
        resources = list_of_dicts[cultivation]["needed_resources"]
        i = 0
        while i < len(resources):
            if "duration" in resources[i]:
                duration = resources[i]["duration"]
                del resources[i]['duration']
                raw_resources = resources[i]
                del resources[i]
                for k in range(int(duration)):
                    resources.insert(i, raw_resources)
                    i += 1
                i -= 1

            i += 1