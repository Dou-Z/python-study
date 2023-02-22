# //game.gtimg.cn/images/yxzj/img201606/heroimg/505/505-smallskin-3.jpg
# //game.gtimg.cn/images/yxzj/img201606/heroimg/505/505-smallskin-2.jpg

#  surl = '//game.gtimg.cn/images/yxzj/img201606/heroimg/' + ename + '/' + ename,
#  burl = "//game.gtimg.cn/images/yxzj/img201606/skin/hero-info/" + ename + '/' + ename,
# https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/505/505-smallskin-2.jpg

# //game.gtimg.cn/images/yxzj/img201606/heroimg/'+ heroid + '/'+ heroid +'-myskin-'+ skinid +'.jpg'
# 小壁纸（170*240）
# //game.gtimg.cn/images/yxzj/img201606/heroimg/505/505-myskin-2.jpg
# 中型壁纸（600*410）
# //game.gtimg.cn/images/yxzj/img201606/heroimg/505/505-mobileskin-1.jpg
# 大壁纸（1920*882）
# //game.gtimg.cn/images/yxzj/img201606/skin/hero-info/505/505-bigskin-1.jpg


# https://pvp.qq.com/web201605/js/herolist.json

# from requests_html import HTMLSession
# from fake_useragent import UserAgent
# from jsonpath import jsonpath
# from multiprocessing import Pool
# import time
# import os
#
# ua = UserAgent()
# session = HTMLSession()
#
#
# class WZRYspider(object):
#     def __init__(self):
#         self.surl = 'https://pvp.qq.com/web201605/js/herolist.json'
#         self.headers = {
#             'referer': 'https://pvp.qq.com/web201605/herolist.shtml',
#             'user-agent': ua.chrome,
#         }
#
#     def start_spider(self):
#         response = session.get(self.surl, headers=self.headers).json()
#         ename_list = jsonpath(response, '$..ename')
#         cname_list = jsonpath(response, '$..cname')
#         # print(response)
#         # print(ename,cname)
#         self.response_data(ename_list, cname_list)
#
#     def response_data(self, ename_list, cname_list):
#         for ename, cname in zip(ename_list, cname_list):
#             i = 1
#             while True:
#                 nurl = f'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{ename}/{ename}-bigskin-{i}.jpg'
#                 resp_img = session.get(nurl)
#                 if resp_img.status_code != 200:
#                     break
#
#                 img = resp_img.content
#                 os_path = './王者荣耀img_1/'
#                 if not os.path.exists(os_path):
#                     os.mkdir(os_path)
#                 with open(os_path + str(cname) +str(i) + '.jpg', 'wb')as f:
#                     f.write(img)
#                     print(f'============={cname}第{i}张下载完成=========')
#                     i += 1
#
#     def run(self):
#         pool = Pool(3)
#         while True:
#             pool.apply_async(self.start_spider)
#
#         pool.close()
#         pool.join()
#
# if __name__ == '__main__':
#     w = WZRYspider()
#     w.run()

# import js2py
# # 创建js执行环境
# js = js2py.EvalJs()
# with open('baidu.js','r')as f:
#     js_demo = f.read()
# js.execute(js_demo)
# str_title = input('请输入你需要翻译的文字：')
# res = js.e(str_title)
# print(res)

"""有误代码"""
# res = js2py.eval_js(js_demo)
# js_data = '我爱你'
# # print(res.e(js_data))
# print(js_demo)

import js2py
# 1.创建js的执行环境
js = js2py.EvalJs()
# 从js文件中加载
# water.js是保存的js加密，解密流程代码
with open('baidu.js', 'r', encoding='utf-8')as f:
    js.execute(f.read())
# 传入被加密数据  resultDecod是js代码里面定义的方法
js_data = '美女'
b = js.e(js_data)
print(b)

import execjs

with open("baidu.js", "r") as f:
     ctx = execjs.compile(f.read())
# 调用在js中定义的resultDecode方法，传入我们的js_data
js_data = '我爱你'
data = ctx.call("e", js_data)
print(data)