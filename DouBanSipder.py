import urllib.request
import re

class DBanSpider:
    def __init__(self):
        self.pageIndex = 0
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}
        self.moivesInfo = []
        self.enable = False
        self.Index = 0
        self.requestTime = 0
    def getPage(self, pageIndex):
        try:
            url = 'https://movie.douban.com/top250?start='+str(pageIndex-1)+'&filter='
            request = urllib.request.Request(url, headers=self.headers)
            response = urllib.request.urlopen(request)
            pageCode = response.read().decode('utf-8')
            self.requestTime+=1
            print("time"+str(self.requestTime))
            #print(pageCode)
            return pageCode
        except urllib.request.URLError as e:
            if hasattr(e,"reason"):
                print("connet is lost ....",e.reason)
                return None

    def getPageItems(self, pageIndex):
        a='<span class="title">(.*?)</span>.*?<span class="title">([^&nbsp;]*?)</span>.*?<span class="other">(.*?)</span>.*?<span class="inq">(.*?)</span>'
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print('loading error')
            return None
        pattern = re.compile(a,re.S)
        items = re.findall(pattern, pageCode)
        pageMovie=[]
        for item in items:
            pageMovie.append([item[0].strip(),item[1].strip(),item[2].strip(),item[3].strip()])
        return pageMovie

    def loadPage(self):
        if self.enable == True:
            
            if len(self.moivesInfo) < 2:
                pageMovie = self.getPageItems(self.pageIndex)
                if pageMovie:
                    self.moivesInfo.append(pageMovie)
                    self.pageIndex+= 25
                    
                    
    def getSingleMovie(self, pageMovie, page):
        for movie in pageMovie:
            self.loadPage()
            if page > 10:  
                self.enable = False
                return
            self.Index+=1
            print(self.Index)
            print("%s%s%s\n简介:%s \n" %(movie[0],movie[1],movie[2],movie[3]))
    def start(self):
        print("======Push Enter to get the movie info======")
        self.enable = True
        self.loadPage()
        nowPage = 0
        while self.enable:
            if len(self.moivesInfo) > 0:
                pageMovie = self.moivesInfo[0]
                nowPage +=1
                del self.moivesInfo[0]
                self.getSingleMovie(pageMovie,nowPage)

if __name__ == "__main__":
    spider = DBanSpider()
    spider.start()            
