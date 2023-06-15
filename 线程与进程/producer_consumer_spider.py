import random
import threading
import time
import queue
import Blog_Spider

from requests.packages import urllib3
urllib3.disable_warnings()


def do_craw(url_queue:queue.Queue,html_queue:queue.Queue):
    while True:
        url = url_queue.get()
        html = Blog_Spider.craw(url)
        html_queue.put(html)
        print(threading.current_thread().name,f"craw{url}",
              "url_queue.size=",url_queue.qsize())

        time.sleep(random.randint(1,2))

def do_parse(html_queue:queue.Queue,fout:open):

    while True:
        html = html_queue.get()
        results = Blog_Spider.parse(html)
        for result in results:
            fout.write(str(result)+"\n")
        print(threading.current_thread().name,f'results.size',len(results),
              "html_queue.size=",html_queue.qsize())

        time.sleep(random.randint(1,2))

if __name__ == '__main__':
    q = queue.Queue()
    url_queue = queue.Queue()
    html_queue = queue.Queue()
    res_queue = queue.Queue()

    for url in Blog_Spider.urls:
        url_queue.put(url)

    for idx in range(4):
        t = threading.Thread(target=do_craw,args = (url_queue,html_queue),
                             name=f"craw{idx}")
        t.start()

    fout = open('data.csv','w')
    for idx in range(3):
        t = threading.Thread(target=do_parse,args = (html_queue,fout),
                             name=f"craw{idx}")
        t.start()


