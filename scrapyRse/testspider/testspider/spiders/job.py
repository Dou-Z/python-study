import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class JobSpider(scrapy.Spider):
    name = 'job'
    allowed_domains = ['jd.com']
    start_urls = ['https://www.jd.com/']



    def parse(self, response):

        link = LinkExtractor(restrict_xpaths=r'//*[@id="J_cate"]/ul/li/a')
        result = link.extract_links(response)
        print(result[0])

        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()

