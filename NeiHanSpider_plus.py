import urllib.request
import re
import os

class MySpiderNeiHan:

    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}
        self.stories = []
        self.enable = False
        self.AllDuanzi = []

    def getPage(self, pageIndex):
        try:
            url = 'http://www.qiushibaike.com/hot/page/'+str(pageIndex)
            request = urllib.request.Request(url, headers=self.headers)
            response = urllib.request.urlopen(request)
            pageCode = response.read().decode('utf-8')
            
            return pageCode
        except urllib.request.URLError as e:
            if hasattr(e,"reason"):
                print("connet is lost ....",e.reason)
                return None
    def getPageItems(self, pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print('loading error')
            return None
        pattern = re.compile(
            '<h2>(.*?)</h2>.*?<div class="content">.*?<span>(.*?)</span>.*?<div class="stats.*?class="number">(.*?)</i>.*?class="number">(.*?)</i>',re.S)
        items = re.findall(pattern, pageCode)
        pageStories=[]
        for item in items:
            pageStories.append([item[0].strip(),item[1].strip(),item[2].strip(),item[3].strip()])
        return pageStories

    def loadPage(self):
        if self.enable == True:
            if len(self.stories) < 2:
                pageStories = self.getPageItems(self.pageIndex)
                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex+= 1

    def getOneStory(self, pageStories, page):
        for story in pageStories:
            #income = input('Waiting Input ')
            self.loadPage()
            ##if income == "Q":
            if page == 5:  
                self.enable = False
                return
            duanzi = "第%d页\n---------------------\n作者:%s\n  %s \n--------------------\n点赞数%s  %s评论  \n\n" % (page,story[0],story[1],story[2],story[3])
            #self.AllDuanzi.append(duanzi)

    def start(self):
        print("======Wait-for-loading======")
        self.enable = True
        self.loadPage()
        nowPage = 0
        while self.enable:
            if len(self.stories) > 0:
                pageStories = self.stories[0]
                nowPage +=1
                del self.stories[0]
                self.getOneStory(pageStories,nowPage)
        #将文件保存到D盘(未完成)
        #fo=open("d:\\duanzi.txt","wb")
        #fo.write(str(self.AllDuanzi))

if __name__ == "__main__":
    spider = MySpiderNeiHan()
    spider.start()
                
        
