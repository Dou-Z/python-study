from requests_html import HTMLSession
from fake_useragent import UserAgent
import js2py,re
ua = UserAgent()
session = HTMLSession()


class BDSpider(object):

    def __init__(self):
        self.title = input('请输入需要翻译的信息：')
        self.url_1 = 'https://fanyi.baidu.com/langdetect'
        self.url_2 = 'https://fanyi.baidu.com/v2transapi?from={}&to={}'
                    # https://fanyi.baidu.com/v2transapi?from=en&to=zh
        self.headers = {
            'Host': 'fanyi.baidu.com',
            'Origin': 'https://fanyi.baidu.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
        }

    def parse_start_response(self):
        """

        :return:
        """
        data = {
            'query': self.title
        }
        resp_json = session.post(self.url_1, headers=self.headers, data=data).json()
        lan = resp_json['lan']
        self.parse_next_response(lan)

    def parse_next_response(self, lan):
        """
        解析翻译
        :param lan: 语言种类
        :return:
        """

        """获取token"""
        headers = {
            'Host': 'fanyi.baidu.com',
            'Cookie': 'BIDUPSID=B1B832BDC0B9036697CBAE56A3819AC0; PSTM=1616679045; BAIDUID=B1B832BDC0B90366E4545AA225C26525:FG=1; delPer=0; PSINO=7; H_PS_PSSID=33636_33261_33344_31660_33693_33675_33392_26350_33731; BA_HECTOR=0k01008hagag8h818n1g5p4470r; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BCLID=8626351770282071039; BDSFRCVID=53LOJexroG3VC55eV39aIGgTgFweG7bTDYLtOwXPsp3LGJLVJeC6EG0Pts1-dEu-EHtdogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tR3aQ5rtKRTffjrnhPF3htA3XP6-hnjy3b7p5K5l5xL5bDoVQPJxbUKWbttf5q3RymJ42-39LPO2hpRjyxv4y4Ldj4oxJpOJ-bCL0p5aHl51fbbvbURvD--g3-AqBM5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIEoCvt-5rDHJTg5DTjhPrMhfvJWMT-MTryKKOC0K5GefLRej5zQP-7bPjfKx-fKHnRhlRNB-3iV-OxDUvnyxAZyxomtfQxtNRJQKDE5p5hKq5S5-OobUPUDMJ9LUkqW2cdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLtCvDqTrP-trf5DCShUFst6JrB2Q-XPoO3KO4EIKGbqD5et_PQUJnKM5f5mkf3fbgylRM8P3y0bb2DUA1y4vpBtQmJeTxoUJ2-KDVeh5Gqfo15-0ebPRiJPb9Qg-qahQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0HPonHj_5jjO03H; BCLID_BFESS=8626351770282071039; BDSFRCVID_BFESS=53LOJexroG3VC55eV39aIGgTgFweG7bTDYLtOwXPsp3LGJLVJeC6EG0Pts1-dEu-EHtdogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tR3aQ5rtKRTffjrnhPF3htA3XP6-hnjy3b7p5K5l5xL5bDoVQPJxbUKWbttf5q3RymJ42-39LPO2hpRjyxv4y4Ldj4oxJpOJ-bCL0p5aHl51fbbvbURvD--g3-AqBM5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIEoCvt-5rDHJTg5DTjhPrMhfvJWMT-MTryKKOC0K5GefLRej5zQP-7bPjfKx-fKHnRhlRNB-3iV-OxDUvnyxAZyxomtfQxtNRJQKDE5p5hKq5S5-OobUPUDMJ9LUkqW2cdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLtCvDqTrP-trf5DCShUFst6JrB2Q-XPoO3KO4EIKGbqD5et_PQUJnKM5f5mkf3fbgylRM8P3y0bb2DUA1y4vpBtQmJeTxoUJ2-KDVeh5Gqfo15-0ebPRiJPb9Qg-qahQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0HPonHj_5jjO03H; __yjs_duid=1_b75ae51ad2974995196a273cb1f02d9f1616679047363; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1616679048; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_PREFER_SWITCH=1; SOUND_SPD_SWITCH=1; BDUSS=zFvUjRqOWtEd1VyZDB6NjZuWnU1T0F6TnpSQzQxNlNZSFpRcjFwNkRoM1pJb1JnRVFBQUFBJCQAAAAAAAAAAAEAAADB7szat~y12Na0t6i52QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANmVXGDZlVxgd; BDUSS_BFESS=zFvUjRqOWtEd1VyZDB6NjZuWnU1T0F6TnpSQzQxNlNZSFpRcjFwNkRoM1pJb1JnRVFBQUFBJCQAAAAAAAAAAAEAAADB7szat~y12Na0t6i52QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANmVXGDZlVxgd; __yjsv5_shitong=1.0_7_6470de95c79259cd83793e8974ae69831657_300_1616680412079_175.9.142.188_e05e1274; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1616680422; ab_sr=1.0.0_MGFhYzliODIzODBmZTFmNWZhNWRjZDQ5ZDFhNGIyNDY1NTcwY2IxNmM3M2VlZWI1ZDM2NTEyNDMxZWRhYmM2ZDYzYzFlNjNlMjhhZDRlMDcyN2M0NGJhZDUyZjViZGI0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
        }
        token_url = 'https://fanyi.baidu.com/'
        res = session.get(token_url, headers=headers).content.decode()
        # print(res)
        token = re.findall("bdstoken = '(.*?)'", res)[0]
        """生成sign"""
        js = js2py.EvalJs()
        with open('1.js', 'r')as f:
            js.execute(f.read())

        to_data = 'en' if lan == 'zh' else 'zh'
        start_url = self.url_2.format(lan, to_data)
        data = {
            'from': lan,
            'to': to_data,
            'query': self.title,
            'transtype': 'realtime',
            'simple_means_flag': '3',
            'sign': js.e(self.title),
            'token': token,
            'domain': 'common'
        }
        print(data)
        headers_1 = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            # 'Content-Length': '134',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'Cookie': 'BIDUPSID=B1B832BDC0B9036697CBAE56A3819AC0; PSTM=1616679045; BAIDUID=B1B832BDC0B90366E4545AA225C26525:FG=1; delPer=0; PSINO=7; H_PS_PSSID=33636_33261_33344_31660_33693_33675_33392_26350_33731; BA_HECTOR=0k01008hagag8h818n1g5p4470r; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BCLID=8626351770282071039; BDSFRCVID=53LOJexroG3VC55eV39aIGgTgFweG7bTDYLtOwXPsp3LGJLVJeC6EG0Pts1-dEu-EHtdogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tR3aQ5rtKRTffjrnhPF3htA3XP6-hnjy3b7p5K5l5xL5bDoVQPJxbUKWbttf5q3RymJ42-39LPO2hpRjyxv4y4Ldj4oxJpOJ-bCL0p5aHl51fbbvbURvD--g3-AqBM5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIEoCvt-5rDHJTg5DTjhPrMhfvJWMT-MTryKKOC0K5GefLRej5zQP-7bPjfKx-fKHnRhlRNB-3iV-OxDUvnyxAZyxomtfQxtNRJQKDE5p5hKq5S5-OobUPUDMJ9LUkqW2cdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLtCvDqTrP-trf5DCShUFst6JrB2Q-XPoO3KO4EIKGbqD5et_PQUJnKM5f5mkf3fbgylRM8P3y0bb2DUA1y4vpBtQmJeTxoUJ2-KDVeh5Gqfo15-0ebPRiJPb9Qg-qahQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0HPonHj_5jjO03H; BCLID_BFESS=8626351770282071039; BDSFRCVID_BFESS=53LOJexroG3VC55eV39aIGgTgFweG7bTDYLtOwXPsp3LGJLVJeC6EG0Pts1-dEu-EHtdogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tR3aQ5rtKRTffjrnhPF3htA3XP6-hnjy3b7p5K5l5xL5bDoVQPJxbUKWbttf5q3RymJ42-39LPO2hpRjyxv4y4Ldj4oxJpOJ-bCL0p5aHl51fbbvbURvD--g3-AqBM5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIEoCvt-5rDHJTg5DTjhPrMhfvJWMT-MTryKKOC0K5GefLRej5zQP-7bPjfKx-fKHnRhlRNB-3iV-OxDUvnyxAZyxomtfQxtNRJQKDE5p5hKq5S5-OobUPUDMJ9LUkqW2cdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLtCvDqTrP-trf5DCShUFst6JrB2Q-XPoO3KO4EIKGbqD5et_PQUJnKM5f5mkf3fbgylRM8P3y0bb2DUA1y4vpBtQmJeTxoUJ2-KDVeh5Gqfo15-0ebPRiJPb9Qg-qahQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0HPonHj_5jjO03H; __yjs_duid=1_b75ae51ad2974995196a273cb1f02d9f1616679047363; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1616679048; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_PREFER_SWITCH=1; SOUND_SPD_SWITCH=1; BDUSS=zFvUjRqOWtEd1VyZDB6NjZuWnU1T0F6TnpSQzQxNlNZSFpRcjFwNkRoM1pJb1JnRVFBQUFBJCQAAAAAAAAAAAEAAADB7szat~y12Na0t6i52QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANmVXGDZlVxgd; BDUSS_BFESS=zFvUjRqOWtEd1VyZDB6NjZuWnU1T0F6TnpSQzQxNlNZSFpRcjFwNkRoM1pJb1JnRVFBQUFBJCQAAAAAAAAAAAEAAADB7szat~y12Na0t6i52QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANmVXGDZlVxgd; __yjsv5_shitong=1.0_7_6470de95c79259cd83793e8974ae69831657_300_1616680412079_175.9.142.188_e05e1274; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1616680422; ab_sr=1.0.0_MGFhYzliODIzODBmZTFmNWZhNWRjZDQ5ZDFhNGIyNDY1NTcwY2IxNmM3M2VlZWI1ZDM2NTEyNDMxZWRhYmM2ZDYzYzFlNjNlMjhhZDRlMDcyN2M0NGJhZDUyZjViZGI0',
            'Host': 'fanyi.baidu.com',
            'Origin': 'https://fanyi.baidu.com',
            # 'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
            'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
            # 'sec-ch-ua-mobile': '?0',
            # 'Sec-Fetch-Dest': 'empty',
            # 'Sec-Fetch-Mode': 'cors',
            # 'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
        response_json = session.post(start_url, headers=headers_1, data=data)
        self.parse_data(response_json.json())

    def parse_data(self, data_json):
        # "trans_result":{"data":[{"dst"
        print(data_json)
        data = data_json['trans_result']['data'][0]['dst']
        print(data)


if __name__ == '__main__':
    b = BDSpider()
    b.parse_start_response()