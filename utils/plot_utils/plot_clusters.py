#!/usr/bin/env python3

from collections import namedtuple

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

PlotCfg = namedtuple('PlotCfg', ['cluster','color', 'name'])
PLOT_CFG = [
    PlotCfg(0,'red','Class 0'),
    PlotCfg(1, 'blue', 'Class 1'),
    PlotCfg(2, 'green', 'Class 2'),
    PlotCfg(3, 'orange', 'Class 3')
]

class PlotClusters:

    def __init__(self, labels):
        self.label_ar = labels


    def _make_plot_df(self, raw_df, labels):
        df = pd.DataFrame(
            [
                np.array(labels).transpose(),
                np.array(self.label_ar).transpose(),
                raw_df.x.transpose(),
                raw_df.y.transpose()
            ]
        ).transpose()

        df.columns=['c_label', 'm_label', 'x', 'y']

        df['color'] = df['c_label'].apply(lambda x: PLOT_CFG[int(x)].color)
        df['class'] = df['c_label'].apply(lambda x: PLOT_CFG[int(x)].name)

        return df

    def small_plot(self, raw_df, labels, title):

        plot_df = self._make_plot_df(raw_df, labels)

        plt.title(title)
        plt.xlabel("Eigen 0")
        plt.ylabel("Eigen 1")
        plt.grid()

        plt.scatter(plot_df.x,plot_df.y, c=plot_df.color)

    def large_plot(self, raw_df, labels, title, centroids=None):

        d_cp = dict()
        for cfg in PLOT_CFG:
            d_cp[cfg.name] = cfg.color

        plot_df = self._make_plot_df(raw_df, labels)


        # Larger Labeled Plot
        fig = plt.figure(figsize=(15,15))
        sns.scatterplot(
            data=plot_df,
            x='x',
            y='y',
            hue='class',  # chance to class to debug large plot color mapping
            style='class',
            palette=d_cp
        )

        for i in range(raw_df.shape[0]):
            plt.text(
                x=plot_df.x[i]+20,
                y=plot_df.y[i]+20,
                s=plot_df.m_label[i]
            )

        if centroids is not None:
            # Show centroids of each cluster
            plt.scatter(centroids[:,0], centroids[:,1], s=30, color='black')
            for i in range(len(centroids)):
                plt.text(
                    x=centroids[i,0]+20,
                    y=centroids[i,1]+20,
                    s=f'c{i}'
                )

        plt.title(title)
        plt.xlabel('Dim 0')
        plt.ylabel('Dim 1')
        plt.grid()
        plt.show()

        pdf_filename = f'{title.replace(" ", "_")}.pdf'
        fig.savefig(pdf_filename, bbox_inches='tight')
