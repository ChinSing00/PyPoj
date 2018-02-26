import urllib.request
import urllib
import re
import time


class MySpiderNeiHan:

    def __init__(self,rule):
        
        self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        self.headers = {'User-Agent': self.user_agent}
        self.rule = rule

    def getPage(self,url):
        try:
            request = urllib.request.Request(url, headers=self.headers)
            response = urllib.request.urlopen(request)
            pageCode = response.read().decode('utf-8')
            return pageCode
        except urllib.request.URLError as e:
            if hasattr(e,"reason"):
                print("connet is lost ....",e.reason)
                return None

    def DownLoadGif(slef,item):
        path = 'C:\\Users\\GUT-093\\Desktop\\PT\\GIFSpider\\DownLoad\\'+item[1].strip()+"S.gif"
        #print(item[0].strip()+'333'+path)
        try:
            urllib.request.urlretrieve('http://qq.yh31.com'+item[0].strip(),path)
            print(item[0].strip()+"成功下载....")
        except urllib.request.URLError as e:
            if hasattr(e,"reason"):
                print("下载失败~~~",e.reason)
                return None           
        
    def getPageItems(self, url):
        pageCode = self.getPage(url)
        #print(pageCode)
        if not pageCode:
            print('loading error')
            return None
        pattern = re.compile(self.rule,re.S)
        items = re.findall(pattern, pageCode)
        for item in items:
            self.DownLoadGif(item)
        return None

    #def start(self): 

if __name__ == "__main__":
    index = 2
    #gaoxiaogif_rex_rule
    rule = '<div class="listgif-giftu">.*?<img src="(.*?)".*? alt="()">'
    #qq.yh31.com_rex_rule
    rule1 = '<dt>.*?<img src="(.*?)".*? alt="(.*?)".*?>'
    #gaoxiaogif_url
    url = 'http://www.gaoxiaogif.com/index_%s.html'%index

    for i in  range(140,149):
        #qq.yh31.com_url
        url1 = 'http://qq.yh31.com/ka/zr/List_%s.html'%i
        print(url1)
        spider = MySpiderNeiHan(rule1)
        spider.getPageItems(url1)
        time.sleep(3)
        index+=i


    
    
      
   
    
                
        
