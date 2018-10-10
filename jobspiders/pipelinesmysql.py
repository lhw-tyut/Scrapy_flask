# -*- coding: utf-8 -*-
from .demo_util import DBUtils

# 作业： 自定义的管道，将完整的爬取数据，保存到MySql数据库中
class JobspidersPipeline(object):

    def process_item(self, item, spider):
        # item['jobPosition']
        # item['jobCompany']
        # item['jobAddress']
        # item['jobSalary']
        # item['jobPublicDate']
        db = DBUtils()
        dt = item
        ls = [(k, dt[k]) for k in dt if dt[k]]
        sql = 'insert into myjob (' + ','.join([i[0] for i in ls]) + ') values (' + ','.join(
            ['%r' % i[1] for i in ls]) + ');'
        db.insert(sql)
        return item

