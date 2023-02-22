from requests_html import HTMLSession
from fake_useragent import UserAgent
from jsonpath import jsonpath

ua = UserAgent()
session = HTMLSession()

# http://119.29.29.29/d?dn=wup.imtt.qq.com

s_url = 'https://wa.qq.com/hot-res/746184cd86384ef47f81a655608e47e0-t.gif?mType=Other'
headers = {
    'User-agent': 'Mozilla/5.0 (Linux; U; Android 10; zh-cn; JER-AN10 Build/HUAWEIJER-AN10) AppleWebKit/533.1 (KHTML, like Gecko) Mobile Safari/533.1',
    # 'Q-GUID':'CCB6057B288249D01B741C30B81D5991A94958D6105DC19F4F91686061B781F9',
}
resp = session.get(s_url, headers=headers)
# print(resp.content)
with open('qq1.txt', 'wb')as f:
    f.write(resp.content)

