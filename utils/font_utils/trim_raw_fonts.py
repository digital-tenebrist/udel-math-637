#!/usr/bin/env python3

import numpy as np
import pandas as pd

from .upper_lower_numerals import UpperLowerNumerals
from .raw_font_record import RawFontRecord

class TrimRawFonts:

    def __init__(self,fname,debug=False):
        self.debug = debug
        self.fname = fname
        self.uln = UpperLowerNumerals.get_ascii_codes()
        self.image_cols = [f'r{r}c{c}' for r in range(20) for c in range(20)]
        self.char_col = 'char'

    def raw_font_as_list(self, rfr: RawFontRecord):
        '''
        Input is RawFontRecord item
        Output is array with string of character and 400 gray scale numerals
        Only output loaded array if input record is in a-zA-Z-0-9
        '''

        if self.debug:
            print(f'TrimRawFonts : str : {str(chr(rfr.ascii_label))}')

        if rfr.ascii_label in self.uln:
            return [chr(rfr.ascii_label), *[eval(f'{rfr}.{x}') for x in self.image_cols]]
        else:
            print('should not be here')
            return None


    def raw_font_as_df(self, rfr: RawFontRecord):
        '''
        Input is RawFontRecord item
        Output is pandas dataframe with column names [char,r0c0,...r19,c19]
        Only output loaded dataframe if input record is in a-zA-Z-0-9
        '''

        if rfr.ascii_label in self.uln:
            i = [chr(rfr.ascii_label)]
            d = [eval(f'{rfr}.{x}') for x in self.image_cols]
            c = self.image_cols
            # print(f'{len(d)} : Data {d}')
            # print(f'{len(c)} : Cols {c}')
            # return None
            return pd.DataFrame(data=[d],index=i,columns=c)
        else:
            print('should not be here')
            return None
