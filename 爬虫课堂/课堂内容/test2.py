# import requests
# from urllib.parse import quote, unquote
#
#
# title = input('请输入贴吧名称：')
# page = input('你想爬取多少页，请输入页码：')
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
#     'Host': 'tieba.baidu.com',
#     'Upgrade-Insecure-Requests': '1'
# }
#
# # 1.准备起始的url地址
# for num in range(int(page)):
#     start_url = f'https://tieba.baidu.com/f?kw={quote(title)}&pn={50 * num}'
#     # print(start_url)
#     # start_url_1 = 'https://tieba.baidu.com/f?kw=' + quote(title)
#     # start_url_2 = ''.join(['https://tieba.baidu.com/f?kw=', quote(title)])
#     # print(start_url_2)
#     # 2.发送请求，获取响应
#     response = requests.get(start_url, headers=headers)
#
#     # 3.解析响应，数据提取
#     data = response.content.decode()
#     # 4.保存数据
#     # print(data)
#     with open(title + '_' + str(num) + '.html', 'w')as f:
#         f.write(data)
#     print(f'{title}----贴吧---第{num+1}页保存完成')


str = """
<lxml version="1.0" encoding="utf-8"?>

<bookstore> 

  <book category="cooking"> 
    <title lang="en">Everyday Italian</title>  
    <author>Giada De Laurentiis</author>  
    <year>2005</year>  
    <price>30.00</price> 
  </book>  

  <book category="children"> 
    <title lang="en">Harry Potter</title>  
    <author>J K. Rowling</author>  
    <year>2005</year>  
    <price>29.99</price> 
  </book>  

  <book category="web"> 
    <title lang="en">XQuery Kick Start</title>  
    <author>James McGovern</author>  
    <author>老王同学</author>  
    <author>Kurt Cagle</author>  
    <author>James Linn</author>  
    <author>Vaidyanathan Nagarajan</author>  
    <year>2003</year>  
    <price>49.99</price> 
  </book> 

  <book category="web" cover="paperback"> 
    <title lang="en">Learning XML</title>  
    <author>Erik T. Ray</author>  
    <year>2003</year>  
    <price>39.95</price> 
  </book> 

</bookstore>
"""
# from lxml import etree
# # 通过lxml转换为具有xpath语法熟悉的对象
# html = etree.HTML(str)
# data = html.xpath('.//book[@category="web"]/author[2]/text()')
#
# print(data)


a = '1'.join('abc')

print(a)











