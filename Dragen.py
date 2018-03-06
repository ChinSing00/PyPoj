import urllib
from urllib import request
import re
import time
import BaseSpi
'''
本程序使用了python的协程来进行网页的爬取,因为没有加入代理功能模块所以对爬取网页的速度做出了限制
强行阻塞了三秒才开始下一个url的爬取.如果加入了代理模块与消息队列模块,多线程模块将可以在最大带宽
下快速地爬取资源

#2018-02-09 将文件存储命名部分修改了一下,使得文件以网站的站内编号命名.只需要修改url就可以下载该网站的许多小说
#2018-02-13 引入了BaseSpi，将url请求和解析的一些常用的方法封装进了该类。使得代码更加整洁明了。
#2018-02-23 为爬取的小说加入章节标题
#2018-03-06 修复了没有下载内容时报错终止的bug
'''
#################################################################################################
'''
2018-02-13-----TODO引入多线程与消息队列，让爬取速度成倍增长同时还要防止网站的反爬虫机制的破坏
2018-02-22-----TODO为爬取的小说加入章节标题----->完成
2018-03-01-----TODO添加GUI界面 
'''

def getDownload(url):
    _81_rule = '&nbsp;&nbsp;&nbsp;&nbsp;[^&nbsp;<]*'
    _nunu_rule = '&nbsp;&nbsp;&nbsp;&nbsp;.*'
    _81_til_rule = '<h1>(.*?)</h1>'
    try:
        items = []
        title = []
        header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64)"}
        request = urllib.request.Request(url=url,headers=header)
        response = urllib.request.urlopen(request)
        try:
            content = response.read().decode('gbk')
        except :
            content = response.read().decode('utf-8') 
        bs = BaseSpi.basespi()
        items = bs._regx(_81_rule,content)
        title = bs._regx(_81_til_rule,content) 
        filename = url.split('/')[4]+'.txt'
        f = open(filename,'a+',encoding = 'utf-8')
        if len(items) != 0:
            temp = []
            temp.extend(items)
            if len(temp) != 0:
                print(str(title[0]))
                f.write('\t\t\t\t----'+title[0]+'----\n')
                for i in temp:
                    print(i)
                    f.write(i.strip().lstrip('&nbsp;')+"\n")
            else:
                for i in temp:
                    f.write(i.strip().lstrip('&nbsp;')+"\n")
        else:
            return None
          
    except urllib.request.URLError as e:
        if hasattr(e,"reason"):
                print("connet is lost ....",e.reason)
                return None

def consumer():
    r = 1.0
    while True:
        n = yield r
        if not n:
            return
        print(str(round((r/n[1]),2)*100)+'%')
        getDownload(n[0])
        r+= 1
 
def produce(con):
    con.send(None)
    n = ''
    '''
    url = 'http://book.km.com/shuku/1336097.html'
    url = 'http://www.kanunu8.com/book3/7751/' lz
    url = 'https://www.txtjia.com/shu/226243/'sjwl
    url ='https://www.zwdu.com/book/11029/'81-xzltq 
    url = 'https://www.zwdu.com/book/28675/'81-dj

    '''
    url ='https://www.zwdu.com/book/11029/'
    _1rule = '<a href=".*?/(\d*.html)">'
    _2rule = '<a href="[\./]*(\d*.html)">'

    bs = BaseSpi.basespi()
    si = bs._regx(_1rule,bs.getPage(url).decode('gbk'))
    print(si)
    l = 0
    for i in range(0,len(si)):
        #print(si[i])
        n = [url+str(si[i]),len(si)]
        con.send(n)
        time.sleep(3)
        
    con.close()


con = consumer()
print('start.....')
produce(con)
 

###############################################################################

