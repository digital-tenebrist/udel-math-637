#!/usr/bin/env python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.decomposition import PCA
from sklearn.manifold import Isomap
from sklearn.manifold import TSNE

from font_utils import char_classes as CHAR_CLASS

class PlotUtils:

    @staticmethod
    def plot_pca(raw, plot_title):
        np.set_printoptions(precision=4,floatmode='fixed')

        label_ar = [chr(x) for x in raw.m_label]

        df=raw.drop(columns=['m_label'])
        df=df-df.mean(axis=0)

        pca = PCA(n_components=20)
        pca.fit(df)

        print(f'Len of eigenvector {len(pca.components_[0])}')
        #print(f'First eigenvector')
        #print(f'{pca.components_[0]}')

        #print(f'First eigenvalue          : {pca.singular_values_[0]:0.4f}')
        print(f'Explained Variance Ratio  : {pca.explained_variance_ratio_[0]:0.4f}')
        print(f'Sum of explained variance : {sum(pca.explained_variance_ratio_)}')

        np.set_printoptions()

        x=df.dot(pca.components_[0])
        y=df.dot(pca.components_[1])

        print(f'Len label_ar {len(label_ar)}')
        print(f'Len x {len(x)}')
        print(f'Len y {len(y)}')

        plot_df = pd.DataFrame([np.array(label_ar).transpose(), x.transpose(), y.transpose()]).transpose()
        plot_df.columns=['m_label', 'x', 'y']

        char_class = CHAR_CLASS.CharClass()
        color_dict = char_class.get_color_map()
        class_dict = char_class.get_char_class_name()
        plot_df['color'] = plot_df['m_label'].apply(lambda x: color_dict[x])
        plot_df['class'] = plot_df['m_label'].apply(lambda x: class_dict[x])

        plt.title(plot_title)
        plt.xlabel("Eigen 0")
        plt.ylabel("Eigen 1")
        plt.grid()

        plt.scatter(plot_df.x,plot_df.y, c=plot_df.color)

        # Larger Labeled Plot
        plt.figure(figsize=(15,15))
        sns.scatterplot(
            data=plot_df,
            x='x',
            y='y',
            hue='class',
            style='class',
            palette=['green', 'blue', 'red', 'orange']
        )

        for i in range(plot_df.shape[0]):
            plt.text(
                x=plot_df.x[i]+20,
                y=plot_df.y[i]+20,
                s=plot_df.m_label[i]#,
                #     fontdict=dict(color='red',size=10),
                #     bbox=dict(facecolor='yellow',alpha=0.5)
            )

        plt.title(plot_title)
        plt.xlabel('Eigen 0')
        plt.ylabel('Eigen 1')
        plt.grid()
        plt.show()

    @staticmethod
    def plot_isomap(raw, plot_title):
        neighbors=8
        components=2

        np.set_printoptions(precision=4,floatmode='fixed')

        label_ar = [chr(x) for x in raw.m_label]

        df=raw.drop(columns=['m_label'])
        df=df-df.mean(axis=0)

        isomap = Isomap(n_neighbors=neighbors,n_components=components)
        y = isomap.fit_transform(df)

        y_df = pd.DataFrame([np.array(label_ar), y[:,0], y[:,1]]).transpose()
        y_df.columns=['m_label', 'x', 'y']

        char_class = CHAR_CLASS.CharClass()
        color_dict = char_class.get_color_map()
        class_dict = char_class.get_char_class_name()
        y_df['color'] = y_df['m_label'].apply(lambda x: color_dict[x])
        y_df['class'] = y_df['m_label'].apply(lambda x: class_dict[x])

        plt.title(plot_title)
        plt.xlabel("Dim 0")
        plt.ylabel("Dim 1")
        plt.grid()

        plt.scatter(y_df.x,y_df.y, c=y_df.color)

        # Larger Labeled Plot
        plt.figure(figsize=(15,15))
        sns.scatterplot(
            data=y_df,
            x='x',
            y='y',
            hue='class',
            style='class',
            palette=['green', 'blue', 'red', 'orange']
        )

        for i in range(y_df.shape[0]):
            plt.text(
                x=y_df.x[i]+20,
                y=y_df.y[i]+20,
                s=y_df.m_label[i]#,
                #     fontdict=dict(color='red',size=10),
                #     bbox=dict(facecolor='yellow',alpha=0.5)
            )

        plt.title(plot_title)
        plt.xlabel('Dim 0')
        plt.ylabel('Dim 1')
        plt.grid()
        plt.show()

    @staticmethod
    def plot_tsne(raw, plot_title):
        components=2
        initializer='pca'
        rs=0

        np.set_printoptions(precision=4,floatmode='fixed')

        label_ar = [chr(x) for x in raw.m_label]

        df=raw.drop(columns=['m_label'])
        df=df-df.mean(axis=0)

        tsne = TSNE(n_components=components,init=initializer,random_state=rs)
        y = tsne.fit_transform(df)

        y_df = pd.DataFrame([np.array(label_ar), y[:,0], y[:,1]]).transpose()
        y_df.columns=['m_label', 'x', 'y']

        char_class = CHAR_CLASS.CharClass()
        color_dict = char_class.get_color_map()
        class_dict = char_class.get_char_class_name()
        y_df['color'] = y_df['m_label'].apply(lambda x: color_dict[x])
        y_df['class'] = y_df['m_label'].apply(lambda x: class_dict[x])

        plt.title(plot_title)
        plt.xlabel("Dim 0")
        plt.ylabel("Dim 1")
        plt.grid()

        plt.scatter(y_df.x,y_df.y, c=y_df.color)

        # Larger Labeled Plot
        plt.figure(figsize=(15,15))
        sns.scatterplot(
            data=y_df,
            x='x',
            y='y',
            hue='class',
            style='class',
            palette=['green', 'blue', 'red', 'orange']
        )

        for i in range(y_df.shape[0]):
            plt.text(
                x=y_df.x[i]+20,
                y=y_df.y[i]+20,
                s=y_df.m_label[i]#,
                #     fontdict=dict(color='red',size=10),
                #     bbox=dict(facecolor='yellow',alpha=0.5)
            )

        plt.title(plot_title)
        plt.xlabel('Dim 0')
        plt.ylabel('Dim 1')
        plt.grid()
        plt.show()
