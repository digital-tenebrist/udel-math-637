#!/usr/bin/env python

from collections import namedtuple

class FontDetailConfig():

    def __init__(self):
        self.nt = namedtuple('FontDetailNamedTuple',
                             [
                                 'font_name',
                                 'font_variant',
                                 'italic'
                             ]
        )
        self.list_of_details = [
            self.nt('ARIAL', 'scanned', 0),
            self.nt('ARIAL', 'ARIAL', 0),
            self.nt('ARIAL', 'ARIAL BLACK', 0),
            self.nt('BASKERVILLE', 'BASKERVILLE OLD FACE', 0),
            self.nt('BODONI', 'BODONI MT BLACK', 0),
            self.nt('BOOKMAN', 'BOOKMAN OLD STYLE', 0),
            self.nt('CALIBRI', 'CALIBRI', 0),
            self.nt('CENTURY', 'CENTURY SCHOOLBOOK', 0),
            self.nt('CONSOLAS', 'CONSOLAS', 0),
            self.nt('COURIER', 'COURIER NEW', 0),
            self.nt('COURIER', 'scanned', 0),
            self.nt('GARAMOND', 'GARAMOND', 0),
            self.nt('LUCIDA', 'LUCIDA CONSOLE', 0),
            self.nt('LUCIDA', 'LUCIDA SANS TYPEWRITER', 0),
            self.nt('LUCIDA', 'LUCIDA SANS', 0),
            self.nt('MODERN', 'MODERN NO. 20', 0),
            self.nt('ROCKWELL', 'ROCKWELL', 0),
            self.nt('ROMAN', 'ROMAND', 0),
            self.nt('ROMAN', 'ROMANT', 0),
            self.nt('TAHOMA', 'TAHOMA', 0),
            self.nt('TIMES', 'TIMES NEW ROMAN', 0)
        ]

    def get_font_detail_config(self):
        return self.list_of_details

    def get_detail_config_for_font(self,font):
        return [f for f in self.list_of_details if f.font_name == font]

    def get_detail_config_for_font_variant(self,variant):
        for fdc in self.list_of_details:
            if fdc.font_variant == variant:
                return fdc
