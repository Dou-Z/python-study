from multiprocessing import Pool

import requests
# 1.准备起始的url地址
# start_url = "http://pic.netbian.com//uploads/allimg/210216/194423-1613475863c1a0.jpg"
# # 2.发送请求，获取响应
# response = requests.get(start_url)
# # 3.数据解析，数据提取
# # 回去二进制数据
# data = response.content
# print(data)
# # 4.保存数据
# with open('1.jpg','wb') as f:
#     f.write(data)

# start_url = 'https://www.baidu.com'
#
# headers = {
#     'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
# }
# response = requests.get(start_url,headers=headers)
#
# response_1 = requests.get(start_url)
# data = response.content.decode()
# data_1 = response_1.content.decode()
#
# print(data)
# print()
# print()
# print()
# print("===============================================")
# print(data_1)

# import re,random
# # str1 = '<meta http-equiv="content-type" content="text/html;charset=utf-8"/>adacc/sd/sdef/24'
# #
# # result = re.findall(r'<.*>', str1)
# # print(result)
# proxy = {
#         'http':'http://60.167.52.106:8888',
#             'http':'http://8.133.191.41:8888',
#             'http':'http://8.133.191.41:80',
#             'http':'http://8.133.191.41:8080',
# }
#
#
# str = random.choice(list(proxy.keys()), weights=list(proxy.values()),k=1)
# print(str)

# res = requests.get("https://m.weibo.cn/profile/info?uid=5720474518")
# re1,reds = res.json()['data']['user']['follow_count'], res.json()['data']['user']['followers_count']
# print(re1,reds)


def func(n):
    print(n)
a=(1,2,3,4,5)
b=[1,2,3,4,5]
c="python"
d = range(2,12)
la=map(str,a)
# lb=map(str,b)
# lc=map(str,c)
ld = map(func,d)
# print(list(la))
# #['1', '2', '3', '4', '5']
# print(lb)
# #['1', '2', '3', '4', '5']
# print(list(lc))
#['p', 'y', 't', 'h', 'o', 'n']
# print(type(str))
# pool = Pool(processes=4)
# pool.map(func,d)
url = 'https://m.weibo.cn/api/container/getIndex?containerid=231051_-_fans_-_1288739185'
res = requests.get(url)
cards = res.json()['data']['cards']
# print(cards)
for i in cards:
    # print(i)
    # break
    if "title" not in i:
        for j in i['card_group'][1]['users']:
            user_name = j['screen_name']  # 用户名
            user_id = j['id']  # 用户id
            fans_count = j['followers_count']  # 粉丝数量
            # sex, add = get_user_info(user_id)
            info = {
                "用户名": user_name,
                # "性别": sex,
                # "所在地": add,
                "粉丝数": fans_count,
            }
# print(info)
    else:
        for j in i['card_group']:
            user_name = j['user']['screen_name']  # 用户名
            user_id = j['user']['id']  # 用户id
            fans_count = j['user']['followers_count']  # 粉丝数量
            # sex, add = get_user_info(user_id)
            info = {
                "用户名": user_name,
                # "性别": sex,
                # "所在地": add,
                "粉丝数": fans_count,
            }

            print(info)