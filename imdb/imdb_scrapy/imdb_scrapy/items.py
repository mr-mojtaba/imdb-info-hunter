# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from imdb.top_250_movies.models import Movie


class MovieItem(DjangoItem):
    django_model = Movie


# class DirectorItem(DjangoItem):
#     django_model = Director


# class ImdbScrapyItem(scrapy.Item):
#     movie_name = scrapy.Field()
#     movie_release = scrapy.Field()
#     movie_rating = scrapy.Field()
#     movie_vote = scrapy.Field()
#     vote_unit = scrapy.Field()
#     # movie_genre = scrapy.Field()
#     movie_duration = scrapy.Field()
#     movie_director = scrapy.Field()
#     # movie_writer = scrapy.Field()
#     # movie_stars = scrapy.Field()
#     movie_synopsis = scrapy.Field()
#     movie_link = scrapy.Field()
