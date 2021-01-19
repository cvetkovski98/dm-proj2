import scrapy
from scraper.items import Song


class SpiderCan(scrapy.Spider):
    name = 'spider_can'
    start_urls = [
        'https://www.billboard.com/charts/year-end/2019/canadian-hot-100'
    ]

    def parse(self, response):
        result = Song()

        songs = response.css('.ye-chart-item__text')
        chart_position = 1
        for song in songs:
            chart_position = chart_position
            title = song.css('.ye-chart-item__title::text').extract()
            artists_with_a = song.css('.ye-chart-item__artist a::text').extract()
            artists_without_a = song.css('.ye-chart-item__artist::text').extract()
            art = artists_with_a
            if len(artists_with_a) == 0:
                art = artists_without_a
            result['title'] = title
            result['artist'] = art
            result['production_house'] = None
            result['chart_position'] = chart_position
            chart_position += 1

            yield result
