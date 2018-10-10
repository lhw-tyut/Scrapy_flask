import requests
import emoji
import json
import time
import random
from dao.demo_util import DBUtils
#下载第一页数据
db = DBUtils()
class Commentget():

    def get_one_page(self,url):
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
        }
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None

    #解析第一页数据
    def parse_one_page(self,html):
        data = json.loads(html)['cmts']
        for item in data:
            yield{
            'comment':item['content'],
            'date':item['time'].split(' ')[0],
            'rate':item['score'],
            'city':item['cityName'],
            'nickname':item['nickName']
            }

    #保存数据到文本文档
    def save_to_txt(self):
        for i in range(1,10):
            url = 'http://m.maoyan.com/mmdb/comments/movie/1212592.json?_v_=yes&offset=' + str(i)
            html = self.get_one_page(url)
            print('正在保存第%d页。'% i)
            for item in self.parse_one_page(html):
                dt = item
                ls = [(k, dt[k]) for k in dt if dt[k]]
                sql = 'insert into comment1 (' + ','.join([i[0] for i in ls]) + ') values (' + ','.join(
                    ['%r' % emoji.demojize(str(i[1])[:25]) for i in ls]) + ');'
                db.insert(sql)

    def movieComment(self):
        sql = 'select nickname,city,date,rate,comment from comment1 where rate>3'
        comments = db.selectallInfo(sql)
        tcomments = []
        for comment in comments:
            if comment not in tcomments:
                tcomments.append(comment)
        return tcomments


