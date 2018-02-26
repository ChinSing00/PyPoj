import urllib.request


header='http://'
print('输入你要爬取得网址:')
url = input()
url=header+url
try:
    webPage = urllib.request.urlopen(url)
    data = webPage.read()
    print()
    print('\n\n\n')
    print(type(webPage))
    print(webPage.geturl())
    print(webPage.info())
    url = input()
except urllib.error.URLError:
    print('------------------网址输入错误----------------')
finally:
    print('------------------完成----------------')
