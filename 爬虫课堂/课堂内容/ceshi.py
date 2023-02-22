from requests_html import HTMLSession
from fake_useragent import UserAgent
from lxml import etree
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

response = session.post(start_url, headers=headers)
# rep = response.html.html
# 楼盘名字 xpath(//*[@class="nlc_img"]/a/img[2]/@alt)
lp_name = response.html.xpath('//*[@class="nlc_img"]/a/img[2]/@alt')
# 楼盘ID xpath(//*[@class="nlc_img"]/a/@href)
lp_id = response.html.xpath('//*[@class="nlc_img"]/a/@href')
# print(lp_name)
# print(lp_id)
for name, id in zip(lp_name, lp_id):
    id_1 = re.findall('loupan/(.*?).htm', id)[0]
    next_url = f'https://zz.newhouse.fang.com/loupan/{id_1}/housedetail.htm'
    # print(next_url)
    response_1 = session.get(next_url, headers=headers)
    html1 = etree.HTML(response_1.content.decode())
    print(response_1.content.decode())
    # 均价 average_price
    average_price = html1.xpath('/html/body/div[5]/div[5]/div/div[1]/div[1]/div/div[1]/div[2]/p/em/text()')
    print(average_price)
    # 建筑类别
    # Lb= html1.xpath('/html/body/div[5]/div[5]/div/div[1]/div[1]/ul/li[3]/div[2]/span/text()')
    Lb = response_1.html.xpath(
        '/html/body/div[5]/div[5]/div/div[1]/div[1]/ul/li[3]/div[2]/span[@class="bulid-type"]/text()')
    print(Lb)

    # 开发 商
    kfs = html1.xpath('/html/body/div[5]/div[5]/div/div[1]/div[1]/ul/li[7]/div[2]/text()')
    # 楼盘地址
    lp_addr = html1.xpath('/html/body/div[5]/div[5]/div/div[1]/div[1]/ul/li[8]/div[2]/text()')
    # 装修状况
    zx = html1.xpath('/html/body/div[5]/div[5]/div/div[1]/div[1]/ul/li[4]/div[2]/text()')
    # 环线位置
    hx_addr = html1.xpath('/html/body/div[5]/div[5]/div/div[1]/div[1]/ul/li[6]/div[2]/text()')
    # 销售信息
    xs = html1.xpath('/html/body/div[5]/div[5]/div/div[1]/div[2]/text()')

    print(kfs, lp_addr, zx, hx_addr, xs)
    # average_price = response_1.html.xpath('/html/body/div[5]/div[3]/div[2]/div[1]/div[5]/div[1]/span/text()')[0] + '元/㎡'
    # print(average_price)
    # # 项目地址：
    # # xm_addr = response_1.html.xpath('//*[@id="xfptxq_B04_23"]')
    # xm_addr = re.findall('<span style="color:#333;" title="(.*?)">', response_1.content.decode())
    # print(xm_addr)
    # # print(response_1.content.decode())
    # # 近期开盘
    # jqkp = re.findall('<a class="newkaipan"  id="xfptxq_B04_23" title="(.*?)"', response_1.content.decode())
    # print(jqkp)
    # # 主力户型
    # huX = re.findall('<a href="/loupan/2510148677/photo/d_house_64260.htm" target="_blank" title="(.*?)">',
    #                  response_1.content.decode())
    # # 详情
    # name_k = re.findall('<meta name="keywords" content="(.*?)" />', response_1.content.decode())
    # Description = re.findall('<meta name="Description" content="(.*?)" />', response_1.content.decode())
    #
    # var_ubp = re.findall('var ubp = {"vwg.page":"xf_lp\^lpsy_pc",(.*?)"}',response_1.content.decode())
    # print(huX,name_k)

    break