from multiprocessing import *
from time import *

def prost(n):
    for i in range(2, round(n ** 0.5 + 1)):
        if n % i == 0:
            return False
    return True

def prosti(p):
    pr = current_process()
    a, b = p
    print('proces: {}; Posao: {}'.format(pr.name, p))
    t = 0
    for i in range(a, b):
        if prost(i):
            t += 1
    return t

if __name__ == '__main__':
    a = 2
    b = 1000001
    n = 4
    m = 1000
    d = (b - a) // m
    poc = process_time()
    p = Pool(n)
    a = p.map(prosti, [(a + i * d, a + (i + 1) * d) for i in range(m)])
    kraj = process_time()
    print('{:.5f}'.format(kraj - poc))
    print('Ukupno brojeva: {}'.format(sum(a)))
