from urllib.request import urlretrieve

import requests,os
from jsonpath import jsonpath


class Lol(object):
    def __init__(self):
        self.url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'

        self.headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus\
                5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Mobile Safari/537.36",
                        'referer': 'https://lol.qq.com/data/info-heros.shtml'}

        self.new_url = 'https://game.gtimg.cn/images/lol/act/img/js/hero/{}.js'

    def num_list(self):
        req = requests.get(url=self.url).json()
        # 提取编号链接
        banAudios = jsonpath(req, '$..banAudio')
        # 提取编号
        # print(banAudios)
        items = []
        for banAudio in banAudios:
            id = banAudio.split("ban/")[1][0:-4]
            items.append(id)
        # print(items)
        return items

    def lol_data(self, items):
        """
        发送请求，保存数据
        :return: lol_photo
        """
        for item in items:
            url = self.new_url.format(item)
            req = requests.get(url, headers=self.headers).json()
            skins = req["skins"]
            names = jsonpath(skins, '$..name')
            mainImgs = jsonpath(req, '$..mainImg')
            try:
                # 创建文件夹
                if not os.path.exists(names[0]):
                    os.mkdir(names[0])
                    print('-------------------切换提取下一个英雄--------------------')
                # 保存图片
                for name, mainImgs in zip(names, mainImgs):
                    urlretrieve(mainImgs, names[0] + "/" + name + ".jpg")
                    print(name + " 100%")
            except:
                print('-------------------切换提取下一个英雄--------------------')

    def run(self):
        lol_num_list = self.num_list()
        self.lol_data(lol_num_list)


if __name__ == '__main__':
    lol = Lol()
    lol.run()