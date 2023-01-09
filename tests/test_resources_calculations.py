from unittest.mock import patch

import pandas as pd
import pytest
from numpy import nan
from pandas import DataFrame

from src.resources_calculations import get_used_resources, penalty, resources_percent, resources_used_day_field, \
    remove_resources_from_list, fixup, resources_df
from src.solution_classes import Solution


@pytest.fixture
def solution():
    solution = Solution(num_fields=2, num_days=10)
    solution.data = [[(0, 0), (1, 5)], [(1, 1), (1, 5)]]
    return solution


@pytest.fixture
def cultivation_types():
    cultivation_types = [{"name": "type1",
                          "duration": 2,
                          "entire_period_resources": {
                              "money": 20,
                              "warehouse": 10
                          },
                          "daily_resources": [
                              {"work_hours": 5,
                               "water": 5,
                               "machine_1": 1},
                              {"work_hours": 5,
                               "machine_2": 1},
                          ]
                          },
                         {"name": "type2",
                          "duration": 2,
                          "entire_period_resources": {
                              "money": 3,
                              "warehouse": 3
                          },
                          "daily_resources": [
                              {"work_hours": 3,
                               "water": 3,
                               "machine_3": 3, },
                              {"work_hours": 3,
                               "machine_2": 3}
                          ]
                          }]
    return cultivation_types


@pytest.fixture
def fields():
    fields = [{"area": 10,
               "coefficients": {"type1": 1.5,
                                "type2": 1.5}},
              {"area": 5,
               "coefficients": {"type1": 1.0,
                                "type2": 2.0}}]
    return fields


def test_get_used_resources(solution, cultivation_types, fields):
    daily_resources_list, period_dict = get_used_resources(solution, cultivation_types, fields)

    assert daily_resources_list == [{'machine_1': 10, 'water': 50, 'work_hours': 50},
                                    {'machine_2': 10, 'machine_3': 15, 'water': 15, 'work_hours': 65},
                                    {'machine_2': 15, 'work_hours': 15},
                                    {},
                                    {},
                                    {'machine_3': 45, 'water': 45, 'work_hours': 45},
                                    {'machine_2': 45, 'work_hours': 45},
                                    {},
                                    {},
                                    {}]
    assert period_dict == {'money': 260, 'warehouse': 160}


def test_penalty_zero(mocker):
    daily_resources_list = [{"machine_1": 1}, {"machine_1": 1, "water": 10}]
    period_dict = {"money": 1,
                   "warehouse": 1}
    mocker.patch("src.resources_calculations.get_used_resources", return_value=(daily_resources_list, period_dict))
    multiplier = 2
    resources = {
        "daily_resources": {
            "machine_1": 1,
            "water": 10,
        },
        "entire_period_resources": {
            "money": 1,
            "warehouse": 1
        }
    }

    penalty_val = penalty(None, None, resources, multiplier, None)
    assert penalty_val == 0


def test_penalty_greater_than_zero(mocker):
    daily_resources_list = [{"machine_1": 2, "water": 15}, {"machine_1": 1}]
    period_dict = {"money": 2,
                   "warehouse": 1}
    mocker.patch("src.resources_calculations.get_used_resources", return_value=(daily_resources_list, period_dict))
    multiplier = 2
    resources = {
        "daily_resources": {
            "machine_1": 1,
            "water": 10,
        },
        "entire_period_resources": {
            "money": 1,
            "warehouse": 1
        }
    }

    penalty_val = penalty(None, None, resources, multiplier, None)
    assert penalty_val == 500


def test_resources_df(mocker):
    daily_resources_list = [{"machine_1": 2, "water": 15}, {"machine_1": 1}]
    period_dict = {"money": 2,
                   "warehouse": 1}
    mocker.patch("src.resources_calculations.get_used_resources", return_value=(daily_resources_list, period_dict))

    df, period_df = resources_df(None, None, None)

    pd.testing.assert_frame_equal(df, DataFrame({1: [2.0, 15.0], 2: [1.0, nan]}, index=['machine_1', 'water']))


def test_resources_used_day_field_zero_used(solution, cultivation_types):
    field = 1
    day = 3

    resources_crop, index = resources_used_day_field(solution, field, day, cultivation_types)

    assert resources_crop is None
    assert index is None


def test_resources_used_day_field(solution, cultivation_types):
    field = 1
    day = 5

    resources_crop, index = resources_used_day_field(solution, field, day, cultivation_types)

    assert resources_crop == ['work_hours', 'water', 'machine_3']
    assert index == 1


def test_remove_resources_from_list():
    daily_resources_list = [{"machine_1": 2, "machine_2": 2}, {"machine_1": 2, "machine_2": 2},
                            {"machine_1": 4, "machine_2": 4}]
    period_dict = {"work_hours": 10, "water": 5}
    day = 1
    daily_resources_to_del = [{"machine_1": 2, "machine_2": 2}, {"machine_1": 2, "machine_2": 2}]
    period_resources_to_del = {"work_hours": 8}

    remove_resources_from_list(daily_resources_list, period_dict, day, daily_resources_to_del, period_resources_to_del)

    assert daily_resources_list == [{"machine_1": 2, "machine_2": 2}, {"machine_1": 0, "machine_2": 0},
                                    {"machine_1": 2, "machine_2": 2}]
    assert period_dict == {"work_hours": 2, "water": 5}


def test_fixup_no_fixup_needed(solution, cultivation_types, fields):
    resources = {
        "daily_resources": {
            "machine_1": 10,
            "water": 50,
            "work_hours": 65,
            "machine_2": 45,
            "machine_3": 45
        },
        "entire_period_resources": {
            "money": 260,
            "warehouse": 160
        }
    }
    fixup(solution, cultivation_types, resources, fields)

    assert solution.data == [[(0, 0), (1, 5)], [(1, 1), (1, 5)]]


def test_fixup_fixup_needed(solution, cultivation_types, fields):
    resources = {
        "daily_resources": {
            "machine_1": 0,
            "water": 50,
            "work_hours": 65,
            "machine_2": 45,
            "machine_3": 45
        },
        "entire_period_resources": {
            "money": 260,
            "warehouse": 160
        }
    }
    fixup(solution, cultivation_types, resources, fields)
    daily_resources_list, period_dict = get_used_resources(solution, cultivation_types, fields)
    print(daily_resources_list, period_dict)
    assert solution.data == [[(1, 5)], [(1, 1), (1, 5)]]
