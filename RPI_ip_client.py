#!/usr/bin/python3
import socket
import sys

# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# 获取本地主机名
host = '120.79.47.182'

# 设置端口好
port = 8081

# 连接服务，指定主机和端口
s.connect((host, port))

# 接收小于 1024 字节的数据
msg = s.recv(1024)

print (msg.decode('utf-8'))

sendmsg = bytes(socket.gethostname(), encoding = "utf8")  

s.sendall(sendmsg)

s.close()