#_4('基于生成器的非阻塞式爬虫')
'''
import socket 
from selectors import DefaultSelector,EVENT_WRITE,EVENT_READ

selector = DefaultSelector()
stopped = False
urls_todo = {'/0','/2','/3','/5','/9','/8','/10','/4','/11','/6','/7'}
#urls_todo = {'/book/30231/','/book/30141/','/book/30246/','/book/30247/','/book/30248/'}

class Future:

	def __init__(self):
		self.result = None
		self._callbacks =[]

	def add_done_callback(self,fn):
		self._callbacks.append(fn)

	def set_result(self,result):
		self.result = result
		for fn in self._callbacks:
			fn(self)

class Crawler:

	def __init__(self,url):
		self.url = url
		self.response = b''

	def fetch(self):
		sock = socket.socket()
		sock.setblocking(False)
		try:
			sock.connect(('example.com',80))
		except BlockingIOError :
			pass
		f = Future()

		def on_conneted():
			f.set_result(None)

		selector.register(sock.fileno(),EVENT_WRITE,on_conneted)
		yield f
		selector.unregister(sock.fileno)
		get = 'GET {0} HTTP/1.0\r\nexample.com\r\n\r\n'.format(self.url)

		global stopped
		while True:
			f = Future()

			def on_readable():
				f.set_result(sock.recv(4096))

			selector.rigister(sock.fileno(),EVENT_READ,on_readable)
			chunk = yield f
			selector.unregister(sock.fileno())
			if chunk:
				self.response += chunkl
				print(str(self.response))
			else:
				urls_todo.remove(self.url)
				if not urls_todo:
					stopped = True
				break

class Task:

	def __init__(self,core):
		self.core = core
		f = Future()
		f.set_result(None)
		self.step(f)

	def step(self,future):
		try:
			next_future = self.core.send(future.result) 
		except StopIteration:
			return
		next_future.add_done_callback(self.step)

def loop():
	while not stopped:
		evnets = selector.select()
		for event_key,event_mask in evnets:
			callback = event_key.data
			callback()

if __name__ == "__main__":
	for url in urls_todo:
		crawler = Crawler(url)
		Task(crawler.fetch())
	loop()
'''

#_3('单线程非阻塞式爬虫')
'''
import socket 
from selectors import DefaultSelector,EVENT_WRITE,EVENT_READ

selector = DefaultSelector()
stopped = False 
urls_todo = {'/0','/2','/3','/5','/9','/8','/10','/4','/11','/6','/7'}


class Crawler:
	def __init__(self,url):
		self.url = url 
		self.sock = None
		self.response = b''

	def fetch(self):
		self.sock = socket.socket()
		self.sock.setblocking(False)
		try:
			self.sock.connect(('example.com',80))
		except BlockingIOError:
			pass
		selector.register(self.sock.fileno(),EVENT_WRITE,self.connected)

	def connected(self,key,mask):
		selector.unregister(key.fd)
		get = 'GET {0} HTTP/1.0\r\nHost:example.com\r\n\r\n'.format(self.url)
		self.sock.send(get.encode('ascii'))
		selector.register(key.fd,EVENT_READ,self.read_response)

	def read_response(self,key,mask):
		global stopped
		chunk = self.cock.recv(4096)
		if chunk:
			self.response += chunk
		else:
			selector.unregister(key.fd)
			urls_todo.remove(self.url)
			if not urls_todo:
				stopped = True


def loop():
		events = selector.select()
		for event_key,event_mask in events:
			callback = event_key.data
			callback(event_key,event_mask)

if __name__ == "__main__":
	for url in urls_todo:
		crawler = Crawler(url)
		crawler.fetch()
	loop()

'''

#_2('BeautifulSoup的用法')
'''
from bs4 import BeautifulSoup
from bs4 import element

soup = BeautifulSoup(open('rrs.html',encoding = 'utf-8'),'lxml')

#aas = soup.find('div',id='content')
#print(aas.get_text())

soup = list(filter(lambda x: type(x) == element.Tag, soup))
for x in soup:
	print(str(x.get_text()),'\n'+'---------------'*8)
	'''

#_1('yield from的用法')
'''
def gen():
	yield from subgen()

def subgen():
    while True:
        x = yield
        yield x+1

g = gen()
next(g)                # 驱动生成器g开始执行到第一个 yield
retval = g.send(1)     # 看似向生成器 gen() 发送数据
print(retval) 
next(g)            # 返回2
retva = g.send(12)
print(retva) 
#g.throw(StopIteration) # 看似向gen()抛入异常
''' 
