#!/usr/bin/env python

import string
import random

import pandas as pd
import numpy as np

from .upper_lower_numerals import UpperLowerNumerals as ULN

FONT_PATH='/data/udel-ms-data-science/math-637/project-1/char-fonts/raw'
FONT_EXTENSION='csv'
FONTS=['courier']
ROW_COLS=[f'r{r}c{c}' for r in range(20) for c in range(20)]
LABEL_COL='m_label'
KEEP_COLS=[LABEL_COL, *ROW_COLS]

class LoadFont:

    def __init__(self, font_name):
        self.fname = f'{FONT_PATH}/{font_name.lower()}.{FONT_EXTENSION}'
        self.raw_df = pd.read_csv(self.fname)
        self.min_char_count = 0
        self.pca_candidate = None

    def get_trimmed_font(self):
        cdf = self.raw_df
        letters_numbers = cdf.loc[
            (cdf['font'] == 'COURIER') &
            (
                ( (cdf['m_label'] > 96) & (cdf['m_label'] < 123) ) | # lower case a-z
                ( (cdf['m_label'] > 64) & (cdf['m_label'] < 91)  ) | # upper case A-Z
                ( (cdf['m_label'] > 47) & (cdf['m_label'] < 58)  )   # numerals 0-9
            ) &
            (cdf['fontVariant'] == 'scanned') &
            (cdf['italic'] == 0)
        ]

        less_cols = letters_numbers[KEEP_COLS]
        min_char_count = min(less_cols.m_label.value_counts())
        self.min_char_count = min_char_count

        to_flatten = [random.sample(less_cols.index[less_cols['m_label'] == c].tolist(), min_char_count) for c in ULN.get_ascii_codes()]
        flat_idx = [item for sublist in to_flatten for item in sublist]
        self.pca_candidate = less_cols[less_cols.index.isin(flat_idx)]

        return self.pca_candidate

    def get_char_count(self):
        return self.min_char_count
