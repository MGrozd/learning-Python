# DESKTOP-8VOCI2K
from threading import *
from socket import *

class Posluzitelj:
    def  __init__(self, hostname, port):
        self.H = hostname
        self.P = port
        self.S = socket()
        self.S.bind((self.H, self.P))
        self.S.listen(5)
        while True:
            print('Čekam klijenta...')
            s, d = self.S.accept()
            print('Klijent spojen')
            t = Thread(target = self.cekaj_poruke, args = (s,))
            t.start()
        return

    def prost(self, n):
        for i in range(2, round(n ** 0.5 + 1)):
            if n % i == 0:
                return False
        return True

    def cekaj_poruke(self, s):
        gotovo = False
        while not gotovo:
            try:
                n = int(s.recv(1024).decode('utf-8'))
                print('Broj: {}'.format(n))
                if n < 2:
                    gotovo = True
                elif self.prost(n):
                    s.send('Broj: {} je prost'.format(n).encode('utf-8'))
                else:
                    s.send('Broj {} nije prost'.format(n).encode('utf-8'))
            except:
                gotovo = False
        print('Klijent odspojen')
        s.close()
        return


if __name__ == '__main__':
    P = Posluzitelj('DESKTOP-8VOCI2K', 10002)
