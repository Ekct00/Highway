import scrapy
from driveFaster.items import DrivefasterItem


class CarSpider(scrapy.Spider):
    name = "car"
    key = "藤浦めぐ"
    page_number = 4
    url = []
    allow_domains = ["torrentkitty.tv"]

    for i in range(0,page_number):
        url.append("https://www.torrentkitty.tv/search/" + key + "/" + str(i + 1))

    start_urls = url

    def parse(self, response):
        for sel in response.xpath('//body'):
            item = DrivefasterItem()
            try:
                item['link'] = sel.xpath('//a[@rel="magnet"]/@href').extract()
            except:
                item['link'] = 'none'
            yield item