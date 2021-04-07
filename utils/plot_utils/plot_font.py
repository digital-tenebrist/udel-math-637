#!/usr/bin/env python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class PlotUtils:

    def __init__(self, char_list):
        self.char = char_list[0]
        self.ar   = np.array(char_list[1:], dtype=np.uint8).reshape(20,20)

    def show_plot(self):
        plt.imshow(self.ar,interpolation='nearest')
        plt.show()
