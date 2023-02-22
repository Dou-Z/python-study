# https://www.qidian.com/search?kw=%E5%8D%8A%E4%BB%99

# 半仙   https://book.qidian.com/info/1020180183
# 孙半仙 https://book.qidian.com/info/1017574250

# 第一章 https://m.qidian.com/book/1025986669/0
# 第二章 https://m.qidian.com/book/1025986669/633074137
# 第二章 https://m.qidian.com/majax/chapter/getChapterInfo?_csrfToken=fkg7Q6ffscJxGeAsC0BwSFzQNoVuEeBLjLei6yBO&bookId=1025986669&chapterId=633074137


from requests_html import HTMLSession
from urllib.parse import quote
from jsonpath import jsonpath
import re

session = HTMLSession()
title = input('请输入小说名：')
title = '人在恶土无限复活'
start_url = f'https://m.qidian.com/search?kw={ quote(title)}'

headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Mobile Safari/537.36',
    'cookie': '_csrfToken=fkg7Q6ffscJxGeAsC0BwSFzQNoVuEeBLjLei6yBO; newstatisticUUID=1615471426_1721714161; hiijack=0; Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c=1615472844; e1=%7B%22pid%22%3A%22qd_P_Searchresult%22%2C%22eid%22%3A%22%22%2C%22l1%22%3A3%7D; e2=%7B%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_H_Search%22%2C%22l1%22%3A2%7D',
    'referer': 'https://www.qidian.com/',
}
response = session.get(start_url, headers=headers)

# print(response.content.decode())
title_list = response.html.xpath('//*[@id="books-"]/li/a/div/div[1]/h4/text()')
one = response.html.xpath('//*[@id="books-"]/li/a/div/div[1]/h4/mark/text()')
title_list = one + title_list
# print(len(title_list))
href_list = response.html.xpath('//*[@id="books-"]/li/a/@href')
# print(len(href_list))
for herf,item in zip(href_list,title_list):

    next_url = f'https://m.qidian.com{herf}/0'
    # book ID
    book_id = herf[6:]
    # print(herf)
    response_1 = session.get(next_url, headers=headers)
    # print(response_1.content.decode())
    # 下一章ID
    next_id_1 = re.findall('"next":(.*?),',response_1.content.decode())[0]
    # 第一章ID
    next_id = re.findall('data-chapter-id="(.*?)" >',response_1.content.decode())[0]
    # print(next_id,chapter_id)
    page_url = f'https://m.qidian.com/majax/chapter/getChapterInfo?_csrfToken=fkg7Q6ffscJxGeAsC0BwSFzQNoVuEeBLjLei6yBO&bookId={book_id}&chapterId={next_id}'
    response_2 = session.get(page_url,headers=headers)
    # print(response_2.html.html)
    # html = response_2.html.html
    nextName = jsonpath(response_2.json(),'$..chapterName')
    content = jsonpath(response_2.json(),'$..content')
    # print(nextName,content[0])
    content_1 = re.findall('<.*?>',content[0])
    content_2 = re.sub('<p>','\\n',content[0])
    print(content_2)
    # xs = response_2.content.decode()
    # xs = jsonpath(xs,'$..content')
    # print(xs)
    break
