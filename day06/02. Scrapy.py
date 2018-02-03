# 它是基于twisted模块实现的。

# spider 爬虫逻辑
# downloader 在多个任务之间切
# 调度
# 引擎  负责数据流之间的传递
# 数据持久化 item pip
# spider 和 引擎之间有个爬虫中间件：
    # - 和django的中间件有点区别。
    #
# 下载器中间件




# 1：第一步spider产生爬取请求。 不走中间件交给引擎
# 引擎调度请求： 通过调度器。 调度器scheduler来干请求。
# 调度一个出来再传给引擎，调度好的传给引擎。
# 引擎发送调度好的请求，通过中间件发给downloader。
# downloader下载好再返回。
class S:
    def __init__(self):
        pass

class T:
    def __init__(self):
        pass

    @staticmethod  #静态方法:类里的方法直接被类调用,就像正常的函数一样
    def show_student_info():
        # f = open('student',encoding= 'utf-8')
        # for line in f:
        #     name,sex = line.strip().split(',')
        print('6666666')
ff = S()
T.show_student_info()

