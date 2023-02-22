# 豆瓣电影250
# https://movie.douban.com/top250
#  start 翻页
# https://movie.douban.com/top250?start=25&filter=
# from pymongo import MongoClient
#
# clien = MongoClient('127.0.0.1',27017)
# db = clien['douban']['movies']
#
# from requests_html import HTMLSession
# from fake_useragent import UserAgent
# import re
# ua = UserAgent()
# session = HTMLSession()
# for i in range(10):
#     s_url =f'https://movie.douban.com/top250?start={i * 25}&filter='
#     resp_1 = session.get(s_url).html
#     vname = resp_1.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[1]/text()')
#     vdetil = resp_1.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/p[2]/span/text()')
#     # print(vname,vdetil)
#     for m,j in zip(vname,vdetil):
#         data = {}
#         data['电影名'] = m
#         data['电影名言'] = j
#         db.insert_one(data)
#     print(f'第{i}页保存完成')
