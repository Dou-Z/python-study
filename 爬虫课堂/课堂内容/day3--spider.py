# import requests
#
# start_url = 'https://www.baidu.com'
#
# headers = {
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81'
# }
#
# response = requests.get(start_url,headers=headers)
# 获取响应原码：字符串类型
# print(response.text,type(response.text))
# print("===============================================================================")
# response.content字节类型，需要decode（）编码
# print(response.content,type(response.content))

# 获取状态码
# print(response.status_code)
# if response.status_code == 200:
#     print('数据提取')
# else:
#     print('重新发送请求')

# print(response.cookies)

# print(response.json())

# import requests
#
# # 会话保持操作，让程序记录登录状态
# session = requests.session()
#
# start_url = 'https://accounts.douban.com/j/mobile/login/basic'
# headers = {
#     'referer': 'https://www.douban.com/',
#     'user-agant': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
# }
# data = {
#     'ck':'',
#     'remember': 'true',
#     'name': '13193709088',
#     'password': 'dz123456'
# }
# session.post(start_url,data=data,headers=headers)
# next_url = 'https://www.douban.com/'
# response_1 = session.get(next_url,headers=headers)
# print(response_1.content.decode())


import requests
proxy = {
    '117.95.192.77':'9999'
}
start_url = 'https://baidu.com/'
response = requests.get(start_url,proxies=proxy)
print(response.content.decode())