import scrapy


# document.querySelector("body > div:nth-child(3) > table > tbody > tr > td > center > table > tbody > tr > td > table:nth-child(1) > tbody > tr > td > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(5) > td:nth-child(4) > table > tbody > tr > td:nth-child(3) > div > b > a")


class SpiderTest(scrapy.Spider):
    name = 'spider_test'
    start_urls = [
        'https://top40-charts.com/chart.php?cid={}'.format(x) for x in range(2, 24)]

    def parse(self, response):
        country_count = response.css(
            'font.biggerblue::text').extract()[0].split()
        # songs = response.css('.latc_song')
        songs = response.css(
            'a[href*="song.php"]::text').extract()
        artists = response.css(
            'a[href*="artist.php"]::text').extract()

        country = country_count[:-2]
        count = country_count[-1]

        yield {'country': country, 'song_count_top': count, 'song_list': songs, 'artists': artists}
