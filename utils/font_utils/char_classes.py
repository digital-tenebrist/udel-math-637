#!/usr/bin/env python3

class CharClass:

    def __init__(self):
        self._curved_class = 'cCGoOQ0689'
        self._straight_class = 'bBdDEFhHiIkKlLpPqrRtT1'
        self._mixed_class   = 'efgjJasS235'
        self._open_class    = 'uUvVwWAmMnNxXyYzZ47'

    def get_curved_class(self):
        return [ord(x) for x in self._curved_class]

    def get_straight_class(self):
        return [ord(x) for x in self._straight_class]

    def get_mixed_class(self):
        return [ord(x) for x in self._mixed_class]

    def get_open_clas(self):
        return [ord(x) for x in self._open_class]

    def get_color_map(self):
        color_map = dict()
        for c in self._curved_class:
            color_map[c] = 'red'
        for c in self._straight_class:
            color_map[c] = 'blue'
        for c in self._mixed_class:
            color_map[c] = 'green'
        for c in self._open_class:
            color_map[c] = 'orange'

        return color_map
