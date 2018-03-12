import PPProxy
import re
import time
import BaseSpi
from bs4 import BeautifulSoup
'''
(本程序使用了python的协程来进行网页的爬取,因为没有加入代理功能模块所以对爬取网页的速度做出了限制
强行阻塞了三秒才开始下一个url的爬取.如果加入了代理模块与消息队列模块,多线程模块将可以在最大带宽
下快速地爬取资源)-------------------已修改为V2版本,使用了Beautiful　Ｓｏｕｐ　来匹配网页内容，但是有
部分内容还是需要正则来匹配（获得全体的ｕｒｌ什么的　）。

'''
#################################################################################################
'''
2018-02-13-----TODO引入多线程与消息队列，让爬取速度成倍增长同时还要防止网站的反爬虫机制的破坏
2018-02-22-----TODO为爬取的小说加入章节标题----->完成
2018-03-01-----TODO添加GUI界面 
'''
class NovelDown:
	def __init__(self，ｕｒｌ):
		self._1rule = '<a href=".*?/(\d*.html)">'
	    self._2rule = '<a href="[\./]*(\d*.html)">'
	    self.url = url
	    slef.bookname = ''

	def getDownload(slef.url):
	    bs = BaseSpi.basespi()
	    try:
	        content = bs.getPageAnt(url,)  
	        soup = BeautifulSoup(content,'lxml')
	        bookname =''''something'''
	        con_text = soup.find('div',id='content')
	        title = soup.title
	        with open(bookname+'.txt','a+',encoding = 'utf-8') as f:
	            f.write('\t\t'+'--'*4+title.get_text()+'--'*4)
	            f.write(con_text.get_text()+'\n')
	            return None
	    except urllib.request.URLError as e:
	        if hasattr(e,"reason"):
	                print("connet is lost ....",e.reason)
	                return None

	def consumer(slef):
	    r = 1.0
	    while True:
	        n = yield r
	        if not n:
	            return
	        print(str(round((r/n[1]),2)*100)+'%')
	        self.getDownload(n[0])
	        r+= 1
	 
	def produce(slef,con):
	    con.send(None)
	    n = ''
	    bs = BaseSpi.basespi()
	    si = bs._regx(_1rule,bs. (self.url).decode('gbk'))
	    print(si)
	    l = 0
	    for i in range(0,len(si)):
	        n = [url+str(si[i]),len(si)]
	        con.send(n)
	        time.sleep(3)    
	    con.close()

url = 'https://www.zwdu.com/book/23488/'
con = consumer()
print('start.....')
produce(con)
 

###############################################################################

'''
	    url = 'http://book.km.com/shuku/1336097.html'
	    url = 'http://www.kanunu8.com/book3/7751/' lz
	    url = 'https://www.txtjia.com/shu/226243/'sjwl
	    url ='https://www.zwdu.com/book/11029/'81-xzltq 
	    url = 'https://www.zwdu.com/book/28675/'81-dj
	    url = 'https://www.zwdu.com/book/23488/'
	    url ='https://www.zwdu.com/book/11029/'
	    '''