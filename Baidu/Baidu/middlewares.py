# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class BaiduSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class BaiduDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        """
        # This method is used by Scrapy to create your spiders.
        scrapy中的许多类都实现了该方法
        通过调用该方法来生成下载器中间件管理器对象
        那再补充两句：
            每一个spider对应一个crawler，一个crawler会使用一个engine
            一个CrawlerProcess中可以创建多个crawler进行多种爬取。
        """
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        """
        当每个request通过下载器中间件时，process_request被调用
        :param request:  要处理的request
        :param spider:   该request对应的spider
        :return:
            必须返回四者其一！！！
            None--> scrapy继续处理该request，会执行其他中间件的相应方法。
                    直到合适的下载器处理函数（download handler）被调用该request被执行,该request被执行(其response被下载)。
            Request对象--> Scrapy停止调用 process_request()方法并重新调度返回的request。当新返回的request被执行后， 相应地中间件链将会根据下载的response被调用。
            Response对象--> 已经安装的中间件的process_response()方法会在每个response返回时调用。
            raise IgnoreRequest异常--> 停止process_request的执行，开始执行process_exception
        """
        return None

    def process_response(self, request, response, spider):
        """
        当下载器完成http请求，传递响应给引擎的时候调用。
        :param request:  发起响应的请求
        :param response: 正在处理的响应
        :param spider:   这个响应所对应的spider
        :return:
            如果返回一个reponse对象（可以与传入的reponse相同，也可以是一个全新的对象），那么响应将继续与process_response()链中的下一个中间件一起处理。
            如果返回一个request对象，那么中间件链将暂停，并且返回的请求将被重新安排在将来被下载。这与返回请求的行为是一样的process_request()。
            如果raise一个IgnoreRequest异常，则调用request的errback(Request.errback)。
            如果没有代码处理抛出的异常，则在下面爬虫中间件会说这个东西。配合着process_spider_input()和process_spider_output()来讲。
        """
        print('reponse1')
        return response

    def process_exception(self, request, exception, spider):
        """
        当下载处理器(download handler)或 process_request()(下载中间件)抛出异常(包括 IgnoreRequest 异常)时，Scrapy 调用 process_exception() 。
        :param request:  产生异常的request
        :param exception:  抛出的异常
        :param spider:  request对应的spider
        :return:
            当下载处理器(download  handler)或 process_request()(下载中间件)抛出异常(包括 IgnoreRequest 异常)时，Scrapy 调用 process_exception()。
            process_exception()应该返回以下之一： 返回 None、一个 Response 对象、或者一个 Request 对象。
            如果其返回 None，Scrapy 将会继续处理该异常，接着调用已安装的其他中间件的 process_exception()方法，直到所有中间件都被调用完毕，则调用默认的异常处理。
            如果其返回一个 Response 对象，则已安装的中间件链的 process_response()方法被调用。Scrapy 将不会调用任何其他中间件的 process_exception() 方法。
            如果其返回一个 Request 对象， 则返回的 request 将会被重新调用下载。这将停止中间件的 process_exception()方法执行，就如返回一个 response 的那样。
        """
        return None

    def spider_opened(self, spider):
        # 爬取的准备工作，创建engine的关键组件
        spider.logger.info('Spider opened: %s' % spider.name)



# 2、middlewares.py
from Baidu.proxy_handle import get_proxy, delete_proxy


class DownMiddleware1(object):
    def process_request(self, request, spider):
        """
        请求需要被下载时，经过所有下载器中间件的process_request调用
        :param request:
        :param spider:
        :return:
            None,继续后续中间件去下载；
            Response对象，停止process_request的执行，开始执行process_response
            Request对象，停止中间件的执行，将Request重新调度器
            raise IgnoreRequest异常，停止process_request的执行，开始执行process_exception
        """
        proxy = "http://" + get_proxy()
        request.meta['download_timeout'] = 20
        request.meta["proxy"] = proxy
        print('为%s 添加代理%s ' % (request.url, proxy), end='')
        print('元数据为', request.meta)

    def process_response(self, request, response, spider):
        """
        spider处理完成，返回时调用
        :param response:
        :param result:
        :param spider:
        :return:
            Response 对象：转交给其他中间件process_response
            Request 对象：停止中间件，request会被重新调度下载
            raise IgnoreRequest 异常：调用Request.errback
        """
        print('返回状态吗', response.status)
        return response

    def process_exception(self, request, exception, spider):
        """
        当下载处理器(download handler)或 process_request() (下载中间件)抛出异常
        :param response:
        :param exception:
        :param spider:
        :return:
            None：继续交给后续中间件处理异常；
            Response对象：停止后续process_exception方法
            Request对象：停止中间件，request将会被重新调用下载
        """
        print('代理%s，访问%s出现异常:%s' % (request.meta['proxy'], request.url, exception))
        import time
        time.sleep(5)
        delete_proxy(request.meta['proxy'].split("//")[-1])
        request.meta['proxy'] = 'http://' + get_proxy()

        return request

