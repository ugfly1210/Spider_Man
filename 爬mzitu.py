import requests
from bs4 import BeautifulSoup
import os


class Mzitu():
    def __init__(self):
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

    def all_url(self, url):
        html = self.request(url)  ##调用request函数把套图地址传进去会返回给我们一个response
        print(html)
        all_a = BeautifulSoup(html.text, 'lxml').find('div', class_='all').find_all('a')
        for a in all_a[1:]:
            title = a.get_text()
            print(u'开始保存：', title)  ##加点提示不然太枯燥了
            path = str(title).replace("?", '_')  ##我注意到有个标题带有 ？  这个符号Windows系统是不能创建文件夹的所以要替换掉
            self.mkdir(path)  ##调用mkdir函数创建文件夹！这儿path代表的是标题title哦！！！！！不要糊涂了哦！
            href = a['href']
            self.html(href)  ##调用html函数把href参数传递过去！href是啥还记的吧？ 就是套图的地址哦！！不要迷糊了哦！

    def html(self, href):  ##这个函数是处理套图地址获得图片的页面地址
        html = self.request(href)
        self.headers['referer'] = href
        max_span = BeautifulSoup(html.text, 'lxml').find('div', class_='pagenavi').find_all('span')[-2].get_text()
        for page in range(1, int(max_span) + 1):
            page_url = href + '/' + str(page)
            self.img(page_url)  ##调用img函数

    def img(self, page_url):  ##这个函数处理图片页面地址获得图片的实际地址
        img_html = self.request(page_url)
        img_url = BeautifulSoup(img_html.text, 'lxml').find('div', class_='main-image').find('img')['src']
        self.save(img_url)

    def save(self, img_url):  ##这个函数保存图片
        name = img_url[-9:-4]
        img = self.request(img_url)
        f = open(name + '.jpg', 'ab')
        f.write(img.content)
        f.close()

    def mkdir(self, path):  ##这个函数创建文件夹
        path = path.strip()
        isExists = os.path.exists(os.path.join("/Users/macbookpro/Desktop/mzt", path))
        if not isExists:
            try:
                print(u'创建了', path, u'文件夹！')
                os.makedirs(os.path.join("/Users/macbookpro/Desktop/mzt", path))
                os.chdir(os.path.join("/Users/macbookpro/Desktop/mzt", path))  ##切换到目录
            except Exception as e :
                print('报告！！！这里有问题-->%s'%e)
            return True
        else:
            print(u'名字叫做', path, u'的文件夹已经存在了！')
            return False

    def request(self, url):  ##这个函数获取网页的response 然后返回
        
        content = requests.get(url, headers=self.headers)
        return content


m = Mzitu()  ##实例化
m.all_url('http://www.mzitu.com/all/')  ##给函数all_url传入参数  你可以当作启动爬虫（就是入口）