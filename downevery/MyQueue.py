from multiprocessing import Queue 

q = Queue(10)#初始化一个Queue对象，最多可接收三条put消息
for i in range(1,11):
	print(i)
	q.put('message-%s'%i)
print(q.full())#False,是否满了
 
#因为消息队列已满，下面的try都会抛出异常，第一个try会等待2秒后再抛出异常，第二个try会立即抛出异常
try:
    q.put('message-11',True,2)
except:
    print('except1,消息队列已满，现有消息数量：%s'%q.qsize())
 
try:
    q.put_nowait('message-11')
except:
    print('except2,消息队列已满，现有消息数量：%s'%q.qsize())
 
#判断队列是否已满
if not q.full():
    q.put_nowait('message-11')
 
#读取消息时，先判断消息队列是否为空，在读取
if not q.empty():
    for i in range(q.qsize()):
        print(q.get())#q.get会阻塞，q.get_nowait()不阻塞，但会抛异常  
print(q.qsize())