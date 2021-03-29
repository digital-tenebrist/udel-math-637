#!/usr/bin/env python3

from .upper_lower_numerals import UpperLowerNumerals
from .raw_font_record import RawFontRecord

class TrimRawFonts:

    def __init__(self,fname):
        self.fname = fname
        self.uln = UpperLowerNumerals.get_ascii_codes()
        self.image_cols = [f'r{r}c{c}' for r in range(20) for c in range(20)]

    def trim_raw_font(self, rfr: RawFontRecord):
        '''
        Input is RawFontRecord item
        Output is array with string of character and 400 gray scale numerals
        Only output loaded array if input record is in a-zA-Z-0-9
        '''

        #print(f'here : {rfr.ascii_label}')
        #print(f'ascii codes : {self.uln}')
        #print(f'type of ascii_label : {type(rfr.ascii_label)}')
        #print(f'type of uln         : {type(self.uln[0])}')

        if rfr.ascii_label in self.uln:
            o_list=[chr(rfr.ascii_label), *[eval(f'{rfr}.{x}') for x in self.image_cols]]
            #o_list.extend([eval(f'{rfr}.{x}') for x in self.image_cols])
            #o_list.append(chr(rfr.ascii_label))
            #o_list.extend([eval(f'{rfr}.{x}') for x in self.image_cols])
            #print(f'here: {o_list}')
            return o_list
        else:
            print('should not be here')
            return None
