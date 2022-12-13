#!/usr/bin/python
# -*- coding: utf-8 -*-
import collections
import functools
import math
import random

import pandas as pd
import operator

from src.genetic_operators import clear_slot


def solution_is_valid(solution):
    for day in solution.days:
        for field in day.field:
            if field is not None and type(field) is not tuple:
                raise ValueError
            if type(field) is tuple and len(field) != 2:
                raise ValueError


def daily_resources_ok(solution, resources, cultivation_types):
    for day in solution.days:
        daily_dict = resources_dict(day, cultivation_types)
        for key in daily_dict:
            if key not in resources["daily_resources"]:
                print("error1", day, key)
                return day, key
            elif resources["daily_resources"][key] < daily_dict[key]:
                print("error2", day, key)
                return day, key



def penalty(solution, cultivation_types, resources):
    penalty_val = 0
    period_dict = {}
    for count, day in enumerate(solution.days):
        daily_dict = {}
        for field in day.fields:
            if field is not None:
                iter_resources = cultivation_types[field[0]]["daily_resources"][field[1]]
                for key in iter_resources:
                    if key in daily_dict:
                        daily_dict[key] += iter_resources[key]
                    else:
                        daily_dict[key] = iter_resources[key]

                if field[1] == 0:
                    iter_resources = cultivation_types[field[0]]["entire_period_resources"]
                    for key in iter_resources:
                        if key in period_dict:
                            period_dict[key] += iter_resources[key]
                        else:
                            period_dict[key] = iter_resources[key]

        for key in daily_dict:
            if key not in resources["daily_resources"]:
                raise ValueError
            diff = resources["daily_resources"][key] - daily_dict[key]
            if diff < 0:
                penalty_val += abs(diff)/resources["daily_resources"][key] * 100

    for key in period_dict:
        if key not in resources["entire_period_resources"]:
            raise ValueError(str(key))
        diff = resources["entire_period_resources"][key] - period_dict[key]
        if diff < 0:
            penalty_val += abs(diff) / resources["entire_period_resources"][key] * 100
    return penalty_val


def resources_percent(solution, cultivation_types, resources):
    df, period_dict = resources_df(solution, cultivation_types)
    #print(df)
    for column in df:
        for row in df.index:
            if math.isnan(df[column][row]):
                df[column][row] = 0.0
            df[column][row] = (df[column][row]/resources['daily_resources'][row])*100
    df = df.transpose()
    return df, period_dict

def resources_df(solution, cultivation_types):
    df = pd.DataFrame()

    period_dict = {}
    data = {}
    for count, day in enumerate(solution.days):
        daily_dict = {}
        for field in day.fields:
            if field is not None:
                iter_resources = cultivation_types[field[0]]["daily_resources"][field[1]]
                for key in iter_resources:
                    if key in daily_dict:
                        daily_dict[key] += iter_resources[key]
                    else:
                        daily_dict[key] = iter_resources[key]

                if field[1] == 0:
                    iter_resources = cultivation_types[field[0]]["entire_period_resources"]
                    for key in iter_resources:
                        if key in period_dict:
                            period_dict[key] += iter_resources[key]
                        else:
                            period_dict[key] = iter_resources[key]

        data["day" + str(count)] = pd.Series(daily_dict, dtype='float64')
    df = pd.DataFrame(data=data)
    return df, period_dict


def fixup(solution, cultivation_types, resources):
    penalty_val = 0
    period_dict = {}
    daily_resources_list = []
    for count, day in enumerate(solution.days):
        daily_dict = {}
        for field in day.fields:
            if field is not None:
                iter_resources = cultivation_types[field[0]]["daily_resources"][field[1]]
                for resource in iter_resources:
                    if resource in daily_dict:
                        daily_dict[resource] += iter_resources[resource]
                    else:
                        daily_dict[resource] = iter_resources[resource]

                if field[1] == 0:
                    iter_resources = cultivation_types[field[0]]["entire_period_resources"]
                    for resource in iter_resources:
                        if resource in period_dict:
                            period_dict[resource] += iter_resources[resource]
                        else:
                            period_dict[resource] = iter_resources[resource]
        daily_resources_list.append(daily_dict)

    for count, day in enumerate(solution.days):
        daily_dict = daily_resources_list[count]
        for resource in daily_dict:
            if resource not in resources["daily_resources"]:
                raise ValueError
            diff = resources["daily_resources"][resource] - daily_dict[resource]
            if diff < 0:
                fields_num_list = list(range(len(day.fields)))
                random.shuffle(fields_num_list)

                for field_count in fields_num_list:
                    if diff >= 0:
                        break
                    if day.fields[field_count] is None:
                        continue
                    daily_resources_current_field = cultivation_types[day.fields[field_count][0]]["daily_resources"][day.fields[field_count][1]]
                    period_resources_current_field = cultivation_types[day.fields[field_count][0]]["entire_period_resources"]
                    if resource in daily_resources_current_field:
                        duration = cultivation_types[day.fields[field_count][0]]["duration"]
                        for key in daily_resources_current_field:
                            daily_dict[key] += daily_resources_current_field[key]
                        for key in period_resources_current_field:
                            period_dict[key] += period_resources_current_field[key]
                        diff = resources["daily_resources"][resource] - daily_dict[resource]
                        clear_slot(solution, count, duration, field_count)

