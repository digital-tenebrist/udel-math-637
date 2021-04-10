#!/usr/bin/env python

from utils.font_utils.font_details import FontDetails

FONT_LIST = [
    'arial',
    'baskerville',
    'bodoni',
    'bookman',
    'calibri',
    'century',
    'consolas',
    'courier',
    'garamond',
    'lucida',
    'modern',
    'monotype',
    'rockwell',
    'roman',
    'sansserif',
    'tahoma',
    'times'
]

def main():
    for f in FONT_LIST:
        fd = FontDetails(f)
        fd.print_font_details()
        print('')

if __name__ == '__main__':
    main()
