# 编码转换

from urllib.parse import quote,unquote

name = '王者荣耀'
# %E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80
print(quote(name))
print(unquote(quote(name)))

"""汉字转换拼音"""
from xpinyin import Pinyin

name = '宝宝巴士，罒罓'
p = Pinyin()
print(p.get_pinyins(name))

"""unicode编码"""
url = 'https:\u002F\u002Fupos-sz-mirrorks3.bilivideo.com\u002Fupgcxcode\u002F82\u002F70\u002F306987082\u002F306987082_nb2-1-16.mp4?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&uipk=5&nbs=1&deadline=1615111711&gen=playurl&os=ks3bv&oi=2099930370&trid=e5036b740f064dec8fd1c2e06ee1395fh&platform=html5&upsig=c86714076061f21fc870c643fca7c899&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mid=0&logo=80000000'

result = url.encode('latin-1').decode('unicode-escape')
print(result)

from urllib.parse import quote

# %u795E%u5893     神墓
# %u7388%u8005%u8363%u8000 王者荣耀

name = '王者荣耀'
result = quote(name.encode('unicode-escape'))   # %5Cu738b%5Cu8005%5Cu8363%5Cu8000
res = result.replace('%5C','%')                 # %u738b%u8005%u8363%u8000
print(res)