import scrapy


class BookItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    image_url = scrapy.Field()
    detail_url = scrapy.Field()
