
import concurrent.futures
import Blog_Spider

# craw
with concurrent.futures.ThreadPoolExecutor() as pool:
    htmls = pool.map(Blog_Spider.craw,Blog_Spider.urls)
    htmls_li = list(zip(Blog_Spider.urls,htmls))
    for url,html in htmls_li:
        print(url,len(html.html))

print("craw over")
# parse

with concurrent.futures.ThreadPoolExecutor() as pool:
    futures = {}
    for url,html in htmls_li:
        future = pool.submit(Blog_Spider.parse,html)
        futures[future] = url

    # for future,url in futures.items():
    #     print(url,future.result())

    # as_completed 更加强大
    for future in concurrent.futures.as_completed(futures):
        url = futures[future]
        print(url,future.result())
