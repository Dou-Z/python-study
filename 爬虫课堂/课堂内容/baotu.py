from requests_html import HTMLSession
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import os
ua = UserAgent()
session = HTMLSession()
# https://ibaotu.com/sucai/19708321.html
s_url ='https://ibaotu.com/?chan=bd&label=ppt&plan=G1-bd&kwd=522482&unit=14375&bd_vid=4449992768782694892'
SP_url = 'https://ibaotu.com/shipin/'
headers = {
    'User-Agent':ua.chrome,
    'Cookie': 'FIRSTVISITED=1615195133.748; Hm_lvt_2b0a2664b82723809b19b4de393dde93=1615195133,1615195185; Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c=1615195134,1615195185; selectJs=1; user_refers=a%3A2%3A%7Bi%3A0%3Bs%3A3%3A%22sem%22%3Bi%3A1%3Ba%3A4%3A%7Bs%3A4%3A%22from%22%3Bs%3A2%3A%22bd%22%3Bs%3A4%3A%22plan%22%3Bs%3A5%3A%22G1-bd%22%3Bs%3A7%3A%22keyword%22%3Bs%3A6%3A%22522482%22%3Bs%3A4%3A%22unit%22%3Bs%3A5%3A%2214375%22%3B%7D%7D; is_sem_chan=1; new_edition_type=0; act9011_pop_hide=1; __is_small_screen=1; referer=http%3A%2F%2Fibaotu.com%2F%3Fm%3Dstats%26callback%3DjQuery11240011740513231284666_1617074508235%26lx%3D1%26pagelx%3D11%26exectime%3D0.0003%26loadtime%3D0.99%26_%3D1617074508238; wx_oal_type=1; md_session_id=20210330001599918; login_type=QQ; md_session_expire=1800; auth_id=38279175%7C%28%EF%BD%A1%C3%AC+_+%C3%AD%EF%BD%A1%29%7C1618375273%7Ca8e8631b542e0dcbe872bcc6b5884654; sns=%7B%22type%22%3A%22qq%22%2C%22token%22%3A%7B%22access_token%22%3A%224370160124BBDA988A7A46B5E6A5B81D%22%2C%22expires_in%22%3A%227776000%22%2C%22refresh_token%22%3A%220A81F945B0268063ACF33984760BAC3C%22%2C%22openid%22%3A%226C106A6018F076F435F4548EFCBBCF99%22%7D%7D; last_auth=1; head_38279175=%2F%2Fqzapp.qlogo.cn%2Fqzapp%2F101334430%2F6C106A6018F076F435F4548EFCBBCF99%2F100; WEBPARAMS=is_pay=0; ISREQUEST=1; hide_bully_time=1; Hm_lvt_bdba7c5873b3a5c678c7e71b38052312=1615195134,1615195185,1617074509,1617079724; Hm_lvt_4df399c02bb6b34a5681f739d57787ee=1615195134,1615195185,1617074509,1617079725; bt_guid=3652da74d745087c86c7a991b07c1b57; Hm_lpvt_4df399c02bb6b34a5681f739d57787ee=1617080877; Hm_lpvt_bdba7c5873b3a5c678c7e71b38052312=1617080877',
    'Host': 'ibaotu.com',
    'Referer': 'https://ibaotu.com/shipin/',
    'Upgrade-Insecure-Requests': '1',
}

resp = session.get(SP_url,headers=headers)
# code_num = resp.status_code
soup = BeautifulSoup(resp.html.html, 'lxml')
# print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.get_text())
v_url_list = soup.find_all("video")[3:]
# print(v_url_list)
v_name = soup.find_all('span','video-title')
# for na in v_name:
#     vname = na.string
#
# print(v_name)
for v_url,na in zip(v_url_list,v_name):
    v = v_url.get('src')
    vname = na.string
    print()
    v_u = 'https:'+ v
    # print(v_u)
    resp_1 = session.get(v_u)
    data = resp_1.content
    # print(data)
    os_pa = './包图视频/'
    print('=============','开始下载',vname,'===========')
    if not os.path.exists(os_pa):
        os.mkdir(os_pa)
    with open(os_pa + vname + '.mp4','wb')as f:
        f.write(data)
        print('=============下载完成===========')
    # break


# data = resp.html.xpath('/html/body/div[4]/div[2]/div[3]/div[4]/ul/li[1]/div/div/a/div[1]/video/@src')
# print(data)

