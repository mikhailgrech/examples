# tutorial: https://docs.scrapy.org/en/2.2/intro/tutorial.html

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "books"

    start_urls = [
        "http://books.toscrape.com/catalogue/page-1.html",
    ]

    def parse(self, response):
        book_page_links = response.css("ol li article.product_pod a::attr(href)").getall()
        yield from response.follow_all(book_page_links, self.parse_book)

        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_book(self, response):
        product_information = response.css("td::text").getall()

        yield {
            "title": response.css("h1::text").get(),
            "upc": product_information[0],
            "product_type": product_information[1],
            "price_excl_tax": product_information[2],
            "price_incl_tax": product_information[3],
            "tax": product_information[4],
            "availability": product_information[5],
            "number_of_reviews": product_information[6]
        }
