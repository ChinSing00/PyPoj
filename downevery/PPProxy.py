import BaseSpi
import urllib 
import threading


class IpPool():


	def __init__(self):
		self._1url = 'http://www.xicidaili.com/nt/'
		self._2url = 'None' 
		self._1rule = '<td>(\d.*?)</td>'
		self.ip_pool = self._Get()
		self.pool = []
		

	def check(self,i):
		proxy = self.ip_pool[i]
		try:
			proxy_support = urllib.request.ProxyHandler(proxy)
			opener = urllib.request.build_opener(proxy_support)
			opener.addheaders=[("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64)")]	
			urllib.request.install_opener(opener)
			res = urllib.request.urlopen('http://1212.ip138.com/ic.asp').read()
			if res == '':
				return False
			print('**%s**',i)
			lock.acquire()
			print('_______'+i+'_______'+proxy)    
			self.pool.append(proxy)
			lock.release()   
			return True
		except Exception as e:
			return False


	def _Get(self):
		ip_pool = []
		ip_temp = []
		gPage = BaseSpi.basespi()
		for pNum in range(2,6):
			url = self._1url+str(pNum)
			pageCode = gPage.getPage(url).decode('utf-8')
			ip_page = gPage._regx(self._1rule,pageCode)
			ip_temp.extend(ip_page)
			for i in range(0,len(ip_temp),4):
				proxy_host = ip_temp[i]+':'+ip_temp[i+1]
				proxy_temp = {"http":proxy_host}
				ip_pool.append(proxy_temp)	
		return ip_pool


	def _GetPool(self):
		threads=[]
		for i in range(len(self.ip_pool)):
			thread  = threading.Thread(target=self.check,args=[i])
			threads.append(thread)
			thread.start()
		for thread in threads:
			thread.join
		return self.pool