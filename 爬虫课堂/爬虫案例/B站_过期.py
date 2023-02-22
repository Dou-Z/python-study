
from requests_html import HTMLSession
import re, os
session = HTMLSession()


class BiLi(object):
    def __init__(self, start_url):
        self.start_url = start_url
        self.headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML\
        , like Gecko) Chrome/83.0.4103.116 Mobile Safari/537.36'}

    def one_data_request(self):
        """
        发送请求,获取重定向的url
        :return:redirect_url
        """
        redirect_html = session.get(url=self.start_url).html.html
        try:
            redirect_url = re.findall(r'property="og:url" content="(.*?)"', redirect_html)[0]
        except:
            print('反爬规则已修改，请修改代码')
            return
        return redirect_url

    def two_data_mining(self, redirect_url):
        """
        发送请求,从响应中提取无水印的url
        :param redirect_url: redirect_url
        :return: mp4_url
        """
        response_text = session.get(url=redirect_url, headers=self.headers).html.text
        try:
            response_json = re.findall(r'window.__INITIAL_STATE__=(.+?);', response_text)[0]
            mp4_url = re.findall(r'"url":"(.+?)"', response_json)[0]
            mp4_name = re.findall(r'"title":"(.+?)"', response_json)[0]
            mp4_url = mp4_url.encode('latin-1').decode('unicode-escape')
            if '/' in mp4_name:
                mp4_name = mp4_name.replace('/', '')
            if '\\' in mp4_name:
                # eval(repr(mp4_name).replace('\\', '@'))
                mp4_name = mp4_name.replace('\\', '')
        except:
            print('反爬规则已修改，请修改代码')
            return
        return mp4_url, mp4_name

    def three_data_save(self, mp4_name, mp4_data):
        os_path = os.getcwd() + '/B站/'
        if not os.path.exists(os_path):
            os.mkdir(os_path)
        with open(os_path + mp4_name + '.mp4', 'wb')as f:
            f.write(mp4_data)
            print('视频---------------{}----------------提取完成'.format(mp4_name))

    def run(self):
        redirect_url = self.one_data_request()
        mp4_url, mp4_name = self.two_data_mining(redirect_url)
        mp4_data = session.get(url=mp4_url).content
        self.three_data_save(mp4_name, mp4_data)


if __name__ == '__main__':
    while True:
        start_url = input('请输入b站链接,输入0退出：')
        if start_url == '0':
            break
        b = BiLi(start_url)
        b.run()