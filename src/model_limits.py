#!/usr/bin/python
# -*- coding: utf-8 -*-
import collections
import copy
import functools
import math
import random

import pandas as pd
import operator

from src.genetic_operators import clear_slot


# def solution_is_valid(solution):
#     for day in solution.days:
#         for field in day.field:
#             if field is not None and type(field) is not tuple:
#                 raise ValueError
#             if type(field) is tuple and len(field) != 2:
#                 raise ValueError


def get_used_resources(solution, cultivation_types):
    daily_resources_list = [{}] * solution.num_days
    period_dict = {}

    for field_index, field in enumerate(solution.data):
        for crop in field:
            iter_resources = cultivation_types[crop[0]]["entire_period_resources"]
            for key in iter_resources:
                if key in period_dict:
                    period_dict[key] += iter_resources[key]
                else:
                    period_dict[key] = iter_resources[key]
            resources_list = cultivation_types[crop[0]]["daily_resources"]
            for day, daily_dict in enumerate(resources_list):
                final_dict = daily_resources_list[day + crop[1]]
                for key in daily_dict:
                    if key in dict:
                        final_dict[key] += daily_dict[key]
                    else:
                        final_dict[key] = daily_dict[key]
    return daily_resources_list, period_dict

def penalty(solution, cultivation_types, resources):
    penalty_val = 0
    daily_resources_list, period_dict = get_used_resources(solution, cultivation_types)
    for daily_dict in daily_resources_list:
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
    for count, day in enumerate(solution.matrix.T):
        daily_dict = {}
        for field in day:
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

def resources_used_day_field(solution, field, day, cultivation_types):
    for index in solution[field]:
        if index[1] <= day <= index[1] + cultivation_types[index[0]]["duration"]:
            resources_crop = cultivation_types[index[0]]["daily_resources"][day]
            return resources_crop, index
    return None, None

def remove_resources_from_list(daily_resources_list, period_dict, day, daily_resources_to_del, period_resources_to_del):
    days = list(range(day, len(daily_resources_to_del)+day))+day
    for day_index in days:
        for key in daily_resources_to_del:
            daily_resources_list[day_index][key] -= daily_resources_to_del[key]

    for key in period_resources_to_del:
        period_dict[key] -= period_resources_to_del[key]




def fixup(solution, cultivation_types, resources):
    daily_resources_list, period_dict = get_used_resources(solution, cultivation_types)

    for day, daily_dict in enumerate(daily_resources_list):
        for key in daily_dict:
            if key not in resources["daily_resources"]:
                raise ValueError
            diff = resources["daily_resources"][key] - daily_dict[key]
            if diff < 0:
                fields_shuffled_num = list(range(solution.num_fields))
                random.shuffle(fields_shuffled_num)
                for field_index in fields_shuffled_num:
                    resources_crop, index = resources_used_day_field(solution, field_index, day, cultivation_types)
                    if index is None or key not in resources_crop:
                        continue
                    else:
                        crop_type = solution[field_index][index][0]
                        daily_resources_to_del = cultivation_types[crop_type]["daily_resources"]
                        period_resources_to_del = cultivation_types[crop_type]["entire_period_resources"]
                        solution.data[field_index].pop(index)
                        remove_resources_from_list(daily_resources_list, period_dict, day, daily_resources_to_del,
                                                   period_resources_to_del)
                        diff = resources["daily_resources"][key] - daily_dict[key]
                        if diff >= 0:
                            break

    for key in period_dict:
        if key not in resources["entire_period_resources"]:
            raise ValueError(str(key))
        diff = resources["entire_period_resources"][key] - period_dict[key]
        if diff < 0:
            fields_shuffled_num = list(range(solution.num_fields))
            random.shuffle(fields_shuffled_num)
            for field_index in fields_shuffled_num:
                indexes_shuffled = copy.deepcopy(solution.data[field_index])
                random.shuffle(indexes_shuffled)
                for index in indexes_shuffled:
                    crop_type = solution.data[field_index][index][0]
                    period_resources_to_del = cultivation_types[crop_type]["entire_period_resources"]
                    remove_resources_from_list(daily_resources_list, period_dict, 0, [], period_resources_to_del)




