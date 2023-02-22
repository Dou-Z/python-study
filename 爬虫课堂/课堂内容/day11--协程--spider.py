"""协程：greenlet   安装：pip install greenlet"""
from greenlet import greenlet
import time


def test1():
    while True:
        print("---A--")
        gr2.switch()
        time.sleep(3)

def test2():
    for i in range(5):
        print("---B--")
        gr1.switch()
        time.sleep(0.5)


gr1 = greenlet(test1)
gr2 = greenlet(test2)

# 切换到gr1中运行
# gr2.switch()

# 生成器
def index():
    for i in range(5):
        yield i

f = index()
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())

# 迭代器
list_1 = [1,2,3,4,5,6]
# 创建可迭代对象
list_result = iter(list_1)

print(next(list_result))
print(next(list_result))
print(next(list_result))
from queue import Queue

"""区别：迭代器是生成器的一种，迭代器能够完成所有生成器的功能"""

"""协程：gevent  操作二"""
# import gevent
# import time
# from gevent import monkey
# 只要有延迟，先执行下一步
# monkey.patch_all()
#
#
# def kang():
#     for i in range(5):
#         print(i)
#         # time.sleep(1)
#
#
# def dong(url):
#     print(url)
#     time.sleep(2)
#
#
# if __name__ == "__main__":
#     for i in range(5):
#         # 给协程下达任务
#         g1 = gevent.spawn(kang)
#         g2 = gevent.spawn(dong, 5)
#         print("kangdong")


"""协程池操作"""
'''
由于gevent的Pool的没有close方法，也没有异常回调参数
引出需要对gevent的Pool进行一些处理，实现与线程池一样接口，实现线程和协程的无缝转换
'''

# import random
# num = random.randint(1,100)
# running = True
#
# while running:
#     answer = int(input('guess(1-100):'))
#     if answer > num:
#         print("猜大了")
#     elif answer < num:
#          print("猜小了")
#     else:
#         print("猜对了")
#         running =False


"""去哪网爬虫案例"""

# https://travel.qunar.com/travelbook/list.htm?order=hot_heat#
# https://travel.qunar.com/travelbook/list.htm?page=2&order=hot_heat
# 详情页
# https://travel.qunar.com/travelbook/note/7662221
# https://travel.qunar.com/travelbook/note/7662064


import os, xlwt, xlrd

from xlutils.copy import copy
from requests_html import HTMLSession
from fake_useragent import UserAgent

session = HTMLSession()
ua = UserAgent()


class LYSpider(object):
    def __init__(self):
        self.start_url = 'https://travel.qunar.com/travelbook/list.htm?page={}&order=hot_heat'


    def parse_start_url(self):
        for i in range(1, 201):
            start_url = self.start_url.format(i)
            # print(start_url)
            print(f'开始爬取第{i}页游记======Writing!!!!=====')
            self.response_data(start_url)
            print(f'第{i}页爬完======Well!!!======')
            # break

    def response_data(self, start_url):
        """
        获取响应
        :param start_url:
        :return:
        """
        headers = {
            'user-agent': ua.chrome,
            'upgrade-insecure-requests': '1',
        }
        response = session.get(start_url,headers=headers)
        if response.status_code != 200:
            self.response_data(start_url)
        # print(response.content.decode())
        for j in range(1, 11):
            # 游记标题
            title = response.html.xpath(f'/html/body/div[2]/div/div[2]/ul/li[{j}]/h2/a/text()')
            title = ''.join(title)
            # 详情页ID
            yj_id = response.html.xpath(f'/html/body/div[2]/div/div[2]/ul/li[{j}]/h2/@data-bookid')
            yj_id = ''.join(yj_id)
            # 小详情
            # 天数
            yj_days = response.html.xpath(f'/html/body/div[2]/div/div[2]/ul/li[{j}]/p[1]/span[1]/span[3]/text()')
            yj_days = ''.join(yj_days)
            # 游记人物
            yj_people = response.html.xpath(
                f'/html/body/div[2]/div/div[2]/ul/li[{j}]/p[1]/span[1]/span[5][@class="people"]/text()')
            #
            yj_people = ''.join(yj_people)
            # 游记方式
            yj_ways = response.html.xpath(f'/html/body/div[2]/div/div[2]/ul/li[{j}]/p[1]/span[1]/span[6]/text()')
            yj_ways = ' '.join(yj_ways)
            # if yj_ways == '':
            #     yj_ways = response.html.xpath('//li[5]/p[1]/span[1]/span[5][@class="trip"]/text()')
            # 途径
            yj_didian = response.html.xpath(f'/html/body/div[2]/div/div[2]/ul/li[{j}]/p[2]/text()')
            yj_didian = '>'.join(yj_didian)[3:]
            if yj_didian == '':
                yj_didian = '不重要'

            # 人均价格
            ave_price = response.html.xpath(f'//li[{j}]/p/span/span[@class="fee"]/text()')
            ave_price = ''.join(ave_price)
            if ave_price == '':
                ave_price = '无数据'
            # 行程：
            yj_line = response.html.xpath(f'/html/body/div[2]/div/div[2]/ul/li[{j}]/p[3]/text()')
            yj_line = '>'.join(yj_line)[3:]
            if yj_line == '':
                 yj_line = '无'

            dict_1 = {
                '游记标题': title,
                '游记ID': yj_id,
                '天数': yj_days,
                '游记人物/方式': yj_people + '  ' + yj_ways,
                '人均价格': ave_price,
                '途径': yj_didian,
                '行程': yj_line
            }

            # print(dict_1)
            data = {
                '游记详情': [title, yj_id, yj_days, yj_people + '  ' + yj_ways, ave_price, yj_didian, yj_line]
            }
        # print(f'保存游记=====loading=====')
            self.save_excel(data)

    def save_excel(self, data):
        # data = {
        #     '基本详情': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        # }
        os_path_1 = os.getcwd() + '/数据/'
        if not os.path.exists(os_path_1):
            os.mkdir(os_path_1)
        # os_path = os_path_1 + self.os_path_name + '.xls'
        os_path = os_path_1 + '去哪儿数据.xls'
        if not os.path.exists(os_path):
            # 创建新的workbook（其实就是创建新的excel）
            workbook = xlwt.Workbook(encoding='utf-8')
            # 创建新的sheet表
            worksheet1 = workbook.add_sheet("游记详情", cell_overwrite_ok=True)
            borders = xlwt.Borders()  # Create Borders
            """定义边框实线"""
            borders.left = xlwt.Borders.THIN
            borders.right = xlwt.Borders.THIN
            borders.top = xlwt.Borders.THIN
            borders.bottom = xlwt.Borders.THIN
            borders.left_colour = 0x40
            borders.right_colour = 0x40
            borders.top_colour = 0x40
            borders.bottom_colour = 0x40
            style = xlwt.XFStyle()  # Create Style
            style.borders = borders  # Add Borders to Style
            """居中写入设置"""
            al = xlwt.Alignment()
            al.horz = 0x02  # 水平居中
            al.vert = 0x01  # 垂直居中
            style.alignment = al
            # 合并 第0行到第0列 的 第0列到第13列
            '''基本详情13'''
            # worksheet1.write_merge(0, 0, 0, 13, '基本详情', style)
            excel_data_1 = ('游记标题', '游记ID', '天数', '游记人物/方式', '人均价格', '途径', '行程',
                            )
            for i in range(0, len(excel_data_1)):
                worksheet1.col(i).width = 2560 * 3
                #               行，列，  内容，            样式
                worksheet1.write(0, i, excel_data_1[i], style)
            workbook.save(os_path)
        # 判断工作表是否存在
        if os.path.exists(os_path):
            # 打开工作薄
            workbook = xlrd.open_workbook(os_path)
            # 获取工作薄中所有表的个数
            sheets = workbook.sheet_names()
            for i in range(len(sheets)):
                for name in data.keys():
                    worksheet = workbook.sheet_by_name(sheets[i])
                    # 获取工作薄中所有表中的表名与数据名对比
                    if worksheet.name == name:
                        # 获取表中已存在的行数
                        rows_old = worksheet.nrows
                        # 将xlrd对象拷贝转化为xlwt对象
                        new_workbook = copy(workbook)
                        # 获取转化后的工作薄中的第i张表
                        new_worksheet = new_workbook.get_sheet(i)
                        for num in range(0, len(data[name])):
                            new_worksheet.write(rows_old, num, data[name][num])
                        new_workbook.save(os_path)


# if __name__ == '__main__':
#     ly = LYSpider()
    # ly.parse_start_url()
