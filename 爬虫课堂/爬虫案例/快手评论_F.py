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