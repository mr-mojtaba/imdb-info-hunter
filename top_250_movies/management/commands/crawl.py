from django.core.management.base import BaseCommand
import subprocess
import os


class Command(BaseCommand):
    help = "Run Scrapy spider: TopMovies"

    def handle(self, *args, **options):
        try:
            # تعیین مسیر فایل اسپایدر TopMovies
            spiders_dir = os.path.abspath(
                os.path.join(
                    os.path.dirname(__file__),
                    '..',
                    '..',
                    '..',
                    'imdb_scrapy',
                    'imdb_scrapy',
                    'spiders'
                )
            )

            os.chdir(spiders_dir)

            # Run movie_spider
            self.stdout.write("Running TopMovies spider...")
            self.stdout.write("This process may take a few minutes...")
            self.stdout.write(
                "you can read The logs from: imdb_scrapy"
                "/imdb_scrapy/spiders scrapy.log file"
            )
            subprocess.run(["scrapy", "crawl", "top_250_movies"], check=True)

        except subprocess.CalledProcessError as e:
            self.stderr.write(f"Error running spider: {e}")
        except Exception as e:
            self.stderr.write(f"An error occurred: {str(e)}")
