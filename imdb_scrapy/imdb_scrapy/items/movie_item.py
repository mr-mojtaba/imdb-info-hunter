import scrapy


class MovieItem(scrapy.Item):
    name = scrapy.Field()
    release = scrapy.Field()
    rating = scrapy.Field()
    vote = scrapy.Field()
    unit = scrapy.Field()
    duration = scrapy.Field()
    synopsis = scrapy.Field()
    link = scrapy.Field()
    pass
