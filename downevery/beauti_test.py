from bs4 import BeautifulSoup
from bs4 import element

soup = BeautifulSoup(open('rrs.html',encoding = 'utf-8'),'lxml')

aas = soup.find('div',id='content')
print(aas.get_text())
#soup = list(filter(lambda x: type(x) == element.Tag, soup))
#for x in soup:
	#print(str(x.get_text()),'\n'+'---------------'*8)