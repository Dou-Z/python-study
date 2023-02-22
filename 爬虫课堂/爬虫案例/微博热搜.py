import requests
# 解析库  xpath  解析数据
from lxml import etree
from urllib.parse import unquote
# csv 保存数据   保存为表格的形式
import csv

"""
序号  标题  热度   链接

"""


# 1.目标url
url = "https://s.weibo.com/top/summary?cate=realtimehot"

# 2.发送请求   解码
data = requests.get(url).content.decode()


# 数据转换  转换成xpath能够操作的数据
html = etree.HTML(data)

# 3.解析数据   xpath 取出来的数据类型是列表
# 排名
rank = html.xpath('//td[@class="td-01 ranktop"]/text()')

# 热搜事件
affair = html.xpath('//td[@class="td-02"]/a/text()')
affair.pop(0)

# 热度
view = html.xpath('//td[@class="td-02"]/span/text()')
# 链接    干扰数据
link = html.xpath('//tr/td/a/@href')
link_try = html.xpath('//tr/td/a/@href_to')
link.pop(0)
# 处理数据
index = 0
for i, sku in enumerate(link):
    if sku == "javascript:void(0);":
        link[i] = link_try[index]
        index += 1


# 4.保存数据   保存为表格
with open('weibo1.csv', 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    # 定义表头
    writer.writerow(['排名', '事件', '热度','链接'])
    # 循环依次保存数据
    for i, rank in enumerate(rank):
        writer.writerow([rank, affair[i], view[i], 'https://s.weibo.com/' + link[i]])
    print('保存完成')