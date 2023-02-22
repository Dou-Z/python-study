import tkinter as tk
import tkinter.messagebox as msgbox
import webbrowser
import os, re, requests, jsonpath
from requests_html import HTMLSession
session = HTMLSession()


class Aef(object):
    def __init__(self):
        self.str_data = ['douyin', 'kuaishou', 'pipix', 'huoshan', 'bilibili', 'b23']
        self.num_data = [0, 1, 2, 3, 4, 5]
        self.w = 500
        self.h = 500
        self.title = '阿尔法无水印MP4提取助手'
        # 窗口取名
        self.root = tk.Tk(className=self.title)
        # 定义button控件上的文字
        self.url = tk.StringVar()
        # 选择代理
        self.v = tk.IntVar()
        # 默认不使用
        self.v.set(1)
        # Frame空间
        frame_1 = tk.Frame(self.root)
        frame_2 = tk.Frame(self.root)
        frame_3 = tk.Frame(self.root)

        # Menu菜单
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)
        mp4menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label='友情链接', menu=mp4menu)

        # 各个短视频网站链接，友情合作
        mp4menu.add_command(label='抖音', command=lambda: webbrowser.open('./a.png'))

        # 控件内容设置
        group = tk.Label(frame_1, text='请选择一个代理：', padx=10, pady=10)
        tb1 = tk.Radiobutton(frame_1, text='代理一', variable=self.v, value=1, width=10, height=3)
        tb2 = tk.Radiobutton(frame_1, text='代理二', variable=self.v, value=2, width=10, height=3)
        label1 = tk.Label(frame_2, text="请输入视频链接：")
        entry = tk.Entry(frame_2, textvariable=self.url, highlightcolor='Fuchsia', highlightthickness=1, width=35)
        label2 = tk.Label(frame_2, text=" ")
        play = tk.Button(frame_2, text="提取", font=('楷体', 12), fg='Purple', width=2, height=1, command=self.run)
        label3 = tk.Label(frame_2, text=" ")
        label_explain = tk.Label(frame_3, fg='red', font=('楷体', 12),
                                 text='\n注意：仅支持抖音,快手,火山,皮皮虾，B站视频网站的视频提取！\n此软件仅用于交流学习，请勿用于任何商业用途！')
        label_warning = tk.Label(frame_3, fg='blue', font=('楷体', 12), text='\n无水印视频将会保存在当前程序文件目录下<视频MP4>\n')

        # 控件布局
        frame_1.pack()
        frame_2.pack()
        frame_3.pack()
        group.grid(row=0, column=0)
        tb1.grid(row=0, column=1)
        tb2.grid(row=0, column=2)
        label1.grid(row=0, column=0)
        entry.grid(row=0, column=1)
        label2.grid(row=0, column=2)
        play.grid(row=0, column=3, ipadx=10, ipady=10)
        label3.grid(row=0, column=4)
        label_explain.grid(row=1, column=0)
        label_warning.grid(row=2, column=0)

    def url_estimate(self):
        """
        url清洗, 是否使用代理判断
        :return: start_url, proxies
        """
        # 正则匹配规则，提取链接中的url，过滤
        pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        try:
            # 正则匹配，正则的findall方法，没有匹配到就报错，再次try一下，返回一个列表
            start_url = re.findall(pattern, self.url.get())[0]
        except:
            print('反爬规则已修改，请修改代码')
            return

        if self.v.get() == 1:
            # 不使用代理
            proxies = None

        else:
            # 使用代理
            proxies = {"http": "http://117.127.0.195:8080"}
        return start_url, proxies

    def start_url_judge(self):
        """
        start_url的判断，判断属于哪一个平台，并返回对应的num
        :return: num
        """
        try:
            start_url, proxies = self.url_estimate()
            # zip方法， for循环两个列表中的元素，且一一对应
            for mp4_url_data, num in zip(self.str_data, self.num_data):
                # 判断 'douyin', 'kuaishou', 'pipix', 'huoshan', 'bilibili', 'b23' 元素是否在传进来的url中
                # 平台识别
                if mp4_url_data in start_url:
                    return num
            else:
                # msgbox.showerror(title='错误', message='视频链接地址无效，请重新输入！')
                return
        except:
            print('反爬规则已修改，请修改代码')
            return

    def requests_douyin(self, url):
        """
        获取抖音无水印链接
        :param url: start_url
        :return: 无水印链接, 标题
        """
        mp4_url = 'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={}'
        headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 9; BND-AL10 Build/HONORBND-AL10; wv) AppleWebKit/537\
                .36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 T7/11.18 lite baiduboxapp/4.12.5.10 (Baidu; P1 9)'}
        user_response = requests.get(url=url, headers=headers).url
        try:
            # 匹配视频id，返会一个列表
            user_id = re.findall(r'https://www.iesdouyin.com/share/video/(.*?)/', user_response)[0]
        except:
            print('反爬规则已修改，请修改代码')
            return
        # 拼接url，将获取的id拼接进去
        user_url = mp4_url.format(user_id)
        # 发送请求，获取json数据
        user_json = requests.get(url=user_url, headers=headers).json()
        # 提取json数据，因为json数据的本质像一个字典，$..的语法，定位到key，所对应的数据，提取出来
        douyin_url = jsonpath.jsonpath(user_json, '$..play_addr')
        # 获取视频标题
        mp4_name = jsonpath.jsonpath(user_json, '$..desc')[0]
        # 获取视频链接(有水印)
        dy_url = douyin_url[0].get('url_list')[0]
        # 字符串替换，获取无水印视频链接
        mp4_url = dy_url.replace('wm', '')
        return mp4_url, mp4_name

    def request_kuaishou(self, url):
        """
        获取快手无水印视频链接
        :param url: start_url
        :return: 无水印视频链接,标题
        """
        headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15\
                 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
                   'Cookie': 'did=web_e4581e2dbe33aae5eac3d9fdf8b12566;'}
        # 忽略警告代码
        requests.packages.urllib3.disable_warnings()
        # 第一次起始url发送请求，获取响应头的url
        mp4_response_url = requests.get(url=url, headers=headers, allow_redirects=False, verify=False).headers['Location']
        # 第二次url发送请求, 获取响应数据的文本
        mp4_two_response = requests.get(url=mp4_response_url, headers=headers, allow_redirects=False,
                                        verify=False).text
        """
                allow_redirects=False     禁止重定向
                verify=False              关闭ssl认证
        """
        # 正则匹配无水印视频链接
        mp4_url = re.findall(r'srcNoMark":"(.*?)"}', mp4_two_response)[0]
        # 正则匹配无水印视频标题
        mp4_name = re.findall(r'share":{"title":"(.*?)"', mp4_two_response)[0]
        return mp4_url, mp4_name

    def request_pipix(self, url):
        """
        获取皮皮虾无水印视频链接
        :param url: start_url
        :return: 无水印视频链接, 标题
        """
        mp4_data_url = 'https://h5.pipix.com/bds/webapi/item/detail/?item_id={}&source=share'
        # 获取视频的id
        mp4_id = re.findall(r'item/(.*?)\?', session.get(url=url).url)[0]
        # 拼接新的url地址
        start_mp4_url = mp4_data_url.format(mp4_id)
        # 获取响应的json数据
        mp4_json = session.get(start_mp4_url).json()
        # 第一次数据提取,获取视频的标题
        mp4_name = jsonpath.jsonpath(mp4_json, '$..content')[0]
        # 第二次数据提取，获取视频的链接
        mp4_one_json = jsonpath.jsonpath(mp4_json, '$..origin_video_download')
        mp4_url = jsonpath.jsonpath(mp4_one_json, '$..url')[0]
        return mp4_name, mp4_url

    def request_huoshan(self, url):
        """
        获取火山无水印链接
        :param url: start_url
        :return: mp4_name, mp4_url
        """
        headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTM\
                L, like Gecko)Chrome/83.0.4103.116 Mobile Safari/537.36'}
        mp4_data_url = 'https://share.huoshan.com/api/item/info?item_id='
        # 提取用户id
        user_id = re.findall(r'item_id=(.*?)&', requests.get(url=url, headers=headers).url)[0]
        # 拼接
        url = mp4_data_url + user_id
        # 发送请求
        response = requests.get(url=url, headers=headers, allow_redirects=False).json()
        # 获取json数据中的url
        mp4_json_url = jsonpath.jsonpath(response, '$..url')[0]
        # 字符串操作替换成无水印链接
        mp4_url = mp4_json_url.replace('_reflow', '_source').replace('watermark=2', 'watermark=0')
        try:
            # 判断输入进来的链接是否包含中文，有中文作为视频标题，没有返回为空
            mp4_name = re.findall(r'(.*?)>>http', url)[0]
        except:
            mp4_name = None
        return mp4_url, mp4_name, user_id

    def request_bilibili(self, url):
        """
        获取B站无水印链接
        :param url: start_url
        :return: mp4_name, mp4_url
        """
        # 获取html源码
        redirect_html = session.get(url=url).html.html
        try:
            # 正则匹配需要的url，即视频链接重定向的MP4_url
            redirect_url = re.findall(r'property="og:url" content="(.*?)"', redirect_html)[0]
        except:
            print('反爬规则已修改，请修改代码')
            return
        # 获取响应文本，即html源码
        response_text = session.get(url=redirect_url, headers={'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 \
        Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Mobile Safari/537.36'}).html.text
        try:
            # 正则匹配html源码中的json数据
            response_json = re.findall(r'window.__INITIAL_STATE__=(.+?);', response_text)[0]
            # 匹配无水印的url
            mp4_url = re.findall(r'"url":"(.+?)"', response_json)[0]
            # 匹配标题
            mp4_name = re.findall(r'"title":"(.+?)"', response_json)[0]
            # 因为匹配的url加过密，解密
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

    def mp4_data_save(self, mp4_url, mp4_name, user_id=None):
        headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 9; BND-AL10 Build/HONORBND-AL10; wv) AppleWebKit/537\
                .36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 T7/11.18 lite baiduboxapp/4.12.5.10 (Baidu; P1 9)'}
        # os.getcwd() 获取当前路径
        os_path = os.getcwd() + '/视频MP4/'
        if mp4_name == None:
            # 若火山视频的标题为空，拿用户视频的id拼接成标题
            mp4_name = '火山视频' + user_id
        # 判断是否存在此路径，没有就创建，有就略过
        if not os.path.exists(os_path):
            os.mkdir(os_path)
        # 获取视频的二进制数据
        mp4_data = requests.get(url=mp4_url, headers=headers).content
        with open(os_path + mp4_name + '.mp4', 'wb')as f:
            # 写入保存
            f.write(mp4_data)
            print('视频-------------{}--------------提取完成'.format(mp4_name))

    def run(self):
        num = self.start_url_judge()
        try:
            start_url, proxies = self.url_estimate()
            if num == 0:
                # 抖音
                mp4_url, mp4_name = self.requests_douyin(start_url)
                self.mp4_data_save(mp4_url, mp4_name)

            elif num == 1:
                # 快手
                mp4_url, mp4_name = self.request_kuaishou(start_url)
                self.mp4_data_save(mp4_url, mp4_name)

            elif num == 2:
                # 皮皮虾
                mp4_name, mp4_url = self.request_pipix(start_url)
                self.mp4_data_save(mp4_url, mp4_name)

            elif num == 3:
                # 火山
                mp4_url, mp4_name, user_id = self.request_huoshan(start_url)
                self.mp4_data_save(mp4_url, mp4_name, user_id)

            elif num == 4:
                # b站(电脑端链接)
                mp4_url, mp4_name = self.request_bilibili(start_url)
                self.mp4_data_save(mp4_url, mp4_name)

            elif num == 5:
                # b站(手机端链接)
                mp4_url, mp4_name = self.request_bilibili(start_url)
                self.mp4_data_save(mp4_url, mp4_name)

        except:
            msgbox.showerror(title='错误', message='视频链接地址无效，请重新输入！')
            return

    def loop(self):
        self.root.mainloop()


if __name__ == '__main__':
    dd = Aef()
    dd.loop()
