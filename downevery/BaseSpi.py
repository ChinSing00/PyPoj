import urllib
from urllib import request
import re
import socket

'''
####为网页爬去提供了几个基本的方法
'''
class basespi():
    def __init__(self):
        self.User_Agent = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64)')]
           
    def getPageAnt(self,url,proxy_ip):
        socket.setdefaulttimeout(5)
        try:
            proxy_support = request.ProxyHandler(proxy)
            opener = request.build_opener(proxy_support)
            opener.addheaders = self.User_Agent
            request.install_opener(opener) 
            response = request.urlopen(url)
            pageCode = response.read()
            return pageCode
        
        except urllib.request.URLError as e:
            if hasattr(e,"Reason"):
                print("解析html出错...  原因：",e.reason)
                return None


    def getPage(self,url):
        try:
            header=dict(self.User_Agent)               
            req=urllib.request.Request(url=url,headers=header)
            response=urllib.request.urlopen(req)
            content=response.read()
            return content

        except urllib.request.URLError as e:
            if hasattr(e,"Reason"):
                print("解析html出错...  原因：",e.reason)
                return None


    def _regx(slef,rule,pageCode) :
      
        if pageCode == '':
            return None
        pattern = re.compile(rule)
        pageItems = re.findall(pattern,pageCode)  
    
        return pageItems      