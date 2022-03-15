from multiprocessing import Process
from time import *

def prost(n):
    for i in range(2, round(n ** 0.5 + 1)):
        if n % i == 0:
            return False
    return True

def prosti(a, b):
    t = 0
    for i in range(a, b):
        if prost(i):
            t += 1
    return t

if __name__ == '__main__':
    a = 2
    b = 1000001
    n = 2
    d = (b - a) // n
    poc = process_time()

    p = [Process(target=prosti, args=(a + i * d, a + (i + 1) * d)) for i in range(n)]
    for t in p:
        t.start()
    for t in p:
        t.join()
    kraj = process_time()
    print('{:.5f}'.format(kraj - poc))
