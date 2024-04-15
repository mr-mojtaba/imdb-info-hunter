from django.db import models


# Create your models here.
class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=100)
    release = models.IntegerField(null=False)
    rating = models.FloatField(null=False)
    duration = models.CharField(null=False, max_length=10)
    synopsis = models.TextField(null=False)
    link = models.URLField(null=False, max_length=100)
