#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import List, Callable

import numpy as np
import pandas as pd



class Solution:
    def __init__(self, num_fields: int, num_days: int):
        self.matrix = np.full((num_fields, num_days), None, dtype=object)
        self.num_days = num_days
        self.num_fields = num_fields

    def __str__(self):
        txt = str(self.matrix)
        return txt

    def to_dataframe(self):
        # #df = pd.DataFrame()
        #
        # values = {}
        # for day in range(self.num_days):
        #     col_name = "day" + str(day)
        #     values[col_name] = self.days[day].fields

        #df = pd.DataFrame(data=values)
        df = pd.DataFrame(data=self.matrix)
        # for day in range(self.num_days):
        #     col_name = "day"+ str(day)
        #     df[col_name] = self.days[day].fields
        pd.set_option("display.max_rows", 500)
        pd.set_option("display.max_columns", 30)
        pd.set_option("display.width", 1000)
        return df

    def to_simple_dataframe(self):
        def reduct(series):
            def remove_tuples(elem):
                if type(elem) is tuple:
                    return str((elem[0])+ 1)
                return " "
            return series.apply(remove_tuples)
        df = self.to_dataframe()
        df = df.apply(reduct)
        return df



class SolutionAndFitness:
    def __init__(self, solution: Solution, fitness: int):
        self.solution = solution
        self.fitness = fitness

    def __str__(self):
        return self.solution.__str__() + str(self.fitness)
