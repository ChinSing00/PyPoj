#用telnet来验证的
#使用telnet验证并不能说明该ip可以用于html页面的访问!!!
# -*- coding: utf-8 -*-

import telnetlib

def checkip(ip):
    print('------------------------connect---------------------------')
    # 连接Telnet服务器
    ips = ip.split(':')
    try:
        tn = telnetlib.Telnet(ips[0],port=ips[1],timeout=20)
    except:
        return  0
    else:
        return  1

    print('-------------------------end----------------------------')


print(checkip('14.117.211.156:9797'))
