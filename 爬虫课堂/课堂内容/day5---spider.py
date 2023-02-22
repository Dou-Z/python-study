# import json
#
# dict_1 = {'name':'向明','sex':'1'}
# with open('1.txt','w')as f:
#     json.dump(dict_1,f)
#
# with open('1.txt','r')as f:
#     print(json.load(f))

# from requests_html import HTMLSession
# from jsonpath import jsonpath
#
# session = HTMLSession()
#
# start_url = 'https://video.kuaishou.com/graphql'
# proxy = {
#     'http': 'http:/60.167.52.106:8888'
# }
# headers = {
#     'content-type': 'application/json',
#     'Cookie': 'did=web_2dcad0e382b435402faf1740d4cb8bbb; didv=1614478591897; kpf=PC_WEB; kpn=KUAISHOU_VISION; clientid=3; Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c=1614478628,1615012879; Hm_lpvt_eaa57ca47dacb4ad4f5a257001a3457c=1615012881',
#     'Host': 'video.kuaishou.com',
#     'Origin': 'https://video.kuaishou.com',
#     'Referer': 'https://video.kuaishou.com/short-video/3xs7uxs6r52xj8k?authorId=3xgfrfi56s8am4g&streamSource=brilliant&hotChannelId=00&area=brilliantxxrecommend',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
# }
# data = {"operationName": "commentListQuery", "variables": {"photoId": "3xs7uxs6r52xj8k", "pcursor": ""},
#         "query": "query commentListQuery($photoId: String, $pcursor: String) {\n  visionCommentList(photoId: $photoId, pcursor: $pcursor) {\n    commentCount\n    pcursor\n    rootComments {\n      commentId\n      authorId\n      authorName\n      content\n      headurl\n      timestamp\n      likedCount\n      realLikedCount\n      liked\n      status\n      subCommentCount\n      subCommentsPcursor\n      subComments {\n        commentId\n        authorId\n        authorName\n        content\n        headurl\n        timestamp\n        likedCount\n        realLikedCount\n        liked\n        status\n        replyToUserName\n        replyTo\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"}
#
# response = session.post(start_url, json=data, headers=headers, proxies=proxy, timeout=5).json()
# # data_list_1 = response['data']['visionCommentList']['rootComments']
# # print(response)
# authorName = jsonpath(response, '$..authorName')
# content = jsonpath(response, '$..content')
# print(authorName)
# print('===============================================')
# print(content)

# from requests_html import HTMLSession
#
# session = HTMLSession()
# import re,os
# from jsonpath import jsonpath
# while True:
#     start_url = input('请输入分享链接：')
#     # start_url = '爸妈不让你吃泡面，就转给他们看%dou是知识点  https://v.douyin.com/edyU2wB/ 复淛此链接，打汧Dou音搜索，直接观看视频！'
#     start_url = 'http' + re.findall('http(.*?) ', start_url)[0]
#     headers = {
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
#     }
#     response = session.get(start_url, headers=headers)
#     url = response.url
#     item_id = re.findall('video/(.*?)/', url)[0]
#     next_url = f'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={item_id}'
#     json_data = session.get(next_url).json()
#     # print(json_data)
#     share_title = jsonpath(json_data, '$..share_title')
#     print(share_title[0])
#
#     addr_play = jsonpath(json_data, '$..play_addr')
#     url = jsonpath(addr_play, '$..url_list')[0][0]
#
#     mp4_url = url.replace('playwm', 'play')
#     data = session.get(mp4_url).content
#     os_path = './dy/'
#     if not os.path.exists(os_path):
#         os.mkdir(os_path)
#     with open(os_path + str(share_title) + '.mp4','wb')as f:
#         f.write(data)
#     print(f'{share_title}------保存完成')

from requests_html import HTMLSession
from jsonpath import jsonpath
import os
session = HTMLSession()

start_url = 'https://video.kuaishou.com/graphql'

headers = {
    'content-type': 'application/json',
    'Cookie': 'did=web_2dcad0e382b435402faf1740d4cb8bbb; didv=1614478591897; kpf=PC_WEB; kpn=KUAISHOU_VISION; clientid=3; Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c=1614478628,1615012879,1615092449; Hm_lpvt_eaa57ca47dacb4ad4f5a257001a3457c=1615094192',
    'Host': 'video.kuaishou.com',
    'Origin': 'https://video.kuaishou.com',
    'Referer': 'https://video.kuaishou.com/',

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'

}
data = {"operationName":"brilliantTypeDataQuery","variables":{"hotChannelId":"00","page":"brilliant"},"query":"fragment feedContent on Feed {\n  type\n  author {\n    id\n    name\n    headerUrl\n    following\n    headerUrls {\n      url\n      __typename\n    }\n    __typename\n  }\n  photo {\n    id\n    duration\n    caption\n    likeCount\n    realLikeCount\n    coverUrl\n    photoUrl\n    coverUrls {\n      url\n      __typename\n    }\n    timestamp\n    expTag\n    animatedCoverUrl\n    distance\n    videoRatio\n    liked\n    stereoType\n    __typename\n  }\n  canAddComment\n  llsid\n  status\n  currentPcursor\n  __typename\n}\n\nfragment photoResult on PhotoResult {\n  result\n  llsid\n  expTag\n  serverExpTag\n  pcursor\n  feeds {\n    ...feedContent\n    __typename\n  }\n  webPageArea\n  __typename\n}\n\nquery brilliantTypeDataQuery($pcursor: String, $hotChannelId: String, $page: String, $webPageArea: String) {\n  brilliantTypeData(pcursor: $pcursor, hotChannelId: $hotChannelId, page: $page, webPageArea: $webPageArea) {\n    ...photoResult\n    __typename\n  }\n}\n"}
response = session.post(start_url,headers=headers,json=data).json()
print(response)
photoUrl = jsonpath(response,'$..photoUrl')
caption = jsonpath(response,'$..caption')

for url,name in zip(photoUrl,caption):
    data_1 = session.get(url).content
    os_path = './ks/'
    if not os.path.exists(os_path):
        os.mkdir(os_path)
    with open(os_path + str(name) + '.mp4','wb')as f:
        print('正在保存...')
        f.write(data_1)
    print(f'{name}------>保存完成')



# url = 'https:\u002F\u002Fupos-sz-mirrorks3.bilivideo.com\u002Fupgcxcode\u002F82\u002F70\u002F306987082\u002F306987082_nb2-1-16.mp4?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&uipk=5&nbs=1&deadline=1615111711&gen=playurl&os=ks3bv&oi=2099930370&trid=e5036b740f064dec8fd1c2e06ee1395fh&platform=html5&upsig=c86714076061f21fc870c643fca7c899&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mid=0&logo=80000000'
#
# result = url.encode('latin-1').decode('unicode-escape')
# print(result)