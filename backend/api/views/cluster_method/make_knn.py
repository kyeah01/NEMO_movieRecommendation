import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import pairwise_distances
from sklearn.neighbors import NearestNeighbors
from scipy.sparse import csr_matrix
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def knn_user(movies, ratings):
    
    # user_movie_ratings, sparse_ratings = df_kmeans_user(data)

    # # nonlibrary
    # predictions = kmeans(params, user_movie_ratings.fillna(0))
    # test = user_movie_ratings.T
    # cluster = predictions.train_cluster()
    # predictions_n = np.array(cluster[2]['Closet_Cluster'])

    # clustered_user = {}
    # for i in range(len(predictions_n)):
    #     clustered_user[movies['id'][i]] = predictions_n[i]
    # clustered_movie = movie_user_matrix
    return clustered_user
    # print(clustered_movie)


def knn_movie(movies, ratings):
    ###################### 1 데이터 불러오기  ############################
    movies = pd.DataFrame.from_records(movies)
    ratings = pd.DataFrame(ratings)
    movies = movies.drop(columns=['group'])
    movies = movies.drop(columns=['genres'])
    ratings = ratings.drop(columns=['rating_date'])
    #################### 2  데이터 matrix로 가공하기 ####################333
    movie_user_matrix = pd.pivot_table(ratings, index='movie_id', columns= 'user_id', values='rating').fillna(0)
    movie_to_idx =  {
    movie: i for i, movie in 
    enumerate(list(movies.set_index('id').loc[movie_user_matrix.index].title))
}



    # convert dataframe of movie features to scipy sparse matrix -- 매트릭스를 sparse 매트릭스로 바꾸기
    movie_user_mat_sparse = csr_matrix(movie_user_matrix.values)
    ######################## 3_KNN 적용하기   ############################
    # define model
    model_knn = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=20, n_jobs=-1)
    # fit
    model_knn.fit(movie_user_mat_sparse)
    ############################## 4 KNN MOVIE RECOMMENDATIONS ##########
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
            print('Oops! No match is found')
            return
        if verbose:
            print('Found possible matches in our database: {0}\n'.format([x[0] for x in match_tuple]))
        return match_tuple[0][1]
    
    def make_recommendation(model_knn, data, mapper, fav_movie, n_recommendations):
        # fit
        model_knn.fit(data)
        # get input movie index
        print('You have input movie:', fav_movie)
        idx = fuzzy_matching(mapper, fav_movie, verbose=True)
        # inference
        print('Recommendation system start to make inference')
        print('......\n')
        distances, indices = model_knn.kneighbors(data[idx], n_neighbors=n_recommendations+1)
        # get list of raw idx of recommendations
        raw_recommends = \
            sorted(list(zip(indices.squeeze().tolist(), distances.squeeze().tolist())), key=lambda x: x[1])[:0:-1]
        # get reverse mapper
        reverse_mapper = {v: k for k, v in mapper.items()}
        # print recommendations
        print('Recommendations for: {} are'.format(fav_movie))
        for i, (idx, dist) in enumerate(raw_recommends):
            # print('{0}: {1}, with distance of {2}'.format(i+1, reverse_mapper[idx], dist))
            print('{0}: {1}'.format(idx, reverse_mapper[idx]))
        
    

    my_favorite = str(input("Enter the moviename : "))

    clustered_movie = make_recommendation(
        model_knn=model_knn,
        data=movie_user_mat_sparse,
        fav_movie=my_favorite,
        mapper= movie_to_idx,
        n_recommendations=10)
    # clustered_movie = len(movie_user_matrix)
   
    return clustered_movie
    