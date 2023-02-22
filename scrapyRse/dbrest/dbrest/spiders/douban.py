import scrapy


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://accounts.douban.com/j/mobile/login/basic']
                    # https://accounts.douban.com/j/mobile/login/basic

    def start_requests(self):
        headers = {
            'Host': 'accounts.douban.com',
            'Origin': 'https://accounts.douban.com',
            'Referer': 'https://accounts.douban.com/passport/login_popup?login_source=anony',
            'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
            # 'Cookie': 'll="118318"; bid=qUZ6rELVAgM; apiKey=; __utma=30149280.306821679.1626014732.1626014732.1626014732.1; __utmc=30149280; __utmz=30149280.1626014732.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=30149280.1.10.1626014732; login_start_time=1626014732840',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        params = {
            'ck': '',
            'remember':' true',
            'name':' 13193709088',
            'password':' dd13193709088',
            'ticket':'t03C-RucnJvf6ppsBbFbPJecAmF4xLjfx0WaSlloU9H3_oVom50J14EAH4sPnMRkEu3-qOMuGOjBZdPULXEGPGBAzt-I1_1blXnwfVTFD5Nvw34B3UKXNdpBFjGcCX7yzUx-cDrwT8DQFh9KTjV5ow9T05Hwln5RXVYP8hL186eOEE*',
            'randstr':'@MUr',
            'tc_app_id': '2044348370'
        }

        yield scrapy.FormRequest(
            url=self.start_urls[0],
            headers=headers,
            formdata=params,
            callback=self.parse
        )
    def parse(self, response):
        print(response.body.decode())
