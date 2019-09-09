import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.cluster import KMeans 

class kmeans:
    def __init__(self, k , input):
        self.k = k
        self.df = input
        self.C =None

    # K개의 중심값을 임의로 선택한다

    def centroids(self):
        import random
        C = {
        i+1:[data for data in self.df.values[i]]
        for i, j in zip(range(self.k), random.sample(range(len(self.df)),self.k))}
        return C

    # 각 중심에서 데이터까지의 거리를 계산 using up.linalg.norm
    # 각 데이터에 가장 가까운 중심점(군집)을 할당
        
    def classify(self,C):
        import copy
        cluster_df = copy.deepcopy(self.df)
        col_n = cluster_df.shape[1]
        for i in C.keys():
            cluster_df["Distance_from_{}".format(i)]\
            =np.linalg.norm(np.array(cluster_df)[:,:col_n]-C[i], axis=1)

        dist_cols=["Distance_from_{}".format(i)  for i in C.keys()]
        cluster_df["Closet_Cluster"] = cluster_df.loc[:,dist_cols].idxmin(axis=1).map(lambda x:int(x.lstrip("Distance_from")))
        return cluster_df

    #각 중심점에 선택된 데이터 포인터들의 평균위치로 중심점을 재이동
    def update(self, C):
        c_df = self.classify(C)
        self.C ={
        i:[c for c in np.mean(self.df[c_df["Closet_Cluster"]==i], axis=0)]
        for i in c_df["Closet_Cluster"].unique()}
        return self.C

    # 위 과정을 '갱신된 중심점이 거의 변화가 없어 할당된 군집이 바뀌지 않을만큼 반복

    def train_cluster(self):
        assignments = None
        C = self.centroids()
        while True:
            # 중심점에 해당하는 군집 찾기
            cluster_df = self.classify(C)
            new_assignments = list(self.classify(C)["Closet_Cluster"])
            # 새로운 중심점 찾기
            new_C = self.update(C)
            # 할당된 군집이 바뀌지 않을만큼 중심점이 수렴했다면 종료
            if assignments == new_assignments:
                break
            # 아니라면 다시 중심점과 군집 찾기
            assignments = new_assignments
            C = new_C

        return new_C, list(new_assignments), cluster_df

def count_word(df, ref_col, liste):
    keyword_count = dict()
    for s in liste: keyword_count[s] = 0
    for liste_keywords in df[ref_col].str.split('|'):
        if type(liste_keywords) == float and pd.isnull(liste_keywords): continue
        for s in liste_keywords: 
            if pd.notnull(s): keyword_count[s] += 1
    # convert the dictionary in a list to sort the keywords  by frequency
    keyword_occurences = []
    for k,v in keyword_count.items():
        keyword_occurences.append([k,v])
    keyword_occurences.sort(key = lambda x:x[1], reverse = True)
    return keyword_occurences, keyword_count

def get_movie(movies):
    movies_genre_indexing = pd.DataFrame()
    genre_ratings = pd.concat([movies_genre_indexing, movies['movie_id'], movies['title']], axis=1)
    return movies_genre_indexing

def df_kmeans_movie(movies):
    genre_labels = set()
    for s in movies['genres'].str.split('|').values:
        genre_labels = genre_labels.union(set(s))

    keyword_occurences, dum = count_word(movies, 'genres', genre_labels)

    movies_genre = movies
    for (key,cnt) in keyword_occurences:
        movies_genre.loc[movies_genre['genres'].str.contains(key), key] = 1
        movies_genre[key] = movies_genre[key].fillna(0)

    movies_genre = movies_genre.drop(columns=['genres'])

    movies_genre_2 = pd.DataFrame(movies_genre, columns = list(genre_labels))

    return movies_genre_2
    # predictions = kmeans(n, movies_genre_2.fillna(0))
    # cluster = predictions.train_cluster()
    # predictions_n = np.array(cluster[2]['Closet_Cluster'])
    # return predictions_n


def df_kmeans_user(data):
    user_movie_ratings = pd.pivot_table(data, index='user_id', columns= 'title', values='rating')
    user_movie_ratings = user_movie_ratings.fillna(0)
    sparse_ratings = csr_matrix(pd.SparseDataFrame(user_movie_ratings).to_coo())
    return user_movie_ratings, sparse_ratings


def kmeans_user(params, movies, ratings):
    movies = pd.DataFrame.from_records(movies)
    ratings = pd.DataFrame(ratings)
    data = pd.merge(ratings, movies, left_on='movie_id', right_on='id')

    user_movie_ratings, sparse_ratings = df_kmeans_user(data)

    # library
    # predictions_l =[]
    # predictions_l = KMeans(n_clusters=params, algorithm='full').fit_predict(sparse_ratings)

    # clustered_movie = {}
    # for i in range(len(predictions_l)):
    #     clustered_movie[movies['id'][i]] = predictions_l[i]
    # print(clustered_movie)

    # nonlibrary
    predictions = kmeans(params, user_movie_ratings.fillna(0))
    test = user_movie_ratings.T
    cluster = predictions.train_cluster()
    predictions_n = np.array(cluster[2]['Closet_Cluster'])

    clustered_user = {}
    for i in range(len(predictions_n)):
        clustered_user[movies['id'][i]] = predictions_n[i]
    return clustered_user
    # print(clustered_movie)


def kmeans_movie(params, movies, ratings):
    movies = pd.DataFrame.from_records(movies)
    ratings = pd.DataFrame(ratings)
    data = pd.merge(ratings, movies, left_on='movie_id', right_on='id')

    movies_genre_2 = df_kmeans_movie(movies)
    # library 사용
    # predictions = make_kmeans.kmeans(16, movies_genre_2.fillna(0))
    # cluster = predictions.train_cluster()
    # predictions_n = np.array(cluster[2]['Closet_Cluster'])  

    # clustered_movie = {}
    # for i in range(len(predictions_1)):
    #     clustered_movie[movies_genre['movieId'][i]] = predictions_1[i]

    # library 사용 X
    predictions = kmeans(params, movies_genre_2.fillna(0))
    cluster = predictions.train_cluster()
    predictions_n = np.array(cluster[2]['Closet_Cluster'])  

    clustered_movie = {}
    for i in range(len(predictions_n)):
        clustered_movie[movies['id'][i]] = predictions_n[i]
    return clustered_movie