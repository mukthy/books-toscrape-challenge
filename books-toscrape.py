import scrapy


class BooksToScrapeSpider(scrapy.Spider):
    name = 'books-toscrape'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']
    base_url = 'http://books.toscrape.com/'

    custom_settings = {

    'AUTOTHROTTLE_ENABLED': True,
    'HTTPCACHE_ENABLED': True,
    }

    def parse(self, response):
        all_books = response.xpath('.//article[@class="product_pod"]')
        for book in all_books:
            book_url = book.xpath('.//h3/a/@href').extract_first()
            if 'catalogue/' not in book_url:
                book_url = 'catalogue/' + book_url

            book_url = self.base_url + book_url

            title = book.xpath('.//h3/a/@title').extract_first()
            price = book.xpath('.//div/p[@class="price_color"]/text()').extract_first()
            partial_image_url = book.xpath('.//div[@class="image_container"]/a/img/@src').extract_first()
            image_url = self.base_url + partial_image_url.replace('../','')

            yield {
                'Title': title,
                'Price': price,
                'Image URL': image_url,
                'Book URL': book_url,
            }

        next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page_url:
            if 'catalogue/' not in next_page_url:
                next_page_url = "catalogue/" + next_page_url

            next_page = self.base_url + next_page_url
            yield scrapy.Request(next_page, callback=self.parse)