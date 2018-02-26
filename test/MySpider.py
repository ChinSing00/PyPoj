import urllib
from urllib import request
from datetime import datetime

def test1(url):
    with request.urlopen(url) as f:
        print(f.read().decode('gbk'))
#runSpider("http://www.baidu.com")
#test1('https://www.zwdu.com/book/11029/2297440.html')
#test1('https://api.douban.com/v2/book/2129650')
#test1('http://www.kanunu8.com/book3/7751/227197.html')
test1('https://www.zwdu.com/book/11029/2297440.html')