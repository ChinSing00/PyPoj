import time
import threadpool


def sayhello(str):
    print( "Hello ",str)
    time.sleep(2)

name_list =['xiaozi','aa','bb','cc','sdedew','dsffd','wwwww']

start_time = time.time()

pool = threadpool.ThreadPool(3) 
requests = threadpool.makeRequests(sayhello, name_list) 

[pool.putRequest(req) for req in requests] 
pool.wait() 
print( '%d second'% (time.time()-start_time))
