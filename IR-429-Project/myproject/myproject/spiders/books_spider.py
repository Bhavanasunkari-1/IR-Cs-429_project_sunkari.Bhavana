import scrapy
class BooksSpiderSpider(scrapy.Spider):
    name = "books_spider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        for product in response.css('article.product_pod'):
            title = product.css('h3 > a::attr(title)').get()
            price = product.css('.price_color::text').get()

            yield {
                'title': title,
                'price': price
            }
