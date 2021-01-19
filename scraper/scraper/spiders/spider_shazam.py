import scrapy
from scraper.items import ShazamSong

country_list = ['Argentina', 'Australia', 'Austria', 'Belarus', 'Belgium', 'Brazil', 'Bulgaria', 'Canada', 'Chile',
                'China', 'Colombia', 'Croatia', 'Denmark', 'Egypt', 'Finland', 'France', 'Germany', 'Greece', 'Hungary',
                'India', 'Indonesia', 'Ireland', 'Israel', 'Italy', 'Japan', 'Kazakhstan', 'Malaysia', 'Mexico',
                'Morroco', 'Netherlands', 'New Zealand', 'Norway', 'Peru', 'Poland', 'Portugal', 'Romania', 'Russia',
                'Saudi', 'Arabia', 'Singapore', 'South', 'Africa', 'Spain', 'Sweden', 'Switzerland', 'Taiwan',
                'Thailand', 'Turkey', 'Ukraine', 'United Kingdom', 'United States', 'Uruguay', 'Venezuela']


class SpiderShazam(scrapy.Spider):
    name = 'spider_shazam'
    start_urls = ['https://www.shazam.com/charts/top-200/{}'.format(x) for x in
                  ['-'.join(list_item.lower().split()) for list_item in country_list]]

    def parse(self, response):
        country = response.request.url.split('/')[-1]
        result = ShazamSong()
        songs = response.css('.shz-partial-track')
        chart_position = 1
        for song in songs:
            title = song.css('div.title div.ellip::text').extract()
            artist = song.css('div.artist div.ellip::text').extract()

            result['title'] = title
            result['artist'] = artist
            result['chart_position'] = chart_position
            result['country'] = country
            chart_position += 1
            yield result
