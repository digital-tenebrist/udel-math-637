#!/usr/bin/env python

import string
import random

import pandas as pd
import numpy as np

from .upper_lower_numerals import UpperLowerNumerals as ULN
from .font_detail_cfg import FontDetailConfig as FDC

FONT_PATH='/data/udel-ms-data-science/math-637/project-1/char-fonts/raw'
FONT_EXTENSION='csv'
ROW_COLS=[f'r{r}c{c}' for r in range(20) for c in range(20)]
LABEL_COL='m_label'
KEEP_COLS=[LABEL_COL, *ROW_COLS]

class LoadFont:

    def __init__(self, font_name):
        self.fname = f'{FONT_PATH}/{font_name.lower()}.{FONT_EXTENSION}'
        self.raw_df = pd.read_csv(self.fname)
        self.variant_dict = dict()

        fdc = FDC()
        self.fdc = fdc.get_detail_config_for_font(font_name.upper())

    def get_trimmed_font(self):
        cdf = self.raw_df
        for fdc in self.fdc:
            cur_variant = dict()
            letters_numbers = cdf.loc[
                (cdf['font'] == fdc.font_name) &
                (
                    ( (cdf['m_label'] > 96) & (cdf['m_label'] < 123) ) | # lower case a-z
                    ( (cdf['m_label'] > 64) & (cdf['m_label'] < 91)  ) | # upper case A-Z
                    ( (cdf['m_label'] > 47) & (cdf['m_label'] < 58)  )   # numerals 0-9
                ) &
                (cdf['fontVariant'] == fdc.font_variant) &
                (cdf['italic'] == fdc.italic)
            ]

            less_cols = letters_numbers[KEEP_COLS]
            min_char_count = min(less_cols.m_label.value_counts())
            to_flatten = [random.sample(less_cols.index[less_cols['m_label'] == c].tolist(), min_char_count) for c in ULN.get_ascii_codes()]
            flat_idx = [item for sublist in to_flatten for item in sublist]

            cur_variant['df'] = less_cols[less_cols.index.isin(flat_idx)]
            cur_variant['min_char_count'] = min_char_count

            self.variant_dict[fdc.font_variant] = cur_variant

        return self.variant_dict
