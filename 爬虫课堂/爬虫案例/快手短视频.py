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
# print(response)
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