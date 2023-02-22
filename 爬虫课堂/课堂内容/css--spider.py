# CSS???
# from fake_useragent import UserAgent
# from requests_html import HTMLSession
# session = HTMLSession()
# # ua??
# ua = UserAgent()
# url = 'https://www.CSDN.net'
#
# response = session.get(url)
# # first=True ????
# data = response.html.find('#floor-nav_62 > div > div > div.index_nav_center > ul > li:nth-child(11) > a',first=True)
# # ??????
# print(data.text)
# # ????????????
# print(data.attrs)
# # ??????
# print(data.links)


# https://zz.newhouse.fang.com/house/s/
# https://zz.newhouse.fang.com/loupan/2510148677.htm  ???
# https://zz.newhouse.fang.com/loupan/2510148677/housedetail.htm

# https://zz.newhouse.fang.com/loupan/2510149275.htm  ??·??
# https://zz.newhouse.fang.com/loupan/2510149275/housedetail.htm ???
#       //zz.newhouse.fang.com/loupan/2510149583.htm

from requests_html import HTMLSession
from fake_useragent import UserAgent
from lxml import etree
import re
import re

ua = UserAgent()
session = HTMLSession()
start_url = 'https://zz.newhouse.fang.com/house/s/'
headers = {

    'origin': 'https://zz.newhouse.fang.com',
    'referer': 'https://zz.newhouse.fang.com/house/s/',
    'cookie': 'city=zz; global_cookie=nsjk0wjl1x1vnu2b1f79i9a0k17km8q8jec; searchConN=1_1615700410_867%5B%3A%7C%40%7C%3A%5D6be2d74d43d38bf7844fdb6c396f8578; Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c=1615700411; __utma=147393320.420763440.1615700411.1615700411.1615700411.1; __utmc=147393320; __utmz=147393320.1615700411.1.1.utmcsr=zz.fang.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt_t0=1; __utmt_t1=1; __utmt_t2=1; __utmt_t3=1; __utmt_t4=1; showCity=; csrfToken=MCzT2Am69n22aV_72GO6LQWA; unique_cookie=U_nsjk0wjl1x1vnu2b1f79i9a0k17km8q8jec*6; Hm_lpvt_eaa57ca47dacb4ad4f5a257001a3457c=1615700532; __utmb=147393320.25.10.1615700411; g_sourcepage=xf_lp%5Elb_pc',
    'user-agent': ua.chrome,
}

response_start = session.post(start_url, headers=headers)
# rep = response.html.html
# ???? xpath(//*[@class="nlc_img"]/a/img[2]/@alt)
lp_name = response_start.html.xpath('//*[@class="nlc_img"]/a/img[2]/@alt')
print(lp_name)
# ??ID xpath(//*[@class="nlc_img"]/a/@href)
lp_id = response_start.html.xpath('//*[@class="nlc_img"]/a/@href')
# print(lp_name)
# print(lp_id)
for name, id in zip(lp_name, lp_id):
    # print(name)
    next_url = 'https:' + id
#     https://zz.newhouse.fang.com/loupan/2510148527.htm
#     id_1 = re.findall('loupan/(.*?).htm',id)[0]
#     next_url = f'https://zz.newhouse.fang.com/loupan/{id_1}/housedetail.htm'
    print(next_url)
    headers_1 = {
        'accept-encoding': 'gzip, deflate, br',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'cookie': 'city=zz; global_cookie=nsjk0wjl1x1vnu2b1f79i9a0k17km8q8jec; searchConN=1_1615700410_867%5B%3A%7C%40%7C%3A%5D6be2d74d43d38bf7844fdb6c396f8578; new_search_uid=38a427226e4354820afe93fb75d3a2a3; lastscanpage=0; resourceDetail=1; __utmz=147393320.1615769366.7.6.utmcsr=zz.fang.com|utmccn=(referral)|utmcmd=referral|utmcct=/; Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c=1615728202,1615769365,1615771248,1615809879; __utmc=147393320; g_sourcepage=xf_lp%5Elpsy_pc; csrfToken=JqbOYgOGsu5xqcUaYf2exnAM; Hm_lpvt_eaa57ca47dacb4ad4f5a257001a3457c=1615811837; unique_cookie=U_ieh85favrraigetj8wfryha512ykmajhctv*3; __utma=147393320.420763440.1615700411.1615809880.1615811838.9; __utmt_t0=1; __utmt_t1=1; __utmt_t2=1; __utmt_t3=1; __utmt_t4=1; __utmb=147393320.5.10.1615811838',
        'user-agent': ua.chrome
    }
    resp = session.get(next_url, headers=headers_1)
    # print(resp.encoding)
    # print(resp.content.decode())
    # data = re.findall(r'title="(.*?)"', resp.content.decode())
    # print(data)
    html = etree.HTML(resp.content)

    data = html.xpath('//title/text()')
    print(''.join(data).encode('iso8859-1').decode())



    break

# a = '郑州恒大未来之光'
# print(a.encode().decode('utf-8'))
# # print(a.encode().decode('gbk'))
# print(a.encode().decode('iso8859-1').encode('iso8859-1').decode())


