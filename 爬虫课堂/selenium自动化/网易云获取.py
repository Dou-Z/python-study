# https://music.163.com/
from selenium import webdriver
from lxml import etree
import time, random,re


class WYSpider(object):
    driver = webdriver.Chrome()

    def __init__(self):
        self.surl = 'https://music.163.com/'

    def parse_s_url(self):
        """
        解析其实URL地址
        :return:
        """
        self.driver.get(self.surl)
        self.driver.implicitly_wait(10)

        el_ifarm = self.driver.find_element_by_tag_name('iframe')
        self.driver.switch_to.frame(el_ifarm)
        next_url = self.driver.find_element_by_class_name('s-fc3').get_attribute('href')
        time.sleep(random.randint(1, 3))
        self.parse_n_url_resp(next_url)

    def parse_n_url_resp(self, next_url):
        """
        解析所有分类列表
        :param next_url: 分类列表
        :return:
        """

        js = 'window.open("{}")'.format(next_url)
        self.driver.execute_script(js)
        # 获取所有窗口
        win = self.driver.window_handles
        # 窗口切换
        self.driver.switch_to.window(win[0])
        self.driver.close()
        self.driver.switch_to.window(win[1])
        self.parse_page_info()

    def parse_page_info(self):
        el_iframe = self.driver.find_element_by_tag_name('iframe')
        self.driver.switch_to.frame(el_iframe)
        time.sleep(random.randint(1,3))
        num_list = self.driver.find_elements_by_xpath('//*[@id="m-pl-container"]/li/div/a')
        # print(len(num))
        num = len(num_list)
        for p in range(1,num+1):
            self.parse_click(p)
        self.parse_next_page()


    def parse_click(self,p):
        """
        解析歌单详细数据
        :param p: 歌单标签所在位置
        :return:
        """
        self.driver.find_element_by_xpath(f'//*[@id="m-pl-container"]/li[{p}]/div/a').click()
        time.sleep(random.randint(1, 3))
        # 获取源码
        html_two_str = self.driver.page_source
        # html_str = re.findall('<iframe.*?/iframe>',html_two_str)
        # print(html_two_str)

        html = etree.HTML(html_two_str)
        url_list = html.xpath('//tr/td[2]/div/div/div/span/a/@href')
        title_list = html.xpath('//tr/td[2]/div/div/div/span/a/b/@title')
        print()
        self.parse_data(url_list,title_list)

    def parse_data(self,url_list,title_list):
        """
        解析歌曲
        :param url_list:
        :param title_list:
        :return:
        """
        print(url_list,title_list)
        self.driver.back()
        el_ifarm = self.driver.find_element_by_tag_name('iframe')
        self.driver.switch_to.frame(el_ifarm)
        time.sleep(random.randint(1, 3))

    def parse_next_page(self):
        """
        执行翻页
        :return:

        """
        el_ifarm = self.driver.find_element_by_tag_name('iframe')
        self.driver.switch_to.frame(el_ifarm)
        a = self.driver.find_element_by_xpath('//*[@id="m-pl-pager"]/div/a[last()]').get_attribute('href')
        if a == 'javascript:void(0)':
            return '程序终止'
        else:
            # self.driver.find_element_by_xpath('//*[@id="m-pl-pager"]/div/a[last()]').click()
            js = 'document.querySelector("#m-pl-pager > div > a.zbtn.znxt").click()'
            self.driver.execute_script(js)
            time.sleep(random.randint(1, 3))
            self.parse_page_info()



# http://m801.music.126.net/20210409142155/a2124f1dddd21e698d8f9a17e27d5387/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/7937683494/31e2/2771/3eef/e1a6f0f79db893a61118d620b204384f.m4a
# http://m10.music.126.net/20210409201219/86033d9c612d4dbd36756a09d225ab97/yyaac/obj/wonDkMOGw6XDiTHCmMOi/1901983001/9280/1335/eb55/67f045f3bc261fb6a686edc2ccc671bd.m4a
# http://m701.music.126.net/20210409201537/216d1ea6c0b86324245f560bc8f13dbe/jdyyaac/015e/0e5b/070e/6417e632389149c515540ddb7ff341c8.m4a


if __name__ == '__main__':
    w = WYSpider()
    w.parse_s_url()


# https://music.163.com/#/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0

# q_url = "https://music.163.com/#/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0"
# driver = webdriver.Chrome()
#
# driver.get(q_url)
# driver.implicitly_wait(10)
#
# el_ifarm = driver.find_element_by_tag_name('iframe')
# driver.switch_to.frame(el_ifarm)
# time.sleep(4)
# js = 'scrollTo(0,2000)'
# driver.execute_script(js)
# time.sleep(2)
# # driver.find_element_by_xpath('//*[@id="m-pl-pager"]/div/a[11]').click()
# # driver.find_element_by_class_name('zbtn znxt').click()
# # driver.find_element_by_link_text('下一页').click()
# """js翻页"""
# js = 'document.querySelector("#m-pl-pager > div > a.zbtn.znxt").click()'
# driver.execute_script(js)
