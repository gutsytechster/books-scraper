# Books Scraper

[![Coverage Status](https://coveralls.io/repos/github/gutsytechster/books-scraper/badge.svg?branch=main)](https://coveralls.io/github/gutsytechster/books-scraper?branch=main) [![Build Status](https://travis-ci.org/gutsytechster/books-scraper.svg?branch=main)](https://travis-ci.org/gutsytechster/books-scraper)

A book spider to scrape books from [books.toscrape.com](https://books.toscrape.com)

## Setup
1. Create and activate a virtual environment(this is super important)
    ```
    $ python -m venv scraper-env
    $ source scraper-env/bin/activate
    ```
2. Install dependencies
    ```
    (scraper-env)$ pip install -r requirements.txt
    ```
    For development environment, use `requirements-dev.txt` instead
    ```
    (scraper-env)$ pip install -r requirements-dev.txt
    ```
3. Run spider
    ```
    (scraper-env)$ scrapy crawl books
    ```
    If you want to save the output to a file, use `-O` option
    ```
    (scraper-env)$ scrapy crawl books -O books.json
    ```

## Tests

The project uses [Scrapy Autounit](https://github.com/scrapinghub/scrapy-autounit/) to test the spiders. To execute the test, run the below command
```
(scraper-env)$ python -m unittest discover autounit/tests/
```
It also uses [coverage](https://github.com/nedbat/coveragepy) to identify the code coverage. To get coverage details, run the below commands
```
(scraper-env)$ coverage run -m unittest discover autounit/tests/
(scraper-env)$ coverage report
```

## Deployment

The spider can be deployed to zyte cloud using `shub`.

- To deploy for the first time
    ```
    (scraper-env)$ shub login
    ```
    Enter your API key when asked. After that run the following command
    ```
    (scraper-env)$ shub deploy <PROJECT ID>
    ```
- To deploy subsequent times
    ```
    (scraper-env)$ shub deploy
    ```

## Details

- The spider only goes through the category pages, and not through each individual book page, to save bandwidth.
- To identify specific CSS selector, inspect the HTML via browser inspector and fetch list of book, from categories pages.
- The spider fetches the following details corresponding to each book on the categories page
    - Book title
    - Book author
    - Book image URL
    - Book detail page URL
- The data has been kept in JSON format using the command above in [`books.json`](https://github.com/gutsytechster/books-scraper/blob/main/books.json) file.
- The spider is deployed on zyte cloud and can be accessed via following URL - https://app.zyte.com/p/524436/
