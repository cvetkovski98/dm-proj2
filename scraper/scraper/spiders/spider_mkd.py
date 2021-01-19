import scrapy
from scraper.items import Song


class SpiderMKD(scrapy.Spider):
    name = 'spider_mkd'
    start_urls = [
        'https://popnable.com/macedonia/charts/top-40/april-2019'
    ]

    def parse(self, response):
        result = Song()

        songs = response.css('div.list-group.chart-panel')
        chart_position = 1
        for song in songs:
            chart_position = chart_position
            title = song.css('span.list-group-item.singer-container>a::text').extract()
            artists = song.css('span.list-group-item>a::text').extract()

            result['title'] = title
            result['artist'] = artists
            result['chart_position'] = chart_position
            result['production_house'] = None
            chart_position += 1

            yield result
