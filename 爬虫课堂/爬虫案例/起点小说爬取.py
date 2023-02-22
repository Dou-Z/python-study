from requests_html import HTMLSession
from urllib.parse import quote
from jsonpath import jsonpath
import re, os

session = HTMLSession()


class qdSpider(object):
    def __init__(self):

        title = input('请输入小说名：')
        # title = '人在恶土无限复活'
        self.start_url = f'https://m.qidian.com/search?kw={quote(title)}'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Mobile Safari/537.36',
            'cookie': '_csrfToken=fkg7Q6ffscJxGeAsC0BwSFzQNoVuEeBLjLei6yBO; newstatisticUUID=1615471426_1721714161; hiijack=0; Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c=1615472844; e1=%7B%22pid%22%3A%22qd_P_Searchresult%22%2C%22eid%22%3A%22%22%2C%22l1%22%3A3%7D; e2=%7B%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_H_Search%22%2C%22l1%22%3A2%7D',
            'referer': 'https://www.qidian.com/',
        }

    def parse_start_url(self):
        response = session.get(self.start_url, headers=self.headers)

        title_list = response.html.xpath('//*[@id="books-"]/li/a/img/@alt')

        # print(len(title_list))
        href_list = response.html.xpath('//*[@id="books-"]/li/a/@href')
        # print(len(href_list))
        for herf, item in zip(href_list, title_list):
            next_url = f'https://m.qidian.com{herf}/0'
            # book ID
            book_id = herf[6:]

            response_1 = session.get(next_url, headers=self.headers)
            # print(response_1.content.decode())
            # 下一章ID
            # next_id_1 = re.findall('"next":(.*?),', response_1.content.decode())[0]
            # 第一章ID
            next_id = re.findall('data-chapter-id="(.*?)" >', response_1.content.decode())[0]
            next_id = ''.join(next_id)
            self.parse_response_data(book_id, next_id, item)
            print(f'====={item}====下载完成!!!')
            break

    def parse_response_data(self, book_id, next_id, item):

        page_url = f'https://m.qidian.com/majax/chapter/getChapterInfo?_csrfToken=fkg7Q6ffscJxGeAsC0BwSFzQNoVuEeBLjLei6yBO&bookId={book_id}&chapterId={next_id}'
        response_2 = session.get(page_url, headers=self.headers)
        # print(response_2.html.html)
        # html = response_2.html.html
        nextName = jsonpath(response_2.json(), '$..chapterName')[0]
        content = jsonpath(response_2.json(), '$..content')[0]
        # content_1 = re.findall('<.*?>', content)
        content_2 = re.sub('<p>', '\\n', content)
        # print(nextName, content_2)
        self.data_save(name=nextName, data=content_2, item=item)
        next_id = re.findall('"next":(.*?),', response_2.content.decode())[0]
        # print(next_id)
        self.parse_response_data(book_id, next_id, item)

    def data_save(self, name, data, item):

        os_path = './起点小说/'
        if not os.path.exists(os_path):
            os.mkdir(os_path)
        with open(os_path + item + '.txt', 'a+', encoding='UTF-8')as f:
            f.write(name + data)
            print(f'正在下载==={name}====logging!!!')


if __name__ == '__main__':
    qd = qdSpider()
    qd.parse_start_url()
