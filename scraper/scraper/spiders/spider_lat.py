import scrapy
from scraper.items import Song


class SpiderLat(scrapy.Spider):
    name = 'spider_lat'
    start_urls = [
        'https://www.ehrhiti.lv/arhivs/ehr-top-40?airDate=2019.04.12'
    ]

    def parse(self, response):
        result = Song()

        songs = response.css('div.song__info')
        chart_position = 1
        for song in songs:
            chart_position = chart_position
            title = song.css('h2.song__title::text').extract()
            artists = song.css('a > h3.song__artist::text').extract()

            result['title'] = title
            result['artist'] = artists
            result['chart_position'] = chart_position
            result['production_house'] = None
            chart_position += 1

            yield result
