#!/usr/bin/env python

from utils.font_utils.trim_raw_fonts import TrimRawFonts

def main():
    font_path='/data/udel-ms-data-science/math-637/project-1/char-fonts/raw'
    test_font='junk.csv'

    trf = TrimRawFonts(f'{font_path}/{test_font}',debug=True)
    junk_df = trf.load_font_dataframe()
    print(f'Junk DataFrame {junk_df}')

if __name__ == '__main__':
    main()
