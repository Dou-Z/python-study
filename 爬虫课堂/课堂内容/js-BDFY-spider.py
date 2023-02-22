# 百度翻译

# https://fanyi.baidu.com/v2transapi?from=zh&to=en
# https://fanyi.baidu.com/、

from requests_html import HTMLSession
from fake_useragent import UserAgent
from jsonpath import jsonpath
import js2py,re
ua = UserAgent()
session = HTMLSession()

class BDspider(object):
    def __init__(self):
        self.token_url = 'https://fanyi.baidu.com/'
        self.fanyi_url = 'https://fanyi.baidu.com/v2transapi?from={}&to={}'
        self.lan_url = 'https://fanyi.baidu.com/langdetect'
        self.headers = {
            'user-agent':ua.chrome,
            'Referer': 'https://fanyi.baidu.com/',
            'Cookie': 'BIDUPSID=3AEC181C78A235ACD9FF3D299B73B19C; PSTM=1604912256; BAIDUID=00306FF4360B3E83778807ABC43B68C3:FG=1; ab_jid_BFESS=ccbc71024a4d58cadd699432fca03642cd1d; ab_jid=ccbc71024a4d58cadd699432fca03642cd1d; __yjs_duid=1_31df1dac7850d22e11891be962dc43ab1614323494714; BDUSS=mJTd0dPWTJiVnF5RjYyTlA5bW1wYmZKSm1RSzc0ZXBuckl3WENma1NFd0YwSE5nRVFBQUFBJCQAAAAAAAAAAAEAAAC4B~rG1NrExMnPsODBywAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAVDTGAFQ0xgS; BDUSS_BFESS=mJTd0dPWTJiVnF5RjYyTlA5bW1wYmZKSm1RSzc0ZXBuckl3WENma1NFd0YwSE5nRVFBQUFBJCQAAAAAAAAAAAEAAAC4B~rG1NrExMnPsODBywAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAVDTGAFQ0xgS; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BAIDUID_BFESS=00306FF4360B3E83778807ABC43B68C3:FG=1; ab_sr=1.0.0_YTIxYzRkMzU4MTI0OWEwZmQxODVhYTIxMjVlNWI3OTdmOGQwMmJhYjUyY2M0YWIyNjg0Mzg1NTk3MWU3MWRiNmMxOTI4MzQ1MmViNmM2MGZhYmJkYjljNDE4YjQ5MmVi; __yjsv5_shitong=1.0_7_e6e656a85eeafcffdfb82a1a2e24cf8b5ae8_300_1616899098645_125.42.101.2_a3d28195'
        }
        self.title = input('输入翻译内容：')
        self.data = {
            'query':self.title
        }

    def start_spider(self):
        resp_1 = session.get(self.token_url,headers=self.headers).content.decode()


        token = re.findall("token: '(.*?)'",resp_1)[0]
        # print(token)
        js = js2py.EvalJs()
        with open('baidu.js', 'r')as f:
            js_net = f.read()
        # js_net 是js的代码
        js.execute(js_net)
        str_title = self.title
        sign = js.e(str_title)

        self.response_data(token,sign)


    def response_data(self,token,sign):
        resp_2 = session.post(self.lan_url, headers=self.headers, data=self.data).json()
        # print(resp_2['lan'])
        to_data = 'en' if resp_2['lan'] == 'zh' else 'zh'
        data1 = {
            'from': resp_2['lan'],
            'to': to_data,
            'query': self.title,
            'simple_means_flag': '3',
            'sign': sign,
            'token': token,
            'domain': 'common',
        }
        next_url = self.fanyi_url.format(resp_2['lan'],to_data)
        resp_3 = session.post(next_url,headers=self.headers,data=data1).json()
        data_FY = jsonpath(resp_3,'$..dst')[0]
        print('翻译结果：',data_FY)



if __name__ == '__main__':
    B = BDspider()
    B.start_spider()


