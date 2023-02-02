import scrapy
from scrapy.crawler import CrawlerProcess


class Tonepedia(scrapy.Spider):
    name = "tonepedia"
    allowed_domains = ["tonepedia.com"]
    custom_settings = {
        "FEEDS": {
            "data/results.json": {
                "format": "jsonlines",
                "encoding": "utf8",
                "indent": 4,
                "overwrite": True,
            }
        },
        "DEPTH_LIMIT": 2,
        "DOWNLOAD_DELAY": 1,
    }

    with open("data/urls.txt", "r", encoding="utf8") as f:
        start_urls = f.readlines()

    def parse(self, response):
        self.logger.info("A response from %s just arrived!", response.url)

        # Pedal name
        pedal_name = response.xpath(
            '//h1[@class="product_title entry-title elementor-heading-title elementor-size-default"]/text()'
        ).get()

        # pedal description
        pedal_des = response.xpath(
            '//div[@class="elementor-widget-container"]/p/b/text()'
        ).get()

        # pedal info
        pedal_info = response.xpath(
            '//div[@class="elementor-widget-container"]/p/text()'
        ).get()

        # pedal specs
        attr_names = response.xpath(
            '//div[@class="elementor-widget-container"]//td[@class="attr-name"]/text()'
        ).getall()
        attr_values = response.xpath(
            '//div[@class="elementor-widget-container"]//td[@class="attr-val"]/text()'
        ).getall()
        pedal_specs = {a: b for a, b in zip(attr_names, attr_values)}

        # save data
        yield {"url": response.url, "name": pedal_name, "specs": pedal_specs}


def main():
    process = CrawlerProcess()
    process.crawl(Tonepedia)
    process.start()


if __name__ == "__main__":
    main()
