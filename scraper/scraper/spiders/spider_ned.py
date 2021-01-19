import scrapy
from scraper.items import Song


class SpiderNed(scrapy.Spider):
    name = 'spider_ned'
    start_urls = [
        'https://www.top40.nl/top40/2019/week-15'
    ]

    def parse(self, response):
        result = Song()

        songs = response.css('div.song-details')
        chart_position = 1
        for song in songs:
            chart_position = chart_position
            title = song.css('a h3.title::text').extract()
            artists = song.css('a p.artist::text').extract()

            result['title'] = title
            result['artist'] = artists
            result['chart_position'] = chart_position
            result['production_house'] = None
            chart_position += 1
            yield result
