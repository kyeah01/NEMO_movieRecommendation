from django.conf.urls import url
from django.urls import path
from api.views import movie_views, rating_views, auth_views, clustering_views
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

urlpatterns = [
    path('auth/verify/', verify_jwt_token),
    path('auth/refresh/', refresh_jwt_token),
    # 초기 setup을 위한 url
    url('auth/signup-many/$', auth_views.signup_many, name='sign_up_many'),
    url('auth/signup/$', auth_views.signup, name='sign_up'),
    url('rating_many/$', rating_views.rating_many, name='rating_list'),

    url('cluster/user', clustering_views.cluster_user_method, name="cluster_user_method"),
    url('cluster/movie', clustering_views.cluster_movie_method, name="cluster_movie_method"),
    url('cluster/custom', clustering_views.user_customized_recommendation, name="user_customized_recommendation"),

    url('cluster/', clustering_views.setup, name="cluster_setup"),

    url('movies/$', movie_views.movies, name='movie_list'),

    url('rating/$', rating_views.rating, name='rating'),

    path('profile/<int:user_id>/newmovies', auth_views.profileUnRatedMovieSearch, name='profileUnRatedMovieSearch'),
    path('profile/<int:user_id>', auth_views.profile, name='profile'),
    path('profile/', auth_views.profileSearch, name='profileSearch'),
    url('auth/login', auth_views.userLogin, name='login'),
    url('auth/logout', auth_views.userLogout, name='logout'),
    path('auth/', obtain_jwt_token),


    path('subscription/<int:user_id>', auth_views.subscription, name="subscription"),
]
