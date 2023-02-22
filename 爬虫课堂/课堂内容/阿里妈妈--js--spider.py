"""阿里妈妈"""
# 找工厂 / 1688首页
# https://factory.1688.com/zgc/page/tyg1c639.html?__pageId__=170307&cms_id=170307&keywords=%E5%B9%BF%E5%B7%9E%E9%A3%9F%E5%93%81&spm=a260k.19776607.0.0
# 工厂名片
# https://show.1688.com/shili/factory/shop.html?spm=a260k.21129858.kj9mj3wz.2.77557c124UThsT&__pageId__=99183&cms_id=99183&facMemId=zheng669
# https://show.1688.com/shili/factory/shop.html?spm=a260k.21129858.kj9mj3wz.6.77557c12U0bE7r&__pageId__=99183&cms_id=99183&facMemId=b2b-220648820161839cd8
# 进旺铺

# https://haoweilai.1688.com/?spm=a262cb.19918180.khuur57j.9.74913cb7Hee3uS
# https://lailihong.1688.com/?spm=a262cb.19918180.khuur57j.11.1a3f3cb7QFQ9hK
# https://shop244r7263h80r8.1688.com/?spm=a262cb.19918180.khuur57j.11.51b93cb77duKkQ

# https://haoweilai.1688.com/page/contactinfo.htm?spm=a2615.2177701.autotrace-topNav.9.6f1f7009Je1oIY  联系方式
# 翻页，工厂列表
# https://widget.1688.com/front/getJsonComponent.json?callback=jQuery1830035052988276674135_1616917226131&dmtrack_pageid=77557c12HuKwPH&namespace=TpFacSearchService&widgetId=TpFacSearchService&methodName=execute&params=%7B%22pageNo%22%3A1%2C%22query%22%3A%22q%3D%E5%B9%BF%E5%B7%9E%E9%A3%9F%E5%93%81%22%2C%22pageSize%22%3A20%2C%22from%22%3A%22PC%22%2C%22showType%22%3A%22transverse%22%2C%22sort%22%3A%22mix%22%7D&pageNo=1&query=q%3D%E5%B9%BF%E5%B7%9E%E9%A3%9F%E5%93%81&pageSize=20&from=PC&showType=transverse&sort=mix&_tb_token_=e3d53e4383ee9&_=1616917226846
"""
callback: jQuery1830035052988276674135_1616917226131
dmtrack_pageid: 77557c12HuKwPH
# namespace: TpFacSearchService
# widgetId: TpFacSearchService
# methodName: execute
params: {"pageNo":1,"query":"q=广州食品","pageSize":20,"from":"PC","showType":"transverse","sort":"mix"}
pageNo: 1
# query: q=广州食品
# pageSize: 20
# from: PC
# showType: transverse
# sort: mix
# _tb_token_: e3d53e4383ee9
_: 1616917226846
"""

# 工厂名片
"""
jsv: 2.5.8
appKey: 12574478
t: 1616921727838
sign: 732938e7e4fe1f8a81369b9bf13442f7
api: mtop.taobao.widgetService.getJsonComponent
v: 1.0
ecode: 1
type: jsonp
isSec: 0
timeout: 20000
dataType: jsonp
callback: mtopjsonp2
data: {"cid":"ShopCatalogMediaRecommendServiceWidget:ShopCatalogMediaRecommendServiceWidget","methodName":"execute","params":"{\"extParam\":{\"page\":1,\"pageSize\":20,\"factoryMemberId\":\"zheng669\",\"categoryId\":\"0\",\"offerType\":\"all\",\"isReturnSingleMedia\":\"Y\"}}"}
"""
data = {
    'i':'12574478',
    'g':'',
    'token':'dedf9f4773bd85fb32a7970350e399d3',
    'c_data':''
}
from urllib.parse import quote,unquote

gongC = '%E5%B9%BF%E5%B7%9E%E9%A3%9F%E5%93%81'
query = '%3A%22q%3D%E5%B9%BF%E5%B7%9E%E9%A3%9F%E5%93%81%22%2C%22'
d = unquote(query)
print(d)