import scrapy
from imdb_scrapy.items import ImdbScrapyItem


class Test(scrapy.Spider):
    """
    This spider extracts information of the top 250 movies from IMDb.
    """
    name = "top_250_movies"
    allowed_domains = ["imdb.com"]
    start_urls = ["https://imdb.com/chart/top/"]
    custom_settings = {
        # Defining a fake User_Agent
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }

    i = 0

    def parse(self, response):
        """
        Parses the main page to extract links to individual movie pages.
        """
        links = response.css('ul a.ipc-title-link-wrapper::attr(href)').getall()

        for link in links:
            yield response.follow(link, callback=self.parse_movies)

    def parse_movies(self, response):
        movie_genres = response.xpath("//div[@class='ipc-chip-list__scroller']//a//text()").getall()

        print("\t")
        print("*" * 20)
        print(movie_genres)
