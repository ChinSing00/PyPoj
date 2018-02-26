import urllib.request
import re

class imgSpi:
    def __init__(self):
        self.pageIndex = 0
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}
        self.url = 'https://www.douban.com/photos/photo/2510554708/#image'
        self.rule1 = '<link rel="next".*?<a href="(.*?)".*?</a>'
        self.rule2 = '<td id="pic-viewer" .*?<img src="(.*?)" alt title>.*?</td>'
        self.rule3 = '<a class="mainphoto".*?<img width=".*?" src="(.*?)">'
        
    def GetHtml(self,url):
        try:
            htmlRequest = urllib.request.Request(url,headers=self.headers)
            response = urllib.request.urlopen(htmlRequest)
            pageCode = response.read().decode('utf-8')
            return pageCode
        except urllib.request.URLError as e:
            if hasattr(e,"reason"):
                print("1.connet is lost ....",e.reason)
                return None
            
    def GetNetxUrl(self,pageCode,rule):
        if not pageCode:
            print('non page....')
            return None
        pattern = re.compile(rule,re.S)
        thisUrl = re.findall(pattern,pageCode)
        if(rule == self.rule2):
            return print(thisUrl)            
        return thisUrl[0]
    
        
    def SaveImg(self,pageCode):
        if not pageCode:
            print('3.non page....')
            return None
        print(pageCode)

        
if __name__ == "__main__":
    start = imgSpi()
    theCode = start.GetHtml(start.url)
    for  i in range(10,13):
        temp = ''
        temp1 = ''
        code = ''
        temp = start.GetNetxUrl(theCode,start.rule1)
        print(temp)
        code = start.GetHtml(temp)
        temp1 = start.GetNetxUrl(code,start.rule2)
        print(temp1)
        start.SaveImg(temp1)
        i+=1
    
