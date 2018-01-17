from concurrent.futures import ThreadPoolExecutor
import queue
import requests
import re
import time
import hashlib
from threading import current_thread

photo_path = r'/Users/macbookpro/desktop/Unplash/'

p = ThreadPoolExecutor(20)

def get_page(url):
    # print('%s GET %s' % (current_thread().getName(), url))
    """
    <concurrent.futures.thread.ThreadPoolExecutor object at 0x102a50828>_0 GET https://unsplash.com/
<concurrent.futures.thread.ThreadPoolExecutor object at 0x102a50828>_0 GET https://unsplash.com/
<concurrent.futures.thread.ThreadPoolExecutor object at 0x102a50828>_0 GET https://unsplash.com/
<concurrent.futures.thread.ThreadPoolExecutor object at 0x102a50828>_1 GET https://unsplash.com/
<concurrent.futures.thread.ThreadPoolExecutor object at 0x102a50828>_0 GET https://unsplash.com/
<concurrent.futures.thread.ThreadPoolExecutor object at 0x102a50828>_2 GET https://unsplash.com/
<concurrent.futures.thread.ThreadPoolExecutor object at 0x102a50828>_1 GET https://unsplash.com/
<concurrent.futures.thread.ThreadPoolExecutor object at 0x102a50828>_3 GET https://unsplash.com/
<concurrent.futures.thread.ThreadPoolExecutor object at 0x102a50828>_0 GET https://unsplash.com/
<concurrent.futures.thread.ThreadPoolExecutor object at 0x102a50828>_4 GET https://unsplash.com/
    :param url:
    :return:
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
    except Exception as e:
        print('error😳😳😳',e)

def parse_images(res): # 这里的res就是get_page的返回值
    # print('%s parse_index🤖🤖🤖'%current_thread().getName())
    res = res.result()
    # print(res)
    obj = re.compile('<meta property="og:image" content="(.*?)">',re.S)
    image_urls = obj.findall(res.decode('utf-8'))
    print(image_urls)

    for image_url in image_urls:
        with open('image.txt','a') as f :
            f.write('%s\n'%image_url)
        p.submit(save,image_url)
        print('%s 下载任务已提交'%image_url)


# def parse_detail(res):
#     pass

def save(image_url):
    print('%s Save:%s'%(current_thread().getName(),image_url))
    try:
        response = requests.get(image_url,stream=False)
        if response.status_code == 200:
            filepath = photo_path+str(hash(image_url))+'.png'
            print(filepath)
            print('%s开始下载'%image_url)
            with open(filepath,'wb') as f:
                f.write(response.content)
                print('%s download success!')
    except Exception as e :
        print('error!!!',e)


def main():
    # index_url = 'https://unsplash.com/'
    # index_url = 'https://unsplash.com/search/photos/computer'
    # index_url = 'https://unsplash.com/new'
    index_url = 'https://unsplash.com/search/photos/wallpaper'
    for i in range(10):
        p.submit(get_page,index_url.format(i,)).add_done_callback(parse_images)

if __name__ == '__main__':
    main()