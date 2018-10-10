# coding:utf-8
import threading
# 在项目外用脚本启动爬虫
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.settings import Settings

# 配置文件在这里手动实现

def runSpider():
    settings = Settings({
        'BOT_NAME' :'jobspiders',
        'SPIDER_MODULES' : ['jobspiders.spiders'],
        'NEWSPIDER_MODULE' : 'jobspiders.spiders',
        'ROBOTSTXT_OBEY' : False,
        'DOWNLOAD_DELAY' : 5,
        'SPIDER_MIDDLEWARES':{'jobspiders.middlewares.JobspidersSpiderMiddleware': 543},
        'DOWNLOADER_MIDDLEWARES' : {
        'jobspiders.middlewares.JobspidersSpiderMiddleware': 543,
        'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,  # 这一行是取消框架自带的useragent
        'jobspiders.rotateuseragent.RotateUserAgentMiddleware': 400
        },
        'ITEM_PIPELINES' :  {
         'jobspiders.pipelinesmysql.JobspidersPipeline': 300,
        },
        'LOG_LEVEL' : 'INFO',
        'LOG_FILE' : 'jobspider.log'
    })

    runner = CrawlerRunner(settings)    # 通过程序对爬虫进行设置
    d = runner.crawl('jobsspider1')      # 启动爬虫
    d.addBoth(lambda _: reactor.stop())
    reactor.run()
    return 0

def spiderThread1():
    # 启动线程执行爬虫程序
    threading.Thread(target= runSpider())

if __name__ == '__main__':
    spiderThread1()




