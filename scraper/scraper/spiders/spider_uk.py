import scrapy
from scraper.items import Song


class SpiderUk(scrapy.Spider):
    name = 'spider_uk'
    start_urls = [
        'https://www.officialcharts.com/charts/uk-top-40-singles-chart/20190405/750140/'
    ]

    def parse(self, response):
        result = Song()

        songs = response.css('div.title-artist')
        chart_position = 1
        for song in songs:
            chart_position = chart_position
            title = song.css('div.title > a::text').extract()
            artists = song.css('div.artist > a::text').extract()
            prod_houses = song.css(
                'div.label-cat > span.label::text').extract()

            result['title'] = title[0]
            result['artist'] = artists[0]
            result['production_house'] = prod_houses[0]
            result['chart_position'] = chart_position
            chart_position += 1

            yield result
