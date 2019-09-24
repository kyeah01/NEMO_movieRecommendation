from django.contrib import admin
from .models import Profile, Movie, Rating, ClusterModel

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    fields = ['id', 'title', 'genres', 'group']

admin.site.register(Profile)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating)
admin.site.register(ClusterModel)