# import requests
#
# session = requests.session()
#
# start_url = 'https://accounts.douban.com/j/mobile/login/basic'
#
# data = {
#     'ck': '',
#     'remember': 'true',
#     'name': '13193709088',
#     'password': 'dz123456',
# }
# headers = {
#     'Host': 'accounts.douban.com',
#     'Origin': 'https://accounts.douban.com',
#     'Referer': 'https://accounts.douban.com/passport/login_popup?login_source=anony',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
# }
# headers_1 = {
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
# }
#
# session.post(start_url, data=data, headers=headers)
# next_url = 'https://www.douban.com/'
# response = session.get(next_url,headers=headers_1)
# print(response.text)

# import requests
#
# start_url = 'https://www.baidu.com'
# response = requests.get(start_url)
# print(response.cookies)
# print(requests.utils.dict_from_cookiejar(response.cookies))

# 使用cookies登录豆瓣

cookie_str = """ll="118253"; bid=xqs0FXhww0Y; __utmz=30149280.1614751770.1.1.utmcsr=(direct)|utmccn=(direct\
|utmcmd=(none); push_doumail_num=0; push_noty_num=0; __utmv=30149280.20258; __yadk_uid=yccrKwl3aXpVYuPAH3d\
OLYNJ2RmC5kWc; _vwo_uuid_v2=DD42CE6C9A26A335DDDE074D748EC40F9|6ead799357458bd16dee7e253e0cc5ea; __gads=ID=\
3a65c91ee7feec11:T=1614953123:S=ALNI_Ma7cHlC_Rnnv9POnOnd6J86AiZMKQ; _pk_ses.100001.8cb4=*; __utmc=30149280;\
 __utma=30149280.1558427072.1614751770.1614953115.1614993899.3; __utmt=1; dbcl2="202580961:rXutxH92zJU"; \
 ck=tNj0; _pk_id.100001.8cb4=7ba008f42903d17d.1614751769.3.1614993906.1614953154.; ap_v=0,6.0; __\
 utmb=30149280.3.10.1614993899; Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c=1614953115,1614953125,\
 1614993899,1614993907; Hm_lpvt_eaa57ca47dacb4ad4f5a257001a3457c=1614993907"""
# cookie_list = cookie_str.split('; ')
# #将cookies字符串转成字典
# cookie_dict = {}
# for cookies in cookie_str.split('; '):
#     c_data_list= cookies.split('=')
#     cookie_dict[c_data_list[0]] = c_data_list[1]

# print(cookie_dict)

# cookies_dict = {cookie.split('=')[0]:cookie.split('=')[1] for cookie in cookie_str.split('; ')}
# print(cookies_dict)
#
# import requests
# headers = {
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
# }
#
# start_url = 'https://www.douban.com'
# response = requests.get(start_url, cookies=cookies_dict,headers=headers)
# print(response.content.decode())

# import requests
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
# }
# start_url = 'https://v.douyin.com/eec2XS7/'
# response = requests.get(start_url,allow_redirects=False,headers=headers)
# print(response.content.decode())
#
# response_1 = requests.get(start_url,headers=headers)
# print(response_1.content.decode())

# import requests
# proxy = {
#     '127.0.0.1:9999'
# }
# start_url = 'https://www.baidu.com'
# try:
#     response = requests.get(start_url,timeout=3,proxies=proxy)
#     with open('代理.txt','a+')as f:
#         f.write(str(proxy))
# except:
#     pass


# import requests
# from retrying import retry
#
# proxy= {
#
#     'https':'https://1.1.1.1:9999'
# }
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
# }
#
# @retry(stop_max_attempt_number = 5)
# def _parse_url(url):
#     print('执行一次')
#     response = requests.get(url,headers=headers,timeout=3,proxies=proxy)
#
#     assert response.status_code == 200
#     return response.content.decode()
# def parse_url(url):
#
#     try:
#         html = _parse_url(url)
#
#     except Exception as e:
#         print(e)
#         html = None
#     return html
#
# if __name__ == '__main__':
#     url = 'https://www.baidu.com'
#     h = parse_url(url)
#     print(h)

# from requests_html import HTMLSession
# from fake_useragent import UserAgent
# ua = UserAgent
# session = HTMLSession()


## 酷我音乐爬取
# from requests_html import HTMLSession
# session = HTMLSession()
# import os
# from urllib.parse import quote
#
# singer = quote(input('请输入歌手：'))
# start_url = f'http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={singer}&pn=1&rn=30&httpsStatus=1&reqId=6c113131-7e33-11eb-9ecc-f345470ec4cc'
# headers = {
#     # 用户信息
#     'Cookie': '_ga=GA1.2.1559515117.1614306533; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1614306532,1615004435; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1615004435; _gid=GA1.2.995625800.1615004435; _gat=1; Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c=1614306533,1615004435; Hm_lpvt_eaa57ca47dacb4ad4f5a257001a3457c=1615004435; kw_token=SMQG2T2LCYR',
#     # 一把钥匙
#     'csrf': 'SMQG2T2LCYR',
#     # 域名
#     'Host': 'www.kuwo.cn',
#    # 这个页面的上一次请求页面
#     'Referer': 'http://www.kuwo.cn/search/list?key=%E5%91%A8%E6%9D%B0%E4%BC%A6',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
# }
#
# # 2.发送数据，获取响应
# response = session.get(start_url,headers=headers)
# # 3.数据解析，数据提取
# data_json = response.json()
# # print(data_json)
# mp3_list = data_json['data']['list']
# for data in mp3_list:
#     name = data['name']
#     rid = data['rid']
#     print(name,rid)
#     next_url = f'http://www.kuwo.cn/url?format=mp3&rid={rid}&response=url&type=convert_url3&br=128kmp3&from=web&t=1615006204140&httpsStatus=1&reqId=6a9542c1-7e37-11eb-8df0-13f972a74b72'
#     mp3_response = session.get(next_url).json()
#     # print(mp3_response)
#     mp3_url = mp3_response['url']
#     mp3_data = session.get(mp3_url).content
#     os_path = './酷我MP3/'
#     if not os.path.exists(os_path):
#         os.mkdir(os_path)
#     with open(os_path + name + '.mp3','wb')as f:
#         f.write(mp3_data)
#
#     print(f'{name}======下载完成！！！=====logging==== ')


# 快手短视频评论爬取
from requests_html import HTMLSession

session = HTMLSession()

start_url = 'https://video.kuaishou.com/graphql'
proxy = {
    'http':'http:/60.167.52.106:8888'
}
headers = {
    'content-type': 'application/json',
    'Cookie': 'did=web_2dcad0e382b435402faf1740d4cb8bbb; didv=1614478591897; kpf=PC_WEB; kpn=KUAISHOU_VISION; clientid=3; Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c=1614478628,1615012879; Hm_lpvt_eaa57ca47dacb4ad4f5a257001a3457c=1615012881',
    'Host': 'video.kuaishou.com',
    'Origin': 'https://video.kuaishou.com',
    'Referer': 'https://video.kuaishou.com/short-video/3xs7uxs6r52xj8k?authorId=3xgfrfi56s8am4g&streamSource=brilliant&hotChannelId=00&area=brilliantxxrecommend',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
}
data = {"operationName":"commentListQuery","variables":{"photoId":"3xs7uxs6r52xj8k","pcursor":""},"query":"query commentListQuery($photoId: String, $pcursor: String) {\n  visionCommentList(photoId: $photoId, pcursor: $pcursor) {\n    commentCount\n    pcursor\n    rootComments {\n      commentId\n      authorId\n      authorName\n      content\n      headurl\n      timestamp\n      likedCount\n      realLikedCount\n      liked\n      status\n      subCommentCount\n      subCommentsPcursor\n      subComments {\n        commentId\n        authorId\n        authorName\n        content\n        headurl\n        timestamp\n        likedCount\n        realLikedCount\n        liked\n        status\n        replyToUserName\n        replyTo\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"}

response = session.post(start_url, json=data,headers=headers,proxies=proxy,timeout=5).json()
data_list_1 = response['data']['visionCommentList']['rootComments']
# print(data_list_1)

for data_list_2 in data_list_1:
    print(data_list_2['authorName'],'========>',data_list_2['content'])
    print('---------------------------------------------------------------------------------------')
    for data_3 in data_list_2['subComments']:
        print('其他用户追评==============',data_3['authorName'], '=====>', data_3['content'])

