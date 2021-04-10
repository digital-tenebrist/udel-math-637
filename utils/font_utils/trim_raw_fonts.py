#!/usr/bin/env python3

import pandas as pd

from csv import DictReader

from .upper_lower_numerals import UpperLowerNumerals
from .raw_font_record import RawFontRecord

class TrimRawFonts:

    def __init__(self,fname,debug=False):
        self.debug = debug
        self.fname = fname
        self.uln = UpperLowerNumerals.get_ascii_codes()
        self.image_cols = [f'r{r}c{c}' for r in range(20) for c in range(20)]
        self.char_col = 'char'

    def load_font_dataframe(self):
        '''
        No inputs
        Returns data frame with 401 columns with character lable in column: char
        '''
        raw_font_list = None
        with open(self.fname, "r") as fh:
            reader = DictReader(fh)
            raw_font_list = [RawFontRecord(*[v for k,v in fc.items()]) for fc in reader]

        trimmed = [[eval(f'{r}.{x}') for x in self.image_cols] for r in raw_font_list if r.ascii_label in self.uln]
        indices = [r.ascii_label for r in raw_font_list if r.ascii_label in self.uln]

        return pd.DataFrame(data=trimmed,index=indices,columns=self.image_cols)
