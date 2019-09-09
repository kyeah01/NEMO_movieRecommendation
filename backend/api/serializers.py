from django.db.models import Avg
from rest_framework import serializers
from .models import Profile, Movie, Rating, ClusterModel
from django.contrib.auth.models import User

class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    username = serializers.SerializerMethodField('get_username')
    is_staff = serializers.SerializerMethodField('get_is_staff')
    similaruser = serializers.SerializerMethodField('get_group')
    ratingmovie = serializers.SerializerMethodField('get_ratingmovie')

    class Meta:
        model = Profile
        fields = ('id', 'username', 'is_staff', 'gender', 'age', 'occupation', 'group', 'similaruser', 'ratingmovie')

    def get_username(self, obj):
        return obj.user.username
    
    def get_ratingmovie(self, obj):
        data = User.objects.get(id=obj.id)
        datas = data.rating_set.all()
        rr = []
        for i in datas :
            rr.append(i.movie.title)
        return rr

    def get_is_staff(self, obj):
        return obj.user.is_staff
        
    def get_group(self, obj):
        users = Profile.objects.filter(group=obj.user.profile.group)
        datas = []
        for i in users :
            data = User.objects.get(id=i.id) 
            datas.append(data.username)
        return datas


class RatingSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField('get_profileInfo')
    
    class Meta:
        model = Rating
        fields = ['movie', 'user', 'rating', 'rating_date',]

    def get_profileInfo(self, obj):
        return { 'id':obj.user.id, 'name': obj.user.username, 'Gender': obj.user.profile.gender, 'age': obj.user.profile.age, 'Occupation': obj.user.profile.occupation }

class MovieSerializer(serializers.ModelSerializer):
    genres_array = serializers.ReadOnlyField()
    rating = RatingSerializer(many=True, read_only=True, source='rating_set')
    view_cnt = serializers.ReadOnlyField(source='rating_set.count')
    average_rating = serializers.SerializerMethodField()
    similarmovie = serializers.SerializerMethodField('get_group')

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genres_array', 'view_cnt', 'rating', 'average_rating', 'group', 'similarmovie']

    def get_average_rating(self, obj):
        average = obj.rating_set.all().aggregate(Avg('rating')).get('rating__avg')
        if average is None:
            return 0
        else:
            return round(average, 1)

    def get_group(self, obj):
        movies = Movie.objects.filter(group=obj.group)
        datas = []
        for i in movies :
            datas.append(i.title)
        return datas

class UserSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField('get_profileInfo')
    class Meta:
        model = User
        fields = ('id', 'username', 'is_staff', 'profile')
        
    def get_profileInfo(self, obj):
        return { 'gender': obj.profile.gender, 'age': obj.profile.age, 'Occupation': obj.profile.occupation }

class ClusterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClusterModel
        fields = ('based', 'method', 'params')