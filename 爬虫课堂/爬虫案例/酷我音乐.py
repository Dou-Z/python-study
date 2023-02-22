# 酷我音乐爬取
from requests_html import HTMLSession
session = HTMLSession()
import os
from urllib.parse import quote

singer = quote(input('请输入歌手：'))
start_url = f'http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={singer}&pn=1&rn=30&httpsStatus=1&reqId=6c113131-7e33-11eb-9ecc-f345470ec4cc'
headers = {
    # 用户信息
    'Cookie': '_ga=GA1.2.1559515117.1614306533; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1614306532,1615004435; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1615004435; _gid=GA1.2.995625800.1615004435; _gat=1; Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c=1614306533,1615004435; Hm_lpvt_eaa57ca47dacb4ad4f5a257001a3457c=1615004435; kw_token=SMQG2T2LCYR',
    # 一把钥匙
    'csrf': 'SMQG2T2LCYR',
    # 域名
    'Host': 'www.kuwo.cn',
   # 这个页面的上一次请求页面
    'Referer': 'http://www.kuwo.cn/search/list?key=%E5%91%A8%E6%9D%B0%E4%BC%A6',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
}

# 2.发送数据，获取响应
response = session.get(start_url,headers=headers)
# 3.数据解析，数据提取
data_json = response.json()
# print(data_json)
mp3_list = data_json['data']['list']
for data in mp3_list:
    name = data['name']
    rid = data['rid']
    print(name,rid)
    next_url = f'http://www.kuwo.cn/url?format=mp3&rid={rid}&response=url&type=convert_url3&br=128kmp3&from=web&t=1615006204140&httpsStatus=1&reqId=6a9542c1-7e37-11eb-8df0-13f972a74b72'
    mp3_response = session.get(next_url).json()
    # print(mp3_response)
    mp3_url = mp3_response['url']
    mp3_data = session.get(mp3_url).content
    os_path = './酷我MP3——1/'
    if not os.path.exists(os_path):
        os.mkdir(os_path)
    with open(os_path + name + '.mp3','wb')as f:
        f.write(mp3_data)

    print(f'{name}======下载完成！！！=====logging==== ')