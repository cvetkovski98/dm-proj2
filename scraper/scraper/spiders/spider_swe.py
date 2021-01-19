import scrapy
from scraper.items import Song


class SpiderSwe(scrapy.Spider):
    name = 'spider_swe'
    start_urls = [
        'https://sverigesradio.se/sida/topplista.aspx?programid=2697&date=2019-04-07'
    ]

    def parse(self, response):
        result = Song()

        songs = response.css('div.track__info')
        chart_position = 1
        for song in songs:
            chart_position = chart_position
            full = song.css('span.track__title::text').extract()[0].split(' - ')
            title = full[0]
            artists = full[1]

            result['title'] = title
            result['artist'] = artists
            result['chart_position'] = chart_position
            result['production_house'] = None
            chart_position += 1

            yield result
