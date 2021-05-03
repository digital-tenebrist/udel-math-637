#!/usr/bin/env python3

from sklearn.cluster import KMeans
from sklearn.cluster import SpectralClustering
from sklearn.neighbors import kneighbors_graph
from sklearn.cluster import AgglomerativeClustering

class ClusterUtils:

    def __init__(self):
        self._methods = ['kmeans', 'spectral', 'agglomerative']
        self._nclusters = 4
        self._agg_neighbors = 4

    def perform_clustering(self, method, raw_df, debug=False):
        '''
        Returns label array based on input of method
        method:
            kmeans
            spectral
            agglomerative
        '''

        if method not in self._methods:
            print(f'Invalid method {method} - expected values {methods}')
            return None

        if method == 'kmeans':
            kmeans = KMeans(n_clusters=self._nclusters, random_state=0).fit(raw_df)
            if debug:
                print(f'Labels  : {kmeans.labels_}')
                for i in range(self._nclusters):
                    print(f'Occurences of {i} in labels {np.count_nonzero(kmeans.labels_ == i)}')
                print(f'Centers : {kmeans.cluster_centers_}')

            return {'labels' : kmeans.labels_, 'centers': kmeans.cluster_centers_}

        if method == 'spectral':
            spectral = SpectralClustering(self._nclusters, eigen_solver='arpack',affinity="nearest_neighbors")
            spectral.fit(raw_df)
            if debug:
                print(f'Labels : {spectral.labels_}')
                for i in range(self._nclusters):
                    print(f'Occurences of {i} in labels {np.count_nonzero(spectral.labels_ == i)}')

            return {'labels': spectral.labels_, 'centers': None}

        if method == 'agglomerative':
            connectivity = kneighbors_graph(raw_df, n_neighbors=self._agg_neighbors, include_self=False)
            # make connectivity symmetric
            connectivity = 0.5 * (connectivity + connectivity.T)
            aggcluster = AgglomerativeClustering(
                linkage="ward",
                affinity="euclidean",
                n_clusters=self._nclusters,
                connectivity=connectivity
            )

            aggcluster.fit(raw_df)
            if debug:
                print(f'Labels : {aggcluster.labels_}')
                for i in range(self._nclusters):
                    print(f'Occurences of {i} in labels {np.count_nonzero(aggcluster.labels_ == i)}')

            return {'labels': aggcluster.labels_, 'centers': None}
