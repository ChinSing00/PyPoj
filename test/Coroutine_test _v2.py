import urllib
from urllib import request
import re
import time

def _getHtmlCode(url):
    ip_totle=[]
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64)"}
    request=urllib.request.Request(url=url,headers=headers)
    response=urllib.request.urlopen(request)
    content=response.read().decode('gbk')
    print(content)
    pattern=re.compile('<a href="[\./]*(\d*.html)">')  
    ip_page=re.findall(pattern,content)
    return ip_page

def getDownload(url):
    try:
        headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64)"}
        request=urllib.request.Request(url=url,headers=headers)
        response=urllib.request.urlopen(request)
        content=response.read().decode('gbk')
        
        pattern=re.compile('&nbsp;&nbsp;&nbsp;&nbsp;.*')  
        items = re.findall(pattern,content)
        #print(str(len(items))+'\n\n'+content)
        for item in items:
            #print('---------'+items[0].strip()+'----------')
            with open('xiaoshuo.txt','a+',encoding='utf8') as f:
                print('---------item----------')
                a =item.strip().lstrip('&nbsp;').rstrip('<br />')
                bs = '  '+a.rstrip('<br />')+'\n'
                f.write(bs)
                f.close()
    except urllib.request.URLError as e:
        if hasattr(e,"reason"):
                print("connet is lost ....",e.reason)
                return None
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        #print('http://www.kanunu8.com/book3/7751/'+n)
        getDownload('http://www.kanunu8.com/book3/7751/'+n)

def produce(con):
    con.send(None)
    n = ''
    #url = 'http://book.km.com/shuku/1336097.html'
    url = 'http://www.kanunu8.com/book3/7751/'
    si = _getHtmlCode(url)
    l = 1
    for i in range(0,len(si)):
        n = si[i]
        con.send(n)
        time.sleep(3)
        #print(si[i])
    con.close()




con = consumer()
produce(con)
