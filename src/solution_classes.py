#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import List, Callable
import pandas as pd


class DaySolution:
    def __init__(self, num_fields):
        self.field = [None] * num_fields


class Solution:
    def __init__(self, num_fields: int, num_days: int):
        self.days = []
        self.num_days = num_days
        self.num_fields = num_fields
        for _ in range(num_days):
            day = DaySolution(num_fields)
            self.days.append(day)

    def __str__(self):
        txt = ""
        for i, day in enumerate(self.days):
            txt += f"Day {i}\n"
            for field_num in range(self.num_fields):
                txt += f"field: {field_num} crop:{day.field[field_num]}\n"
        txt += "\n\n"
        return txt

    def to_dataframe(self):
        df = pd.DataFrame()
        for day in range(self.num_days):
            col_name = "day"+ str(day)
            df[col_name] = self.days[day].field
        pd.set_option("display.max_rows", 500)
        pd.set_option("display.max_columns", 30)
        pd.set_option("display.width", 1000)
        return str(df) + "\n"

class SolutionAndFitness:
    def __init__(self, solution: Solution, fitness: int):
        self.solution = solution
        self.fitness = fitness

    def __str__(self):
        return self.solution.__str__() + str(self.fitness)
