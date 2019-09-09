import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering

class Hierarchical:
    def __init__(self, movie, rating, target):
        movies = pd.DataFrame.from_records(movie)
        ratings = pd.DataFrame(rating)
        self.target = target
        self.data = pd.merge(ratings, movies, left_on='movie_id', right_on='id')
        self.pivotTable = pd.pivot_table(self.data, index='user_id', columns= 'movie_id', values='rating')
        self.pivotTable.replace(np.nan, 0, inplace=True)

        if self.target == 'movie':
            self.pivotTable = self.pivotTable.T
        self.pivotTable['labels'] = 0
    
    def cluster(self, n):
        cluster = AgglomerativeClustering(n_clusters=n, affinity='euclidean', linkage='ward')  
        result = cluster.fit_predict(self.pivotTable)
        ans = {}
        for i in range(len(result)):
            ans[self.pivotTable.index[i]] = result[i]
        return ans
