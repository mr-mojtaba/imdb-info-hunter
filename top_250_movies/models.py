from django.db import models


# Create your models here.
class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=100)
    release = models.IntegerField(null=False)
    rating = models.FloatField(null=False)
    vote = models.FloatField(null=False, max_length=10)
    unit = models.CharField(null=True, max_length=1)
    duration = models.CharField(null=False, max_length=10)
    synopsis = models.TextField(null=False)
    link = models.URLField(null=False, max_length=100)

    class Meta:
        unique_together = ('name', 'release')


# class Genre(models.Model):
#     genre_id = models.AutoField(primary_key=True)
#     genre_name = models.CharField(null=False, max_length=20, unique=True)


# class Director(models.Model):
#     director_id = models.AutoField(primary_key=True)
#     director_name = models.CharField(null=False, max_length=30)


# class Writer(models.Model):
#     writer_id = models.AutoField(primary_key=True)
#     writer_name = models.CharField(null=False, max_length=30)


# class Actor(models.Model):
#     actor_id = models.AutoField(primary_key=True)
#     actor_name = models.CharField(null=False, max_length=30)


# class MovieGenre(models.Model):
#     movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
#     genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)


# class MovieDirector(models.Model):
#     movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
#     director_id = models.ForeignKey(Director, on_delete=models.CASCADE)
#
#     class Meta:
#         unique_together = ('movie_id', 'director_id')


# class MovieWriter(models.Model):
#     movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
#     Writer_id = models.ForeignKey(Writer, on_delete=models.CASCADE)


# class MovieActor(models.Model):
#     movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
#     actor_id = models.ForeignKey(Actor, on_delete=models.CASCADE)
