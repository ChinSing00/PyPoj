import PPProxy
import re
import time
import BaseSpi
from bs4 import BeautifulSoup
from bs4 import element
'''
(本程序使用了python的协程来进行网页的爬取,因为没有加入代理功能模块所以对爬取网页的速度做出了限制
强行阻塞了三秒才开始下一个url的爬取.如果加入了代理模块与消息队列模块,多线程模块将可以在最大带宽
下快速地爬取资源)-------------------已修改为V2版本,使用了Beautiful　Ｓｏｕｐ　来匹配网页内容，但是有
部分内容还是需要正则来匹配（获得全体的ｕｒｌ什么的--假的,我tm全用bs4了　）。

'''
#################################################################################################
'''
2018-02-13-----TODO引入多线程与消息队列，让爬取速度成倍增长同时还要防止网站的反爬虫机制的破坏
2018-02-22-----TODO为爬取的小说加入章节标题----->完成
2018-03-01-----TODO添加GUI界面 
'''
class NovelDown:
	def __init__(self,url):
		#self._1rule = '<a href=".*?/(\d*.html)">'
	    #self._2rule = '<a href="[\./]*(\d*.html)">'
	    self.url = url
	    self.bookname = ''

	def getDownload(self,url):
	    bs = BaseSpi.basespi()
	    try:
	        content = bs.getPage(url)  
	        soup = BeautifulSoup(content,'lxml')
	        bookname =str(self.bookname)
	        con_text = soup.find('div',id='htmlContent')
	        title = soup.title
	        with open(bookname+'.txt','a+',encoding = 'utf-8') as f:
	            f.write('\t\t'+'--'*4+title.get_text()+'--'*4)
	            f.write(con_text.get_text()+'\n')
	            return None
	    except :
	        return None

	def consumer(self):
	    r = 1.0
	    while True:
	        n = yield r
	        if not n:
	            return
	        self.getDownload(n[0])
	        print(str(round((r/n[1]),2)*100)+'%')
	        r+= 1
	 
	def produce(self,con):
	    con.send(None)
	    n = ''
	    si = []
	    bs = BaseSpi.basespi()
	    soup = BeautifulSoup(bs.getPage(self.url),'lxml')
	    #soup = BeautifulSoup(open('lst.html',encoding='utf-8'),'lxml')
	    ls = soup.find('div',class_='book_list')
	    self.bookname = soup.title.string.strip('- 小说在线阅读 - 村上春树作品集')	
	    print('开始%s'%self.bookname+'的爬取')
	    lls = list(filter(lambda x: x.name == 'ul' , ls))
	    ap = lls[0].find_all('a')
	    list(filter(lambda x:si.append(x['href']),ap))
	    #print(bn)
	    for i in si:
	        n = [i,len(si)]
	        con.send(n)
	        time.sleep(3)    
	    con.close()
	    print('完成%s'%self.bookname+'的爬取！')

if __name__ == '__main__':
	bs = BaseSpi.basespi()
	soup = BeautifulSoup(bs.getPage('http://cscs.zuopinj.com/'),'lxml')
	pps = soup.find_all('h3')
	li = []
	list(filter(lambda x: li.append(pps[x].a['href']), range(len(pps))))
	print(li)
	for i in li:
		my = NovelDown(i)
		con = my.consumer()
		my.produce(con)
 

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
