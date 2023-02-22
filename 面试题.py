# class Bike:
#     def __init__(self,newWheel,newColor):
#         self.whellNum = newWheel
#         self.color = newColor
#
#     def move(self):
#         print('车会跑')
#
# # 创建对象
# BM = Bike(2,'green')
#
# print('车的颜色为：%s'%BM.color)
# print('车轮的数量为：%d'%BM.whellNum)

class A(object):
    def __init__(self):
        print('这是init方法',self)


    def __new__(cls):
        print('这是cls的ID',id(cls))
        print('这是new方法',object.__new__(cls))
        return object.__new__(cls)


# A()
# print('这是类A的ID',id(A))

# li = [1,2,3,6,7]
# def fn(x):
#     return x*2
# res = map(fn,li)
# print(list(res))

# import random
# import numpy as np
# r1 = random.randint(10,20)
# res = np.random.randn(5)
# res1 = random.random()
# print("正整数",r1)
# print('5个随机小数',res)
# print('0-1随机小数',res1)

# import re
#
# str = '<div class="nam">中国</div>'
#
# res = re.findall('>(.*)<',str)
# print(res)

# a = 3
# assert (a>2)
# print('断言成功，则程序继续执行')
# assert (a>5)
# print('断言失败，则程序报错')

# s = "ajldjlajfdljfddd"
# li = list(s)
# dic = set(li)
# print(dic)
# lis = list(dic)
# lis.sort()
# print(lis)

# sum=lambda a,b:a*b
# print(sum(5,4))

# dic={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}
# print(dic.items())
# lis = sorted(dic.items(),key=lambda i:i[0],reverse=False)
# print(dict(lis))

# from collections import Counter
# a = 'kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h'
# res = Counter(a)
# print(res)

import re

# a = "not 404 found 张三 99 深圳"
# li = a.split(' ')
#
# print(li)
# res = re.findall('\d+|[a-zA-Z]+',a)
#
# for i in res:
#     if i in li:
#         li.remove(i)
# new_str = ' '.join(li)
# print(res)
# print(new_str)

# from requests_html import HTMLSession
# session = HTMLSession()
# headers = {
#     # 'Cookie': 'll="118253"; bid=xqs0FXhww0Y; push_doumail_num=0; push_noty_num=0; __utmv=30149280.20258; __yadk_uid=DuOv3M3F7FQbuYMquXE7LeNRpDJq53SJ; _vwo_uuid_v2=DD42CE6C9A26A335DDDE074D748EC40F9|6ead799357458bd16dee7e253e0cc5ea; _ga=GA1.2.1558427072.1614751770; _vwo_uuid_v2=DD42CE6C9A26A335DDDE074D748EC40F9|6ead799357458bd16dee7e253e0cc5ea; __gads=ID=3a65c91ee7feec11-226dbf21fbc60007:T=1617357101:RT=1617357101:S=ALNI_MYe8fKZ-TVxIb5ws6q-N3ZVaDp5eA; __utmc=30149280; __utmc=223695111; dbcl2="202580961:yza/lZZ7S2A"; ck=y1nC; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1618115801%2C%22https%3A%2F%2Faccounts.douban.com%2F%22%5D; _pk_id.100001.4cf6=11d765d8242ca2b5.1614752851.5.1618115801.1618110993.; _pk_ses.100001.4cf6=*; Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c=1617537899,1618108283,1618109817,1618115801; Hm_lpvt_eaa57ca47dacb4ad4f5a257001a3457c=1618115801; __utma=30149280.1558427072.1614751770.1618108282.1618115801.9; __utmb=30149280.0.10.1618115801; __utmz=30149280.1618115801.9.5.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=223695111.381968087.1614752851.1618108282.1618115801.5; __utmb=223695111.0.10.1618115801; __utmz=223695111.1618115801.5.4.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/',
#     'Host': 'movie.douban.com',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
# }
#
# s_url = 'https://movie.douban.com/subject/1652587/'
# res = session.get(s_url,headers=headers)
# print(res.html)
# tt = res.html.xpath('//*[@id="content"]/h1/span[1]/text()')
# yy = res.html.xpath('//*[@id="info"]/span[3]/span[2]/span[1]/a/text()')
# print(tt,yy)

# a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def fn(a):
#     return a%2==1
# newlist = filter(fn,a)
# newlist=[i for i in newlist]
# print(newlist)
#
# res = [i for i in a if i%2==1 ]
# print(res)

# import re
#
# content ='''Hello 1234567 World_This
# is a Regex Demo'''
# pattern = re.compile('Hello.*Demo',re.S)
# result = re.match(pattern,content)
# #result = re.match('Hello.*Demo',content,re.S)
# print(result)


# l = [1,5,7,9]
# l1 = [2,2,6,8]
# l2 = l + l1
#
# l2.sort()
# print(l)
#
# l = [1,5,7,9]
# l1 = [2,2,6,8]
# l.extend(l1)
#
# print(l)

# import datetime
# a = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))+'  星期：'+str(datetime.datetime.now().isoweekday())
#
# print(a)

def fnu():
    try:
        for i in range(5):
            if i>2:
                raise Exception('数字大于2了')
    except Exception as ret:
        print(ret)

# fnu()
# import re
# s = '<a>哈哈</a><a>嘿嘿</a>'
# res1=re.findall('<a>(.*)</a>',s)
# print('贪婪模式',res1)
#
# res2 = re.findall('<a>(.*?)</a>',s)
# print('非贪婪模式',res2)

# a = [[1,2],[3,4],[5,6]]
# li = [j for i in a for j in i]
# print(li)
#
# import numpy as np
# # .tolist()
# b = np.array(a).flatten().tolist()
# print(b)

# import os
# x="abc"
# y="def"
# z=["d","e","f"]
# j1 = x.join(y)
# j2 = x.join(z)
# # print(j1,j2)
# j3 = os.path.join('./爬虫课堂/','星空.html')
# print(j3)

# li_1 = [1,2,3,4,5]
# # 枚举法
# for num,data in enumerate(li_1):
#     print(num,data)
#
# from requests_html import HTMLSession
# session = HTMLSession()
#
# url = 'https://hr.163.com/position/list.do?currentPage=1'
# resp = session.get(url)
#
# t = resp.html.xpath('//*[@id="position-table-29240"]/tbody/tr[1]/td[1]/a/@href/text()')
# l = resp.html.xpath('//*[@id="position-table-77992"]/tbody/tr[1]/td[1]/a/text()')
# #                    //*[@id="position-table-77992"]/tbody/tr[1]/td[1]/a
# print(t,l)

# a = "  hehheh  "
# print([a.strip()])

# foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
# # # foo.sort()
# # a = sorted(foo,key = lambda x:x)
# # print(a)

# f1 = [{"name":"zs","age":19},{"name":"ll","age":54},
#
#         {"name":"wa","age":17},{"name":"df","age":23}]
#
# a = sorted(f1,key=lambda x:x['age'],reverse=True)
# print(a)
# a = sorted(f1,key=lambda x:x['name'])
# print(a)
my_list = ['','ade',123,[],{},{'asd':'dada'},(1,2),(),{1,2,3}]
"""
参数说明：
第一个参数，自己定义的过滤函数，没有传None：代表过滤掉为空的数据
"""
# result = filter(None,my_list)
# for i in result:
#     print(i)

from time import ctime, sleep


def timefun(func):
    def wrappedfunc():
        print("%s called at %s" % (func.__name__, ctime()))
        return func()

    return wrappedfunc


@timefun
def foo():
    print("I am foo")
# foo()


# A = {'b':1,'c':2}
# print(A.get('b'))
# print(A['b'])

# A='abcdefg'
# t = list(A)
# l = len(t)
# for i, j in zip(range(l - 1, 0, -1), range(l // 2)):
#     print(i,j)
#     t[i], t[j] = t[j], t[i]
# print("".join(t))

def fibo(num):
    numList = [0,1]
    for i in range(num - 2):
        numList.append(numList[-2] + numList[-1])
    return numList

a = fibo(10)
print(a)
