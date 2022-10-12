#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import List, Callable


class DaySolution:
    def __init__(self, num_fields):
        self.field = [None] * num_fields


class Solution:
    def __init__(self, num_fields: int, num_days: int):
        self.days = []
        self.num_fields = num_fields
        for _ in range(num_days):
            day = DaySolution(num_fields)
            self.days.append(day)

    def __str__(self):
        txt = ""
        for i, day in enumerate(self.days):
            txt += f"Day {i}\n"
            for field_num in range(self.num_fields):
                txt += f"field num: {field_num} cultivation type:{day.field[field_num]}\n\n"
        txt += "\n\n\n\n"
        return txt




