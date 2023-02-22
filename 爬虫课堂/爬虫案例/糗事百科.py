# coding=utf-8
import requests
from lxml import etree
from queue import Queue
from multiprocessing.dummy import Pool
import time


class QiubaiSpider:
    def __init__(self):
        self.url_temp = "https://www.qiushibaike.com/8hr/page/{}/"
        self.headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X \
        10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"}
        self.queue = Queue()
        self.pool = Pool(5)
        self.is_running = True
        self.total_requests_num = 0
        self.total_response_num = 0

    def get_url_list(self):  # 获取url列表
        for i in range(1, 14):
            self.queue.put(self.url_temp.format(i))
            self.total_requests_num += 1

    def parse_url(self, url):  # 发送请求，获取响应
        return requests.get(url, headers=self.headers).content.decode()

    def get_content_list(self, html_str):  # 提取段子
        html = etree.HTML(html_str)
        div_list = html.xpath("//div[@id='content-left']/div")
        content_list = []
        for div in div_list:
            content = {}
            content["content"] = div.xpath(".//div[@class='content']/span/text()")
            print(content)
            content_list.append(content)
        return content_list

    def save_content_list(self, content_list):  # 保存数据
        print(content_list)
        pass

    def exetute_requests_item_save(self):
        url = self.queue.get()
        html_str = self.parse_url(url)
        content_list = self.get_content_list(html_str)
        self.save_content_list(content_list)
        self.total_response_num += 1

    def _callback(self, temp):
        if self.is_running:
            self.pool.apply_async(self.exetute_requests_item_save, callback=self._callback)

    def run(self):
        self.get_url_list()

        for i in range(2):  # 控制并发
            self.pool.apply_async(self.exetute_requests_item_save, callback=self._callback)

        while True:  # 防止主线程结束
            time.sleep(0.0001)  # 避免cpu空转，浪费资源
            if self.total_response_num >= self.total_requests_num:
                self.is_running = False
                break


if __name__ == '__main__':
    qiubai = QiubaiSpider()
    qiubai.run()