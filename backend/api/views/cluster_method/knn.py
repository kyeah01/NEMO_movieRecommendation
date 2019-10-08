import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import pairwise_distances
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# USER BASED

def find_n_neighbours(df,n):
    order = np.argsort(df.values, axis=1)[:, :n]
    df = df.apply(lambda x: pd.Series(x.sort_values(ascending=False)
           .iloc[:n].index, 
          index=['top{}'.format(i) for i in range(1, n+1)]), axis=1)
    return df

def knn_user(movies, ratings):
    movies = pd.DataFrame.from_records(movies)
    ratings = pd.DataFrame(ratings)
    # data = pd.merge(ratings, movies, left_on='movie_id', right_on='id')
    Mean = ratings.groupby(by="user_id",as_index=False)['rating'].mean()
    rating_avg = pd.merge(ratings,Mean, on='user_id')
    rating_avg['adg_rating'] = rating_avg['rating_x'] - rating_avg['rating_y']
    check = pd.pivot_table(rating_avg, values='rating_x', index='user_id', columns='movie_id')
    final = pd.pivot_table(rating_avg, values='adg_rating', index='user_id', columns='movie_id')
    
    final_movie = final.fillna(final.mean(axis=0))
    final_user = final.apply(lambda row: row.fillna(row.mean()), axis=1)

    # 유저 유사도 계산하기
    cosine = cosine_similarity(final_movie)
    np.fill_diagonal(cosine, 0 )
    similarity_with_movie =pd.DataFrame(cosine,index=final_movie.index)
    similarity_with_movie.columns=final_movie.index

    # cosine
    cosine_similar = cosine_similarity(final_user)
    np.fill_diagonal(cosine_similar, 0)
    # final user이면 양쪽 column 기준이 user인지
    similarity_with_user = pd.DataFrame(cosine_similar,index=final_user.index)
    similarity_with_user.columns=final_user.index

    # top 5 neighbours for each user
    sim_user_5 = find_n_neighbours(similarity_with_user,5)
    sim_user_5_dict = {}
    sim_user_5 = sim_user_5.T
    for i in sim_user_5:
        sim_user_5_dict[i] = sim_user_5[i].tolist()

    return sim_user_5_dict


# ITEM BASED

def fuzzy_matching(mapper, fav_movie, verbose=True):
    match_tuple = []
    # get match
    for title, idx in mapper.items():
        ratio = fuzz.ratio(title.lower(), fav_movie.lower())
        if ratio >= 60:
            match_tuple.append((title, idx, ratio))
    # sort
    match_tuple = sorted(match_tuple, key=lambda x: x[2])[::-1]
    if not match_tuple:
        return
    return match_tuple[0][1]

def make_recommendation(model_knn, data, mapper, fav_movie, n_recommendations):
    # fit
    model_knn.fit(data)
    idx = fuzzy_matching(mapper, fav_movie, verbose=True)
    distances, indices = model_knn.kneighbors(data[idx], n_neighbors=n_recommendations+1)
    # get list of raw idx of recommendations
    raw_recommends = sorted(list(zip(indices.squeeze().tolist(), distances.squeeze().tolist())), key=lambda x: x[1])[:0:-1]
    recommends_5 = []
    # print(raw_recommends)
    for i in raw_recommends:
        recommends_5.append(i[0])
    return recommends_5


def knn_movie(movies, ratings):
    ###################### 1 데이터 불러오기  ############################
    movies = pd.DataFrame.from_records(movies)
    ratings = pd.DataFrame(ratings)
    movies = movies.drop(columns=['group'])
    movies = movies.drop(columns=['genres'])
    ratings = ratings.drop(columns=['rating_date'])
    #################### 2  데이터 matrix로 가공하기 ####################333
    movie_user_matrix = pd.pivot_table(ratings, index='movie_id', columns= 'user_id', values='rating').fillna(0)
    movie_to_idx = {}
    # print('keys :', movies.keys())
    for i in range(len(movies)):
        movie_to_idx[movies.title[i]] =movies['id'][i]
    print('movie_to_idx :', movie_to_idx)
    # convert dataframe of movie features to scipy sparse matrix -- 매트릭스를 sparse 매트릭스로 바꾸기
    movie_user_mat_sparse = csr_matrix(movie_user_matrix.values)
    ######################## 3_KNN 적용하기   ############################
    # define model
    model_knn = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=20, n_jobs=-1)
    # fit
    model_knn.fit(movie_user_mat_sparse)
    ############################## 4 KNN MOVIE RECOMMENDATIONS ##########
        
    final_recommend={}
    for i in range(10):
        # movie_to_idx[movies.title[i]] = movies['id'][i]
        my_favorite = movies.title[i]

        result = make_recommendation(
            #사용 알고리즘 knn
            model_knn=model_knn,
            # 사용할 데이터 - 정렬해놓은 sparse matrix
            data=movie_user_mat_sparse,
            # 유사한 영화 찾고자하는 좋아하는 movie
            fav_movie=my_favorite,
            # index로 영화를 찾아서
            mapper=movie_to_idx,
            # n 개의 개수만큼 정렬하기
            n_recommendations=5)
        
        final_recommend[movies['id'][i]] = result
        finaaa = movie_user_mat_sparse

   
    return finaaa
