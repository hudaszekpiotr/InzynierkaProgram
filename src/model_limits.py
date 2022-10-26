#!/usr/bin/python
# -*- coding: utf-8 -*-
from solution_classes import Solution


#file includes functions checking if solution is acceptable

#na kazdym polu w danym dniu moze byc uprawiana maksymalnie jedna uprawa

def daily_resources_ok(solution, resources, cultivation_types):
    for day in solution.days:
        daily_dict = {}
        for field in day.field:
            if field is not None:
                iter_resources = cultivation_types[field[0]]["daily_resources"][field[1]]
                for key in iter_resources:
                    if key in daily_dict:
                        daily_dict[key] += iter_resources[key]
                    else:
                        daily_dict[key] = iter_resources[key]
        for key in daily_dict:
            if key not in resources["daily_resources"]:
                print("error1", day, key)
                return day, key
            elif resources["daily_resources"][key] < daily_dict[key]:
                print("error2", day, key)
                return day, key

def entire_period_resources(solution, resources, cultivation_types):
    pass