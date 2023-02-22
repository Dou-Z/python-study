
# https://web-drcn.hispace.dbankcloud.cn/uowap/index?method=internal.user.commenList3&serviceType=20&reqPageNum=3&maxResults=25&appid=C10652857&version=10.0.0&zone=&locale=zh
# https://web-drcn.hispace.dbankcloud.cn/uowap/index?method=internal.user.commenList3&serviceType=20&reqPageNum=1&maxResults=25&appid=C10652857&version=10.0.0&zone=&locale=zh
from requests_html import HTMLSession
from fake_useragent import UserAgent
from jsonpath import jsonpath
ua = UserAgent()
session = HTMLSession()

class DyAppSpider(object):
    def __init__(self):
        for i in range(1,10):
            s_url = f'https://web-drcn.hispace.dbankcloud.cn/uowap/index?method=internal.user.commenList3&serviceType=20&reqPageNum={i}&maxResults=25&appid=C10652857&version=10.0.0&zone=&locale=zh'
            self.headers = {
                'Referer': 'https://appgallery.huawei.com/',
                'User-Agent':ua.chrome,
                'Host': 'web-drcn.hispace.dbankcloud.cn',
                'Origin': 'https://appgallery.huawei.com'
            }
            self.data = {
                'method': 'internal.user.commenList3',
                'serviceType': '20',
                'reqPageNum': i,
                'maxResults': '25',
                'appid': 'C10652857',
                'version': '10.0.0',
                'zone': '',
                'locale': 'zh',

            }
            self.start_requests(s_url,i)
    def start_requests(self,s_url,i):
        resp_1 = session.get(s_url,headers=self.headers,data=self.data)
        ccode = resp_1.status_code
        # print(resp_1.content.decode(),'================================================',i)
        L_data = jsonpath(resp_1.json(),'$..accountName')
        print(ccode,L_data,'=================',i,'\n',s_url)






if __name__ == '__main__':
    D = DyAppSpider()
    D.start_requests()


"""
method: internal.user.commenList3
serviceType: 20
reqPageNum: 1
maxResults: 25
appid: C10652857
version: 10.0.0
zone: 
locale: zh
"""