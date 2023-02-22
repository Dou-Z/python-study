import requests, os
from urllib.parse import quote, unquote


# name = '爱情'
# print(quote(name))
# title = input('请输入贴吧名称：')
# page = input('你要多少页：')
# headers = {
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
# }
# for num in range(int(page)):
#     start_url = f'https://tieba.baidu.com/f?kw={quote(title)}&pn={50 * num}'
#     # join拼接
#     # start_url_1 = ''.join(['https://tieba.baidu.com/f?kw=',quote(title)])
#     # print(start_url)
#     response = requests.get(start_url,headers=headers)
#     data = response.content.decode()
#
#     with open(title + str(num) + '.html','w') as f:
#         f.write(data)
#     print(f'{title}----贴吧-----第{num+1}页保存完成')


class TbSpider(object):

    def __init__(self):
        self.title = input('请输入贴吧名称：')
        self.page = input('你要多少页：')
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
        }

    def parse_stat_url(self):
        """
        1.准备起始的url地址
        :return:
        """
        for num in range(int(self.page)):
            start_url = f'https://tieba.baidu.com/f?kw={quote(self.title)}&pn={50 * num}&utf-8'
            self.parse_requests(start_url, num)

    def parse_requests(self, start_url, num):
        """
        2.发送请求，获取响应
        :return:
        """
        response = requests.get(start_url, headers=self.headers)
        self.parse_response(response, num)

    def parse_response(self, response, num):
        """
        3.解析响应，数据提取
        :return:
        """
        data = response.content.decode()
        self.save_data(data, num)

    def save_data(self, data, num):
        """
        4.保存数据
        :return:
        """
        # os_path = r'D:\QQ 数据\python\\'
        os_path = os.getcwd() + f'/{self.title}/'  # 获取文件当前路径
        # 判断是否存在
        if not os.path.exists(os_path):
            os.mkdir(os_path)
        with open(os_path + self.title + '_' + str(num) + '.html', 'w', encoding='utf-8') as f:
            f.write(data)
        print(f'{self.title}----贴吧-----第{num + 1}页保存完成')


# if __name__ == '__main__':
#     bd = TbSpider()
#     bd.parse_stat_url()
from requests_html import HTMLSession
session = HTMLSession()

url = 'http://localhost:6800/schedule.json'
data = {
    'project':'py_a',
    'spider':'ace'
}
resp = requests.post(url,data=data)

print(resp.json())