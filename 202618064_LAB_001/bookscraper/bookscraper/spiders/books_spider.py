import scrapy


class BookSpider(scrapy.Spider):
    # Scrapy already provides a base Spider class with crawling functionality.
    name = "books"

    # List of pages where the spider starts crawling
    start_urls = [
        "https://books.toscrape.com/catalogue/page-20.html",
        "https://books.toscrape.com/catalogue/page-21.html",
        "https://books.toscrape.com/catalogue/page-22.html",
        "https://books.toscrape.com/catalogue/page-23.html",
        "https://books.toscrape.com/catalogue/page-24.html",
        "https://books.toscrape.com/catalogue/page-25.html",
    ]

    def parse(self, response):
        books = response.css("article.product_pod")

        for book in books:
            title = book.css("h3 a::attr(title)").get()

            price = book.css("p.price_color::text").get()

            rating = (
                book.css("p.star-rating::attr(class)")
                .get()
                .replace("star-rating ", "")
            )

            availability = book.css("p.instock.availability::text").getall()
            availability = "".join(availability).strip()

            product_url = response.urljoin(
                book.css("h3 a::attr(href)").get()
            )

            yield response.follow(
                product_url,
                callback=self.parse_book,
                meta={
                    "title": title,
                    "price": price,
                    "rating": rating,
                    "availability": availability,
                    "product_url": product_url,
                },
            )

    def parse_book(self, response):

        upc = response.css("table tr:nth-child(1) td::text").get()

        category = response.css(
            "ul.breadcrumb li:nth-child(3) a::text"
        ).get()

        description = response.css(
            "#product_description + p::text"
        ).get()

        reviews = response.css(
            "table tr:nth-child(7) td::text"
        ).get()

        yield {
            "Title": response.meta["title"],
            "Category": category,
            "Price": response.meta["price"],
            "Rating": response.meta["rating"],
            "Availability": response.meta["availability"],
            "Description": description,
            "UPC": upc,
            "Number_of_Reviews": reviews,
            "Product_URL": response.meta["product_url"],
        }

         # python dict key value pair 
# parse() → catalog pages.
# parse_book() → individual book pages.
# yeild is a way of saying spidey Visit another page