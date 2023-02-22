# https://weibo.com/u/1751675285?refer_flag=0000015010_&from=feed&loc=avatar
# https://weibo.com/p/1003061751675285/info?mod=pedit_more
from requests_html import HTMLSession
from fake_useragent import UserAgent
import json
ua = UserAgent()
session = HTMLSession()

class WbSpider(object):
    def __init__(self):
        self.s_url = 'https://weibo.com/u/1751675285?refer_flag=0000015010_&from=feed&loc=avatar'
        self.headers = {
            'user-agent':ua.chrome,
            'cookie': 'SINAGLOBAL=6316313941499.581.1607865216322; UOR=,,login.sina.com.cn; Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c=1615339706,1615363149,1615427258,1615427271; SCF=AptQbON-bodM-kvUgZG4hsAi0JSz1u91rWVZE_Kj4r5pVH0p9Uflo-be93qQbQ4tGpwj1AUeV03jhbkqBBbQnmg.; login_sid_t=26cd7fa61ce8b00ee7041607a5280894; cross_origin_proto=SSL; _s_tentry=-; Apache=1127499497728.9321.1617157467511; ULV=1617157467520:8:6:2:1127499497728.9321.1617157467511:1617112086974; wb_view_log=1536*8641.25; SUB=_2A25NZ62qDeRhGeBN4lQU-C_JwzuIHXVuFJhirDV8PUNbmtAKLWXmkW9NRBtERW5rHOqeXxhZ_k5ZJkkUdgO-ahf2; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W52Xn-F5iO0-JDy9WHPWC5-5JpX5KzhUgL.Foq01Kqf1h2f1hM2dJLoIEBLxKML1K-LB-2LxKnL12eL1hBLxK-L1K2L1h5LxK-L1K-L122t; ALF=1648693626; SSOLoginState=1617157626; wvr=6; wb_view_log_6396581587=1536*8641.25; webim_unReadCount=%7B%22time%22%3A1617177636573%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A9%2C%22msgbox%22%3A0%7D',
            'upgrade-insecure-requests':'1',


        }
        self.data = {
            'mod': 'pedit_more',
        }
    def start_resquest(self):
        resp_1 = session.get(self.s_url,headers=self.headers)
        data1 = resp_1.html.xpath('//*[@id="Pl_Official_PersonalInfo__56"]/div[1]/div/div[2]/div/ul/li[5]/span[2]/cjktext/text()')
        print(data1)


if __name__ == '__main__':
    W = WbSpider()
    W.start_resquest()