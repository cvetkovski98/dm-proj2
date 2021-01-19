import scrapy
import pandas as pd

from ..items import EtsyShopItem


class EtsyShopSpider(scrapy.Spider):
    name = 'etsy_shops'
    # start_urls = [
    #     'https://www.etsy.com/search/shops?page=' + str(i) for i in range(1, 1200)
    # ]
    start_urls = [
        f'https://www.etsy.com/shop/{l}' for l in pd.read_csv('products_final.csv')['productShop']
    ]

    def parse(self, response, **kwargs):
        links = response.css('.wt-card a::attr(href)').extract()
        for link in links:
            print(str(link))
            yield response.follow(str(link), callback=self.parse_shop)

    def parse_shop(self, response):
        items = EtsyShopItem()
        shop_name = response.css('.mb-lg-1::text').extract()
        noOfItems = response.css('.wt-mr-md-2::text').extract_first()
        shopOwner = response.css('.img-container p::text').extract()
        shopAddress = response.css('.br-lg-1::text').extract()
        noOfSales = response.css('.no-wrap a::text').extract_first()

        items['shopName'] = shop_name
        items['noOfItems'] = noOfItems
        items['shopOwner'] = shopOwner
        items['shopAddress'] = shopAddress
        items['noOfSales'] = noOfSales if noOfSales is not None else ''
        yield items
