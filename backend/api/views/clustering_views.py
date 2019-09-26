from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Movie, Rating, ClusterModel, Profile
from api.serializers import ClusterSerializer

from api.views.cluster_method.make_kmeans import kmeans_user, kmeans_movie
from api.views.cluster_method.make_knn import knn_movie
from api.views.cluster_method.gmm import GaussianMix
from api.views.cluster_method.Hierarchical import Hierarchical


@api_view(['POST'])
def setup(request):
    # 기본으로 설정되는 값은 kmeans, param=2
    # DB에 없으면 만든다.
    if not len(ClusterModel.objects.all()):
        ClusterModel.objects.create(based="user", method=1, params=2, id=1)
        user_result = kmeans_user(2, Movie.objects.all().values(), Rating.objects.all().values())
        for key, value in user_result.items():
            user = Profile.objects.get(id=key)
            user.group = value
            user.save()

        ClusterModel.objects.create(based="movie", method=1, params=2, id=2)
        movie_result = kmeans_movie(2, Movie.objects.all().values(), Rating.objects.all().values())
        for key, value in movie_result.items():
            movie = Movie.objects.get(id=key)
            movie.group = value
            movie.save()
    return Response(status=status.HTTP_200_OK)

# cluster model에서 user는 1번, movie는 2번
@api_view(['GET', 'POST'])
def cluster_user_method(request):

    if request.method == 'POST':
        method = request.data.get('method')
        params = request.data.get('params')
        if method and params:
            if method == 'K':
                # kmeans algorithm 적용
                result = kmeans_user(params, Movie.objects.all().values(), Rating.objects.all().values())
            if method == 'G':
                # gausian algorithm 적용
                gaussian = GaussianMix(Rating.objects.all().values(), Movie.objects.all().values(), 'user', params)
                result = gaussian.get_result()

            if method == 'H':
                # hierarchical algorithm 적용
                hier = Hierarchical(Movie.objects.all().values(), Rating.objects.all().values(), 'user')
                result = hier.cluster(params)

            for key, value in result.items():
                user = Profile.objects.get(id=key)
                user.group = value
                user.save()
            
            # cluster method 저장
            now = ClusterModel.objects.get(id=1)
            algorithms = {'K':1, 'G':2, 'H':3}
            now.method = algorithms[method]
            now.params = params
            now.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_200_OK)

    if request.method == 'GET':
        # now = ClusterModel.objects.get(id=1)
        # serializer = ClusterSerializer(now)
        print('hi')
        return Response(status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def cluster_movie_method(request):
    if request.method == 'POST':
        method = request.data.get('method')
        params = request.data.get('params')


        if method and params:

            if method == "K":
                result = kmeans_movie(params, Movie.objects.all().values(), Rating.objects.all().values())

            if method == "G":
                gaussian = GaussianMix(Rating.objects.all().values(), Movie.objects.all().values(), 'item', params)
                result = gaussian.get_result()

            if method == 'H':
                hier = Hierarchical(Movie.objects.all().values(), Rating.objects.all().values(), 'movie')
                result = hier.cluster(params)
            
            for key, value in result.items():
                movie = Movie.objects.get(id=key)
                movie.group = value
                movie.save()
            # cluster method 저장
            now = ClusterModel.objects.get(id=2)
            algorithms = {'K':1, 'G':2, 'H':3}
            now.method = algorithms[method]
            now.params = params
            now.save()
            return Response(status=status.HTTP_200_OK)


    if request.method == 'GET':
        # now = ClusterModel.objects.get(id=1)
        # serializer = ClusterSerializer(now)
        a =  knn_movie(Movie.objects.all().values(), Rating.objects.all().values())
        # print('hi')
        print(a)
        return Response(status=status.HTTP_200_OK)

