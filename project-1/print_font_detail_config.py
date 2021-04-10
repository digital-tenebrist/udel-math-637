#!/usr/bin/env python3

from utils.font_utils.font_detail_cfg import FontDetailConfig


def main():
    fdc = FontDetailConfig()
    lod = fdc.get_font_detail_config()
    for f in lod:
        print(','.join([f.font_name, f.font_variant, str(f.italic)]))


    lucida_fonts = fdc.get_detail_config_for_font('LUCIDA')
    for f in lucida_fonts:
        print(','.join([f.font_name, f.font_variant, str(f.italic)]))

    century_schoolbook = fdc.get_detail_config_for_font_variant('CENTURY SCHOOLBOOK')
    print(','.join([century_schoolbook.font_name, century_schoolbook.font_variant, str(century_schoolbook.italic)]))

if __name__ == '__main__':
    main()
