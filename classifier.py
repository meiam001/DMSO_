import tensorflow
# import rdkit
from data_parse import dmso
# import os
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np


class ya_boi:

    def __init__(self, x):
        self.data = x.data
        self.kmeans = None

    def create_clusters(self):
        self.kmeans = KMeans(n_clusters=3,)#verbose=-1)
        self.kmeans.fit(np.array(list(self.data['fingerprints']), dtype='int32'))
        self.data['cluster'] = self.kmeans.labels_

