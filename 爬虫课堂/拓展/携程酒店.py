from requests_html import HTMLSession
from fake_useragent import UserAgent
import json
from jsonpath import jsonpath

ua = UserAgent()
session = HTMLSession()
#        https://m.ctrip.com/restapi/soa2/16709/json/GetReviewList
s_url = 'https://m.ctrip.com/restapi/soa2/16709/json/GetReviewList'
headers = {
    # 'p': ' 12103528347',
    'cookie': 'ibulanguage=CN; ibulocale=zh_cn; cookiePricesDisplayed=CNY; _RF1=125.42.101.2; _RSG=_xK9fLFCUg8ADwiaKim0Z8; _RDG=28e5de85209de024da18bc22723d546d6d; _RGUID=8a9e30f5-6925-4eff-88c0-c2c524b3a34a; _ga=GA1.2.1985365426.1617424218; _gid=GA1.2.814582032.1617424218; Union=OUID=&AllianceID=4897&SID=167093&SourceID=&createtime=1617424218&Expires=1618029017697; MKT_OrderClick=ASID=4897167093&AID=4897&CSID=167093&OUID=&CT=1617424217699&CURL=https%3A%2F%2Fhotels.ctrip.com%2F%3Fallianceid%3D4897%26sid%3D167093%26bd_vid%3D7346321128338400365%26keywordid%3D113712038226&VAL={"pc_vid":"1617424213234.12w1wc"}; MKT_Pagesource=PC; MKT_CKID=1617424217803.5bolg.isvg; MKT_CKID_LMT=1617424217804; _abtest_userid=9c385891-10d9-475f-b53e-1604e6a5acbc; intl_ht1=h4=2_458349; _bfa=1.1617424213234.12w1wc.1.1617424213234.1617424213234.1.4; _bfs=1.4; _bfi=p1%3D102003%26p2%3D102003%26v1%3D4%26v2%3D3; _jzqco=%7C%7C%7C%7C1617424295126%7C1.1502902650.1617424217726.1617424339824.1617424737887.1617424339824.1617424737887.0.0.0.4.4; __zpspc=9.1.1617424217.1617424737.4%232%7Cwww.baidu.com%7C%7C%7C%7C%23; appFloatCnt=4; Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c=1617425026; Hm_lpvt_eaa57ca47dacb4ad4f5a257001a3457c=1617425063',
    'referer': 'https://hotels.ctrip.com/',
    'origin': 'https://hotels.ctrip.com',
    'user-agent': ua.chrome,
}
for i in range(10):
    data = {"PageNo": f'{i}', "PageSize": 10, "MasterHotelId": 458349, "NeedFilter": 'true', "UnUsefulPageNo": 1,
            "UnUsefulPageSize": 5, "isHasFold": 'false',
            "head": {"Locale": "zh-CN", "Currency": "CNY", "Device": "PC", "UserIP": "125.42.101.2", "Group": "",
                     "ReferenceID": "", "UserRegion": "CN", "AID": "4897", "SID": "167093", "Ticket": "", "UID": "",
                     "IsQuickBooking": "", "ClientID": "1617424213234.12w1wc", "OUID": "", "TimeZone": "8",
                     "P": "12103528347", "PageID": "102003", "Version": "",
                     "HotelExtension": {"WebpSupport": 'true', "group": "CTRIP", "Qid": 'null', "hasAidInUrl": 'false'},
                     "Frontend": {"vid": "1617424213234.12w1wc", "sessionID": 2, "pvid": 5}}, "ServerData": ""}
    data = json.dumps(data).encode(encoding='utf-8')
    resp = session.post(s_url, headers=headers,data=data).json()
    reviewContent_l = jsonpath(resp,'$..reviewContent')
    print(reviewContent_l)
    break
