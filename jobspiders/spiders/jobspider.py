import scrapy
from ..items import JobspidersItem
count = 1
class Jobspider(scrapy.Spider):

    name = 'jobsspider'
    #allowed_domains = ['search.51job.com/list/010000,000000,0000,00,9,99,python,2,1.html']
    start_urls = ['https://search.51job.com/list/010000,000000,0000,00,9,99,python,2,1.html/']

    def parse(self, response):
        global count
        currentPageItems = response.xpath('/html/body/div[@class="dw_wp"]/div[@class="dw_table"]/div[@class="el"]')

        # currentPageItems = response.xpath('//div[@class="el"]')
        for jobItem in currentPageItems:
            # print(jobItem)
            jobspidersItem = JobspidersItem()
            jobPosition = jobItem.xpath('p[@class="t1 "]/span/a/text()').extract()
            if jobPosition:
                print(jobPosition[0].strip())
                jobspidersItem['jobPosition'] = jobPosition[0].strip()

            jobCompany = jobItem.xpath('span[@class="t2"]/a/text()').extract()
            if jobCompany:
                print(jobCompany[0].strip())
                jobspidersItem['jobCompany'] = jobCompany[0].strip()
            jobAddress  = jobItem.xpath('span[@class="t3"]/text()').extract()
            if jobAddress:
                print(jobAddress[0].strip())
                jobspidersItem['jobAddress'] = jobAddress[0].strip()
            jobSalary = jobItem.xpath('span[@class="t4"]/text()').extract()
            if jobSalary:
                print(jobSalary[0].strip())
                jobspidersItem['jobSalary'] = jobSalary[0].strip()
            jobPublicDate = jobItem.xpath('span[@class="t5"]/text()').extract()
            if jobPublicDate:
                print(jobPublicDate[0].strip())
                jobspidersItem['jobPublicDate'] = jobPublicDate[0].strip()
            jobspidersItem['jobSource'] = '前程无忧'
            yield jobspidersItem
            pass
        pass
        if count < 5:
            nextPageURL = response.xpath('//li[@class="bk"]/a/@href').extract()  # 取下一页的地址
            print(nextPageURL)
            if nextPageURL:
                count += 1
                url = response.urljoin(nextPageURL[-1])
                print('url', url)
                # 发送下一页请求并调用parse()函数继续解析
                yield scrapy.Request(url, self.parse, dont_filter=False)
                pass
            else:
                print("退出")
        else:
            print("完成")