#!/usr/bin/python
# -*- coding: utf-8 -*-

import copy
import math
import random
import pandas as pd



def get_used_resources(solution, cultivation_types):
    daily_resources_list = [{} for i in range(solution.num_days)]
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
                for key in daily_dict:
                    if key in daily_resources_list[day + crop[1]]:
                        daily_resources_list[day + crop[1]][key] += daily_dict[key]
                    else:
                        daily_resources_list[day + crop[1]][key] = daily_dict[key]
    return daily_resources_list, period_dict


def penalty(solution, cultivation_types, resources, multiplier):
    penalty_val = 0
    daily_resources_list, period_dict = get_used_resources(solution, cultivation_types)
    for daily_dict in daily_resources_list:
        for key in daily_dict:
            if key not in resources["daily_resources"]:
                raise ValueError
            diff = resources["daily_resources"][key] - daily_dict[key]
            if diff < 0:
                penalty_val += abs(diff)/resources["daily_resources"][key] * 100 * multiplier

    for key in period_dict:
        if key not in resources["entire_period_resources"]:
            raise ValueError(str(key))
        diff = resources["entire_period_resources"][key] - period_dict[key]
        if diff < 0:
            penalty_val += abs(diff) / resources["entire_period_resources"][key] * 100 * multiplier
    return penalty_val


def resources_percent(solution, cultivation_types, resources):
    df, period_df = resources_df(solution, cultivation_types)
    for key in period_df:
        period_df[key] = (period_df[key]/resources['entire_period_resources'][key])*100
    #print(df)
    for column in df:
        for row in df.index:
            if math.isnan(df[column][row]):
                df[column][row] = 0.0
            df[column][row] = (df[column][row]/resources['daily_resources'][row])*100
    df = df.transpose()
    return df, period_df

def resources_df(solution, cultivation_types):
    df = pd.DataFrame()
    data = {}
    daily_resources_list, period_dict = get_used_resources(solution, cultivation_types)
    for count, daily_dict in enumerate(daily_resources_list):
        data[count+1] = pd.Series(daily_dict, dtype='float64')
    df = pd.DataFrame(data=data)
    for key in period_dict:
        period_dict[key] = [period_dict[key]]
    period_df = pd.DataFrame(data=period_dict)
    return df, period_df

def resources_used_day_field(solution, field, day, cultivation_types):
    for index, crop in enumerate(solution.data[field]):
        if crop[1] <= day < crop[1] + cultivation_types[crop[0]]["duration"]:
            if crop[0] >= len(cultivation_types):
                print(crop)
                print(cultivation_types)
                raise RuntimeError
            if day-crop[1] >= len(cultivation_types[crop[0]]["daily_resources"]):
                print(crop)
                print(cultivation_types)
                print(day - crop[1])
                print(cultivation_types[crop[0]]["daily_resources"])
                raise RuntimeError
            resources_crop = cultivation_types[crop[0]]["daily_resources"][day - crop[1]]
            return resources_crop, index
    return None, None

def remove_resources_from_list(daily_resources_list, period_dict, day, daily_resources_to_del, period_resources_to_del):
    days = list(range(day, len(daily_resources_to_del)+day))
    for day_to_del, day_index in enumerate(days):
        for key in daily_resources_to_del[day_to_del]:
            if key not in daily_resources_list[day_index]:
                print(key)
                print(daily_resources_list)
                print(day_index)
                print(daily_resources_to_del)
                print(day_to_del)
                raise RuntimeError
            daily_resources_list[day_index][key] -= daily_resources_to_del[day_to_del][key]

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
                        crop_type = solution.data[field_index][index][0]
                        crop_start_day = solution.data[field_index][index][1]
                        daily_resources_to_del = cultivation_types[crop_type]["daily_resources"]
                        period_resources_to_del = cultivation_types[crop_type]["entire_period_resources"]
                        solution.data[field_index].pop(index)
                        remove_resources_from_list(daily_resources_list, period_dict, crop_start_day, daily_resources_to_del,
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




