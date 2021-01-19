import datetime

import scrapy
from scraper.items import SongUK


class SpiderUkAll(scrapy.Spider):
    name = 'spider_uk_all'
    start_urls = ['https://www.officialcharts.com/charts/uk-top-40-singles-chart/{}/7501/'.format(x) for x in [
        (datetime.date(2018, 12, 31) + datetime.timedelta(weeks=i)).strftime('%Y%m%d') for i in range(0, 52)
    ]]

    def parse(self, response):
        result = SongUK()

        songs = response.css('div.title-artist')
        no_of_weeks = response.css('td:nth-child(5)::text').extract()
        chart_position = 1
        ulr = response.request.url
        weekstr = ulr.split('/')[-3]
        week = datetime.datetime.strptime(weekstr, "%Y%m%d").isocalendar()[1]
        for song, week_on_chart in zip(songs, no_of_weeks):
            chart_position = chart_position
            title = song.css('div.title > a::text').extract()
            artists = song.css('div.artist > a::text').extract()
            prod_houses = song.css(
                'div.label-cat > span.label::text').extract()

            result['title'] = title[0]
            result['artist'] = artists[0]
            result['production_house'] = prod_houses[0]
            result['chart_position'] = chart_position
            result['week'] = week
            result['country'] = 'UK'
            result['weeks_on_chart'] = week_on_chart
            chart_position += 1

            yield result
