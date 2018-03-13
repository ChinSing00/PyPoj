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



from bs4 import BeautifulSoup
from bs4 import element

soup = BeautifulSoup(open('rrs.html',encoding = 'utf-8'),'lxml')

#aas = soup.find('div',id='content')
#print(aas.get_text())

soup = list(filter(lambda x: type(x) == element.Tag, soup))
for x in soup:
	print(str(x.get_text()),'\n'+'---------------'*8)