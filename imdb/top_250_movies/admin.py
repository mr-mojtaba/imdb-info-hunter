from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'release', 'rating']
    ordering = ['movie_id']
    search_fields = ['movie_id', 'name', 'release', 'rating']
    list_filter = ['movie_id', 'name', 'release', 'rating']


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['director_id', 'director_name']
    ordering = ['director_id']
    search_fields = ['director_id', 'director_name']
    list_filter = ['director_id', 'director_name']


@admin.register(MovieDirector)
class MovieDirectorAdmin(admin.ModelAdmin):
    list_display = ['movie_id', 'director_id']
    ordering = ['movie_id']
    search_fields = ['movie_id', 'director_id']
    list_filter = ['movie_id', 'director_id']
