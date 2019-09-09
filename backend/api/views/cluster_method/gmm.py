# 1.1 data analysis and wrangling
import numpy as np
import pandas as pd
# 1.2정규분포
from scipy.stats import norm
import scipy as sp

from sklearn.mixture import GaussianMixture

import warnings
from sklearn.exceptions import ConvergenceWarning
warnings.filterwarnings(action='ignore', category=ConvergenceWarning)

class GaussianMix:
    def __init__(self, ratings, movies, base, N):
        genres = [
            "Action", "Adventure", "Animation", "Children's", "Comedy", "Crime", "Documentary", "Drama", "Fantasy",
            "Film-Noir", "Horror", "Musical", "Mystery", "Romance", "Sci-Fi", "Thriller", "War", "Western"
        ]
        genreNum = [
            "200", "201", "202", "203", "204", "205", "206", "207", "208", "209",
            "210", "211", "212", "213", "214", "215", "216", "217"
        ]
        movies = pd.DataFrame.from_records(movies)
        ratings = pd.DataFrame(ratings)
        data = pd.merge(ratings, movies, left_on='movie_id', right_on='id')
        result = dict()

        for genre in genres:
            gmmData = self.get_gmm_data(ratings, data, genre, base)
            clusterData = self.make_gmm(gmmData, N)
            for i in clusterData:
                try:
                    if result[i[0]][1][1] < i[2]:
                        result[i[0]] = [genre, i[1:]]
                except:
                    result[i[0]] = [genre, i[1:]]

        for i in result:
            for j in range(len(genres)):
                if result[i][0] == genres[j]:
                    result.update({i: str(genreNum[j]) + str(result[i][1][0])})
        self.result = {k:int(v) for k,v in result.items()}
        return

    def get_result(self):
        return self.result

    def get_gmm_data(self, ratings, data, genre, base):
        if base == 'item':
            data = data.sort_values(["movie_id"])
        rateData = self.get_user_ratings(ratings, data, genre, base)
        return self.get_gmm_sort(rateData, base)

    def get_user_ratings(self, ratings, movies, genre, base):
        genre_ratings = pd.DataFrame()
        genre_movies = movies[movies['genres'].str.contains(genre)]
        if base != 'item':
            genre_ratings = pd.concat([genre_ratings, genre_movies['user_id'], genre_movies['rating']], axis=1)
        else:
            genre_ratings = pd.concat([genre_ratings, genre_movies['movie_id'], genre_movies['rating']], axis=1)
        return genre_ratings

    def get_gmm_sort(self, data, base):
        b = []
        if base != 'item':
            scope = sorted(set(data.user_id))
        else:
            scope = sorted(set(data.movie_id))
        for i in scope:
            if base != 'item':
                diX = data.loc[data.user_id == i].values.tolist()
            else:
                diX = data.loc[data.movie_id == i].values.tolist()
            a = []
            for j in diX:
                a.append(j[1])
            b.append([i, sum(a)/len(a), np.std(a)])
        b = np.array(b)
        return b

    def make_gmm(self, data, N):
        if len(data) < N:
            return []
        em = GaussianMixture(n_components=N, max_iter=100, random_state=0)
        y_pred = em.fit_predict(data[:, 1:])
        
        xy_pred=[]
        a = data[:, 1:2]
        a.tolist()

        x_pred = (data[:, :1])
        for i in range(len(x_pred)):
            xy_pred.append([int(x_pred.tolist()[i][0]),y_pred[i], round(*a[i], 2)])
        return xy_pred