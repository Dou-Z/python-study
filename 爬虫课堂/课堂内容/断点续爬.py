from requests_html import HTMLSession
from fake_useragent import UserAgent
from jsonpath import jsonpath
from multiprocessing import Pool
import time
import os,json,re

ua = UserAgent()
session = HTMLSession()


class WZRYspider(object):
    def __init__(self):
        self.surl = 'https://pvp.qq.com/web201605/js/herolist.json'
        self.headers = {
            'referer': 'https://pvp.qq.com/web201605/herolist.shtml',
            'user-agent': ua.chrome,
        }
    def if_file(self,ename_list,cname_list):
        if not os.path.exists('./王者日志.log'):
            print('没有发现日志')
            self.response_data(ename_list, cname_list)
        else:
            print('开始读取日志==========logging=====')
            with open('./王者日志.log','r')as f:
                f_data = f.read()
                data = re.findall('\d*,.*?,\d',f_data)
                #re.findall("[\u4e00-\u9fa5]+"
                # cname = re.findall("[\u4e00-\u9fa5]+",data[-1])[0]
                # i = data[-1][-1]
                # ename = data[-1][0:3]
                # print(data[-1][0:3])
                # print(cname)
                # print(len(data))
                ename_list = ename_list[len(data):]
                cname_list = cname_list[len(data):]
                # print(ename_list,cname_list)
                self.response_data(ename_list,cname_list)

    def start_spider(self):
        response = session.get(self.surl, headers=self.headers).json()
        ename_list = jsonpath(response, '$..ename')
        cname_list = jsonpath(response, '$..cname')
        # print(response)
        # print(ename,cname)
        self.if_file(ename_list, cname_list)

    def response_data(self, ename_list, cname_list):
        for ename, cname in zip(ename_list, cname_list):
            i = 1
            while True:
                nurl = f'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{ename}/{ename}-bigskin-{i}.jpg'

                resp_img = session.get(nurl)
                if resp_img.status_code != 200:
                    break

                img = resp_img.content
                os_path = './王者荣耀img_last_1/'
                if not os.path.exists(os_path):
                    os.mkdir(os_path)
                with open(os_path + str(cname) +str(i) + '.jpg', 'wb')as f:
                    f.write(img)
                    print(f'============={cname}第{i}张下载完成=========')


                # data = {
                #     'ename_list': ename,
                #     'cname_list': cname,
                #     'nurl': nurl,
                # }
                if not os.path.exists('./王者日志.log'):
                    with open('./王者日志.log','w')as f:
                        # json.dump(data,f)
                        f.write(str(ename) + ',')
                        f.write(str(cname) + str(i) + '\n')
                    print('日志记录完成 ===========logging=======')
                else:
                    print('开始更新日志数据 =========logging===========')
                    with open('./王者日志.log','r')as r:
                        r_data = r.read()
                    # print(r_data)
                    with open('./王者日志.log','a+')as f:
                        f.write(str(ename) + ',')
                        f.write(str(cname) + ',' + str(i) + '\n')
                    print('日志记录更新完成 ========logging=======')
                i += 1


    # def run(self):
        # pool = Pool(3)
        # while True:
        #     pool.apply_async(self.start_spider)
        #
        # pool.close()
        # pool.join()

if __name__ == '__main__':
    w = WZRYspider()
    w.start_spider()