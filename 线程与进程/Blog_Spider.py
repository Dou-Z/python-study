from requests_html import HTMLSession
session = HTMLSession()
from requests.packages import urllib3
urllib3.disable_warnings()

urls = [f'https://www.cnblogs.com/#p{page}' for page in range(1,50+1)]
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}

def craw(url):
    r = session.get(url,headers=header,verify=False)
    return r.html


def parse(html):
    # // *[ @ id = "post_list"] / article[1] / section / div / a / @ href
    links = html.xpath('//*[@id="post_list"]/article/section/div/a/@href')
    name_li = html.xpath('//*[@id="post_list"]/article/section/div/a/text()')
    return [(link,name) for link,name in zip(links,name_li)]


if __name__ == '__main__':
    for result in parse(craw(urls[2])):
        print(result)

    # print(urls)
