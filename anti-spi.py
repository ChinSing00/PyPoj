# -*- coding: UTF-8 -*-
from urllib import request
import re

if __name__ == "__main__":
    #访问网址
    url = 'http://www.kanunu8.com/book3/7751/227197.html'
    #这是代理IP
    proxy = {'http': '14.153.55.243:3128'}
    #创建ProxyHandler
    proxy_support = request.ProxyHandler(proxy)
    #创建Opener
    opener = request.build_opener(proxy_support)
    #添加User Angent
    opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
    #安装OPener
    request.install_opener(opener)
    #使用自己安装好的Opener
    response = request.urlopen(url)
    #读取相应信息并解码
    html = response.read().decode("utf-8")
    print(html)
    
    '''
    rule = '{(.*?)}'
    pattern = re.compile(rule,re.S)
    print(rule+'\n\n\n\n\n\n\n\n'+html)
    items = re.findall(pattern, html)
    打印信息
    for i in items:
        #print("......")
        #print(i[0],i[1])
    '''