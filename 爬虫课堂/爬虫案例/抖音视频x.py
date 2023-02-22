from requests_html import HTMLSession

session = HTMLSession()
import re,os
from jsonpath import jsonpath
while True:
    start_url = input('请输入分享链接：')
    # start_url = '爸妈不让你吃泡面，就转给他们看%dou是知识点  https://v.douyin.com/edyU2wB/ 复淛此链接，打汧Dou音搜索，直接观看视频！'
    start_url = 'http' + re.findall('http(.*?) ', start_url)[0]
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    }
    response = session.get(start_url, headers=headers)
    url = response.url
    item_id = re.findall('video/(.*?)/', url)[0]
    next_url = f'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={item_id}'
    json_data = session.get(next_url).json()
    # print(json_data)
    share_title = jsonpath(json_data, '$..share_title')
    print(share_title[0])

    addr_play = jsonpath(json_data, '$..play_addr')
    url = jsonpath(addr_play, '$..url_list')[0][0]

    mp4_url = url.replace('playwm', 'play')
    data = session.get(mp4_url).content
    os_path = './dy/'
    if not os.path.exists(os_path):
        os.mkdir(os_path)
    with open(os_path + str(share_title) + '.mp4','wb')as f:
        f.write(data)
    print(f'{share_title}------保存完成')