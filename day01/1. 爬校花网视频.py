import requests
import re
import time
import hashlib
from concurrent.futures import ThreadPoolExecutor # 线程池
from threading import current_thread

pool = ThreadPoolExecutor(50)
movie_path = r'/Users/macbookpro/desktop/movie_path'
def get_page(url):
    """获取要访问的网站"""
    # print('get_page===%s get %s'%(current_thread().getName(),url))
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except Exception as e :
        print(e)

def parse_index(res):
    """
    获取索引
    该函数里面的res参数，是在main函数里面，submit最后有个回调函数。
    回调函数会拿到当前返回值。
    """

    index_page = res.result()
    # print('index_page===',index_page)
    # print('parse_index===%s parse_index'%current_thread().getName())
    urls = re.findall('class="items".*?<a href="(.*?)"',index_page,re.S)
    # print('parse_inde_urls==',urls)
    for detail_url in urls:
        if not detail_url.startswith('http'):
            detail_url = 'http://www.xiaohuar.com'+detail_url
            # print(detail_url)
        pool.submit(get_page,detail_url).add_done_callback(parse_detail)

def parse_detail(detail_page):
    """parse_detail"""
    detail_page1 = detail_page.result()
    # print('detail_page===',detail_page)
    l = re.findall('id="media".*?src="(.*?)"',detail_page1,re.S)
    # print(l)
    if l :
        movie_url = l[0]
        if movie_url.endswith('mp4'):


            pool.submit(get_movie,movie_url)

def get_movie(url):
    print('=====================')
    try:
        response = requests.get(url)
        print('response===',response)
        if response.status_code == 200:
            m = hashlib.md5()
            m.update(str(time.time().encode('utf-8')))
            m.update(url.encode('utf-8'))
            filepath = '%s\%s.mp4'%(movie_path,m.hexdigest())
            print('%s 开始下载'%url)
            with open(filepath,'wb') as f :
                f.write(response.text)
                print('%s 下载成功' %url)
    except Exception as e :
        print(e)
# def save():
#     """获取的数据你要保存在哪"""
#     pass

def main():
    """执行函数"""
    base_url = 'http://www.xiaohuar.com/list-3-{page_num}.html'
    for i in range(5):
        url = base_url.format(page_num=i)
        print(url,'-----')
        pool.submit(get_page,url).add_done_callback(parse_index)

if __name__ == '__main__':
    main()



