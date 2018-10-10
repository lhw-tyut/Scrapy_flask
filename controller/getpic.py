import re
import requests
import os,time,random

class Download():
    def dowmloadPic(self,html, keyword):
        pic_url = re.findall('"objURL":"(.*?)",', html, re.S)
        i = 1
        print('找到关键词:' + keyword + '的图片，现在开始下载图片...')
        for each in pic_url:
            print('正在下载第' + str(i) + '张图片，图片地址:' + str(each))
            pic = requests.get(each, timeout=100)
            time.sleep(random.randint(0,3))
            savePath = os.path.join('F:\\AI\\Scrapy_web\\static/img/' + str(i) + '.jpg')
            with open(savePath, 'wb')as fp:
                fp.write(pic.content)
            i += 1
        return True

    def main(self,key):

        word = key
        url = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&hs=0&xthttps=111111&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word='+word
        headers = {#"User-Agent":"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
         #"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
         "User-Agent":"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
         "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
         "User-Agent":"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
                   }
        result = requests.get(url,headers=headers)
        a = self.dowmloadPic(result.text, word)
        return a

