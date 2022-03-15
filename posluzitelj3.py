## Posluzitelj
from socket import *
from threading import *

class Korisnik:
    def __init__(self, s, ime):
        self.S = s
        self.I = ime
        return

    def salji(self, p):
        self.S.send(p.encode('utf-8'))
        return

class Posluzitelj:
    def __init__(self, host, port):
        self.H = host
        self.P = port
        self.S = socket()
        self.S.bind((self.H, self.P))
        self.S.listen(6)
        self.K = []
        return

    def start(self):
        while True:
            print('Čekam klijenta...')
            c, t = self.S.accept()
            print('Spojen klijent {0}'.format(t))
            p = c.recv(1024).decode('utf-8')
            k = Korisnik(c, p)
            self.K.append(k)
            self.saljiSvima('{0} je došao na chat'.format(p))
            t = Thread(target = self.citaj, args = (k,))
            t.start()
        return

    def saljiSvima(self, p):
        for t in self.K:
            t.salji(p)
        return

    def citaj(self, k):
        while True:
            p = k.S.recv(1024).decode('utf-8')
            if p == '@kraj@':
                self.saljiSvima('{0} je napustio chat'.format(k.I))
                ## Brišemo korisnika iz liste
                del(self.K[self.K.index(k)])
                ## prekidamo izvođenje dretve
                return
            else:
                self.saljiSvima('{0}:: {1}'.format(k.I, p))
        return

if __name__ == '__main__':
    s = Posluzitelj('DESKTOP-8VOCI2K', 10002)
    s.start()
