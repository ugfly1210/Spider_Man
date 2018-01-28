from scrapy.cmdline import execute
# execute(['scrapy','crawl','baidu','--nolog'])
from scrapy.settings.default_settings import DOWNLOADER_MIDDLEWARES_BASE

execute(['scrapy','crawl','baidu'])