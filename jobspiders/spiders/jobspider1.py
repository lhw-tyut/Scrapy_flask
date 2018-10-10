import scrapy
from ..items import JobspidersItem

class Jobspider1(scrapy.Spider):

    name = 'jobsspider1'
    allowed_domains = ['liepin.com/zhaopin/?imscid=R000000035&key=%E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98&dqs=010&d_sfrom=search_sub_site']
    start_urls = ['https://www.liepin.com/zhaopin/?imscid=R000000035&key=%E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98&dqs=010&d_sfrom=search_sub_site/']

    def parse(self, response):
        global count
        currentPageItems = response.xpath('/html/body/div[@class="container"]/div[@class="wrap"]/div[@class="job-content"]/div[@class="sojob-result "]/ul[@class="sojob-list"]/li')

        # currentPageItems = response.xpath('//div[@class="el"]')
        for jobItem in currentPageItems:
            # print(jobItem)
            jobspidersItem = JobspidersItem()
            jobPosition = jobItem.xpath('div[@class="sojob-item-main clearfix"]/div[@class="job-info"]/h3/a/text()').extract()
            if jobPosition:
                print(jobPosition[0].strip())
                jobspidersItem['jobPosition'] = jobPosition[0].strip()

            jobCompany = jobItem.xpath('div[@class="sojob-item-main clearfix"]/div[@class="company-info nohover"]/p[@class="company-name"]/a/text()').extract()
            if jobCompany:
                print(jobCompany[0].strip())
                jobspidersItem['jobCompany'] = jobCompany[0].strip()
            jobAddress  = jobItem.xpath('div[@class="sojob-item-main clearfix"]/div[@class="job-info"]/p[@class="condition clearfix"]/span[@class="area"]/text()').extract()
            if jobAddress:
                print(jobAddress[0].strip())
                jobspidersItem['jobAddress'] = jobAddress[0].strip()
            else:
                jobspidersItem['jobAddress'] = '北京'
            jobSalary = jobItem.xpath('div[@class="sojob-item-main clearfix"]/div[@class="job-info"]/p[@class="condition clearfix"]/span[@class="text-warning"]/text()').extract()
            if jobSalary:
                print(jobSalary[0].strip())
                jobspidersItem['jobSalary'] = jobSalary[0].strip()
            jobPublicDate = jobItem.xpath('div[@class="sojob-item-main clearfix"]/div[@class="job-info"]/p[@class="time-info clearfix"]/time/@title').extract()
            if jobPublicDate:
                print(jobPublicDate[0].strip())
                jobspidersItem['jobPublicDate'] = jobPublicDate[0].strip()
            jobspidersItem['jobSource'] = '猎聘网'
            yield jobspidersItem
            pass
        pass
