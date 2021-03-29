#!/usr/bin/env python

from csv import DictReader
from utils.font_utils.raw_font_record import RawFontRecord
from utils.font_utils.upper_lower_numerals import UpperLowerNumerals
from utils.font_utils.trim_raw_fonts import TrimRawFonts

def main():
    font_path='/data/udel-ms-data-science/math-637/project-1/char-fonts/raw'
    test_font='junk.csv'

    trf = TrimRawFonts(f'{font_path}/../trimmed/{test_font}')

    #print(f'{UpperLowerNumerals.get_ascii_codes()}')
    #print(f'{[chr(x) for x in UpperLowerNumerals.get_ascii_codes()]}')

    with open(f'{font_path}/{test_font}', 'r') as font_csv:
        reader = DictReader(font_csv)
        for font_char in reader:
            rfr = RawFontRecord(*[v for k,v in font_char.items()])
            #print(f'{chr(int(rfr.ascii_label))}')
            trimmed = trf.trim_raw_font(rfr)
            if trimmed:
                print(','.join([str(x) for x in trimmed]))


if __name__ == '__main__':
    main()
