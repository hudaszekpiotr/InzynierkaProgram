#!/usr/bin/python
# -*- coding: utf-8 -*-




import pandas as pd


class Solution:
    def __init__(self, num_fields: int, num_days: int):
        self.data = [[] for i in range(num_fields)]
        self.num_days = num_days
        self.num_fields = num_fields

    def to_dataframe(self, cultivation_types):
        matrix = [['' for i in range(self.num_days)] for k in range(self.num_fields)]
        #matrix = np.full((self.num_fields, self.num_days), "", dtype=object)
        for field_index, field in enumerate(self.data):
            for crop in field:
                duration = cultivation_types[crop[0]]["duration"]
                matrix[field_index][crop[1] : crop[1] + duration] = [str(crop[0])] * duration
                #matrix[field_index, crop[1]:crop[1] + duration] = str(crop[0])

        df = pd.DataFrame(data=matrix)
        pd.set_option("display.max_rows", 500)
        pd.set_option("display.max_columns", 30)
        pd.set_option("display.width", 1000)
        return df


class SolutionAndFitness:
    def __init__(self, solution: Solution, fitness: int):
        self.solution = solution
        self.fitness = fitness

    def __str__(self):
        return self.solution.__str__() + str(self.fitness)
