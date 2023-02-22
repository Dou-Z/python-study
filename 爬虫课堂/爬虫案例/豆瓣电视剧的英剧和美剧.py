from requests_html import HTMLSession
session = HTMLSession()
import json


class Douban(object):
    def __init__(self, tv_name):
        self.start_url = 'https://movie.douban.com/j/search_subjects?type=tv&tag={}&sort=recommend&page_limit=20&page_start={}'
        self.referer = 'https://m.douban.com/movie/subject/{}/'
        self.tv_msg = 'https://m.douban.com/rexxar/api/v2/tv/{}?ck=&for_mobile=1'
        self.tv_name = tv_name

    def run(self):
        """
        拼接url，获取翻页信息
        :return:
        """
        for i in range(5):
            # 拼接url，获取翻页信息
            url = self.start_url.format(self.tv_name, i)
            # 获取url响应的json数据，并转换成字典
            tv_list_json = json.loads(session.get(url).content.decode())
            # print(tv_list_json)
            self.parse_json_data(tv_list_json)
            break
    def parse_json_data(self, json_data):
        """
        json数据解析
        :param json_data: json_data
        :return:
        """
        # 遍历字典，获取需要的数据
        for tv in json_data['subjects']:
            # 电视剧标题
            tv_title = tv['title']
            # 电视剧的url
            tv_url = tv['url']
            # 电视剧的图片地址
            tv_img = tv['cover']
            # 电视剧的id
            tv_id = tv['id']
            self.parse_tv(tv_id, tv_title, tv_url, tv_img)

    def parse_tv(self, tv_id, tv_title, tv_url, tv_img):
        """

        :param tv_id:
        :return:
        """
        # 拼接电视剧详细信息的url
        url = self.tv_msg.format(tv_id)
        # 反反爬，拼接referer
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Appl\
                            eWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
                   'referer': self.referer.format(tv_id)}
        # 获取json数据，转化为字典
        tv_json_data = json.loads(session.get(url, headers=headers).content.decode('utf-8'))
        # 获取电视剧简介
        intro = tv_json_data['intro']
        self.actor_msg(tv_json_data, tv_title, tv_url, tv_img, intro)

    def actor_msg(self, tv_json_data, tv_title, tv_url, tv_img, intro):
        name = []
        # 演员在字典中，循环取出演员名
        for actor in tv_json_data['actors']:
            name.append(actor)
        self.save(name, tv_title, tv_url, tv_img, intro)

    def save(self, name, tv_title, tv_url, tv_img, intro):
        with open('tv.txt', 'a+', encoding='utf-8')as f:
            # 构造上下文
            content = {
                '类别': self.tv_name,
                '标题': tv_title,
                '播放链接': tv_url,
                '封面链接': tv_img,
                '内容简介': intro,
                '演员': name
            }
            f.write(str(content) + '\r\n')
        print('{}{}保存完成'.format(self.tv_name, tv_title))


if __name__ == '__main__':
    print("1: '美剧', 2: '英剧'")
    while True:
        num = input('请输入对应的编号, 按回车结束')
        if num == '1' or num == '2':
            data = {1: '美剧', 2: '英剧'}
            douban = Douban(data[int(num)])
            douban.run()
            continue
        if num == '0':
            break
        else:
            print('输入有误')