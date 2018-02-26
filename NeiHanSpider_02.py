import urllib.request
import re


class DuanZiSpider:
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}
        self.stories = []
        self.enable = False

    def getPage(self, pageIndex):
            try:
                url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
                request = urllib.request.Request(url, headers=self.headers)
                response = urllib.request.urlopen(request)
                pageCode = response.read().decode('utf-8')
                return pageCode

            except urllib.request.URLError as e:
                if hasattr(e, "reason"):
                    print(u"连接糗事百科失败,错误原因", e.reason)
                    return None

    def getPageItems(self, pageIndex):

        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print("页面加载失败...")
            return None
        pattern = re.compile(
            '<h2>(.*?)</h2>.*?<div class="content">.*?<span>(.*?)</span>.*?<div class="stats.*?class="number">(.*?)</i>',
            re.S)
        items = re.findall(pattern, pageCode)
        pageStories=[]
        for item in items:
            pageStories.append([item[0].strip(),item[1].strip(), item[2].strip()])
        return pageStories

    def loadPage(self):
        if self.enable == True:
            if len(self.stories) < 2:
                pageStories = self.getPageItems(self.pageIndex)
                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex += 1


    def getOneStory(self, pageStories, page):
        for story in pageStories:
            income = input('Please Input')
            self.loadPage()
            if income == 'Q':
                self.enable = False
                return
            print("第%d页 作者:%s 段子内容:%s 点赞数(%s)" % (page,story[0],story[1],story[2]))

    def start(self):
        print("正在读取糗事百科，按回车查看新段子，Q退出")
        self.enable=True
        self.loadPage()
        nowPage =0
        while self.enable:
            if len(self.stories) > 0:
                pageStories= self.stories[0]
                nowPage +=1
                del self.stories[0]
                self.getOneStory(pageStories,nowPage)


if __name__ == "__main__":
    spider = DuanZiSpider()
    spider.start()
