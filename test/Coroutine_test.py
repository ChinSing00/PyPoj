def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'
        s =  '4565'

def produce(con):
    con.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = con.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    con.close()

con = consumer()
produce(con)
