#!/usr/bin/env python

import string
import random

import pandas as pd
import numpy as np

from .upper_lower_numerals import UpperLowerNumerals as ULN

FONT_PATH='/data/udel-ms-data-science/math-637/project-1/char-fonts/raw'
FONT_EXTENSION='csv'
DETAIL_COLS=['font', 'fontVariant', 'italic']

class FontDetails:

    def __init__(self, font_name):
        self.fname = f'{FONT_PATH}/{font_name.lower()}.{FONT_EXTENSION}'
        self.raw_df = pd.read_csv(self.fname)

    def print_font_details(self):
        for col in DETAIL_COLS:
            vc = f'self.raw_df.{col}.value_counts()'
            res = eval(vc)
            print(f'Detail {col} : ')
            for i,v in res.items():
                print(f'  {i} : {v}')
            # for r in res:
                # print(f'  {r}')
            #print(eval(vc))

    def print_font_variant(self):
        for col in ['fontVariant']:
            vc = f'self.raw_df.{col}.value_counts()'
            res = eval(vc)
            for i,v in res.items():
                print(f'    {i} : {v}')
