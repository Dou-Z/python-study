import scrapy


class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com']
    start_urls = ['https://toy.jd.com/']

    def parse(self, response):
        print(response.xpath('//*[@id="toys_cms_fs_2"]/div/div[1]/div/div/text()').extract())
