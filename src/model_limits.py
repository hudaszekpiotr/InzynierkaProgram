#!/usr/bin/python
# -*- coding: utf-8 -*-
import collections
import functools

from solution_classes import Solution
import pandas as pd
import operator


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
        for field in day.field:
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



def resources_df(solution, cultivation_types):
    df = pd.DataFrame()

    period_dict = {}
    for count, day in enumerate(solution.days):
        daily_dict = {}
        for field in day.field:
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

        df["day" + str(count)] = pd.Series(daily_dict, dtype='float64')

    return df, period_dict