import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    start_urls = [
        "https://books.toscrape.com/"
    ]

    def parse(self, response):
        for book in response.css("li.col-xs-6"):
            yield {
                "title": book.css("h3 a::attr(title)").get(),
                "price": book.css("p.price_color::text").get(),
                "image_url": response.urljoin(book.css("img.thumbnail::attr(src)").get()),
                "detail_url": response.urljoin(book.css("h3 a::attr(href)").get())
            }
        yield from response.follow_all(css='ul.pager a', callback=self.parse)
