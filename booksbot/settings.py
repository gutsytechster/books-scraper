# Scrapy settings for booksbot project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "booksbot"

SPIDER_MODULES = ["booksbot.spiders"]
NEWSPIDER_MODULE = "booksbot.spiders"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

SPIDER_MIDDLEWARES = {
    "scrapy_autounit.AutounitMiddleware": 950,
}

# Enable this whenever updating tests for the spider
AUTOUNIT_ENABLED = False
