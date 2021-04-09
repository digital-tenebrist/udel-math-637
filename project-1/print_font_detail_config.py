#!/usr/bin/env python3

from utils.font_utils.font_detail_cfg import FontDetailConfig


def main():
    fdc = FontDetailConfig()
    lod = fdc.get_font_detail_config()
    for f in lod:
        print(','.join([f.font_name, f.font_variant, str(f.italic)]))

if __name__ == '__main__':
    main()
