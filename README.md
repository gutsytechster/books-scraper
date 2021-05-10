# Books Scraper
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
    If you want to save the output to a file, use `-o` option
    ```
    (scraper-env)$ scrapy crawl books -o books.json
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
- The data is kept in JSON format using the command above in [`books.json`](https://github.com/gutsytechster/books-scraper/blob/main/books.json) file.
- The spider is deployed on zyte cloud and can be accessed via following URL - https://app.zyte.com/p/524436/
