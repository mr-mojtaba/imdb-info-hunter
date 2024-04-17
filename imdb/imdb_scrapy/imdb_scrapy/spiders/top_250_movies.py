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
        """
        Extracts information of each movie from its individual page.
        """
        movie_name = response.css('h1 span::text').extract_first()
        movie_release = response.css(
                'ul.ipc-inline-list > li.ipc-inline-list__item > a.ipc-link--baseAlt[href*="releaseinfo"]::text').get()
        movie_rating = response.css("span.sc-bde20123-1::text").get()
        movie_vote = response.css("div.sc-bde20123-3::text").get()
        vote_unit = None
        # movie_genre = response.xpath("//div[@class='ipc-chip-list__scroller']//a//text()").getall()
        movie_duration = response.css('ul.ipc-inline-list > li.ipc-inline-list__item:nth-child(3)::text').get()
        movie_director = response.css("a.ipc-metadata-list-item__list-content-item::text").get()
        # movie_writer = set(response.css(
        #         'ul.ipc-metadata-list li:nth-child(2).ipc-metadata-list__item > '
        #         'div.ipc-metadata-list-item__content-container > ul.ipc-inline-list > li.ipc-inline-list__item > '
        #         'a.ipc-metadata-list-item__list-content-item[href*="/name/nm"]::text').getall())
        # movie_stars = set(response.xpath("//a[text()='Stars']/following-sibling::div//a//text()").getall())
        movie_synopsis = response.css('span.sc-466bb6c-1::text').get()
        movie_link = response.url

        # Operations
        for i in movie_vote:
            if i == "K" or i == "M":
                vote_unit = i
                movie_vote = movie_vote.replace(i, "")

        if vote_unit is not None:
            unit = str(vote_unit)
        else:
            unit = ""

        self.i += 1
        # Prints.
        print("\t")
        print("*" * 20)
        print(self.i)
        print("Movie name: {}".format(movie_name))
        print("Date of Release: {}".format(movie_release))
        print("IMDB Rating: {}/10 - {}{} Vote".format(movie_rating, movie_vote, unit))
        # print("Genre: {}".format(", ".join(str(item) for item in movie_genre)))
        print("Duration: {}".format(movie_duration))
        print("Director: {}".format(movie_director))
        # print("Writer(s): {}".format(", ".join(str(item) for item in movie_writer)))
        # print("Stars: {}".format(", ".join(str(item) for item in movie_stars)))
        print("Synopsis : {}".format(movie_synopsis))
        print("Link: {}".format(movie_link))
        print("*" * 20)
        print("\t")

        item = ImdbScrapyItem()
        item['movie_name'] = movie_name
        item['movie_release'] = movie_release
        item['movie_rating'] = movie_rating
        item['movie_vote'] = movie_vote
        item['vote_unit'] = vote_unit
        # item['movie_genre'] = movie_genre
        item['movie_duration'] = movie_duration
        item['movie_director'] = movie_director
        # item['movie_writer'] = movie_writer
        # item['movie_stars'] = movie_stars
        item['movie_synopsis'] = movie_synopsis
        item['movie_link'] = movie_link
        return item
