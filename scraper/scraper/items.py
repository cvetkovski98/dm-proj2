# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Song(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    country = scrapy.Field()
    title = scrapy.Field()
    artist = scrapy.Field()
    production_house = scrapy.Field()
    chart_position = scrapy.Field()
    count = scrapy.Field()


class SongUK(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    country = scrapy.Field()
    title = scrapy.Field()
    artist = scrapy.Field()
    production_house = scrapy.Field()
    chart_position = scrapy.Field()
    week = scrapy.Field()
    weeks_on_chart = scrapy.Field()


class ShazamSong(scrapy.Item):
    country = scrapy.Field()
    title = scrapy.Field()
    artist = scrapy.Field()
    chart_position = scrapy.Field()


class EtsyShopItem(scrapy.Item):
    # define the fields for your item here like:
    shopName = scrapy.Field()
    noOfItems = scrapy.Field()
    shopOwner = scrapy.Field()
    shopAddress = scrapy.Field()
    noOfSales = scrapy.Field()
    shopImageLink = scrapy.Field()
    yearCreated = scrapy.Field()


class EtsyShopFeedbacks(scrapy.Item):
    shopName = scrapy.Field()
    reviewer = scrapy.Field()
    feedbackDate = scrapy.Field()
    feedback = scrapy.Field()
    feedbackGrade = scrapy.Field()
    feedbackForProduct = scrapy.Field()


class EtsyProducts(scrapy.Item):
    productUrl = scrapy.Field()
    productName = scrapy.Field()
    productCategory = scrapy.Field()
    productRating = scrapy.Field()
    productReviews = scrapy.Field()
    productPriceSale = scrapy.Field()
    productPriceOriginal = scrapy.Field()
    productShop = scrapy.Field()


class EtsyProductFeedbacks(scrapy.Item):
    productUrl = scrapy.Field()
    productName = scrapy.Field()
    productFeedbackRating = scrapy.Field()
    productFeedbackText = scrapy.Field()
    productFeedbackReviewer = scrapy.Field()
    productFeedbackDate = scrapy.Field()


class EtsyShopOwners(scrapy.Item):
    shopName = scrapy.Field()
    shopOwnerName = scrapy.Field()
    ownerFollowers = scrapy.Field()
    ownerFollowing = scrapy.Field()
    ownerLocation = scrapy.Field()

