
import scrapy


class tutorialSpider(scrapy.Spider):
    name = "tutorial"
    start_urls = [
        "https://listado.mercadolibre.com.pe/g502"
    ]

    def parse(self, response):
        yield {
            "precio": response.xpath('//span[@class="andes-money-amount__fraction"]/text()').getall(),
            "titulo": response.xpath('//h2[@class="ui-search-item__title shops__item-title"]/text()').getall(),
        }

