from socket import *

class Klijent:
    def __init__(self, posluzitelj, port):
        self.H = posluzitelj
        self.P = port
        self.S = socket()
        self.S.connect((self.H, self.P))
        t = 2
        while t >= 2:
            t = int(input('Unsei broj (manji od 2 za kraj): '))
            self.S.send(str(t).encode('utf-8'))
            print(self.S.recv(1024).decode('utf-8'))
        self.S.close()
        return

if __name__ == '__main__':
    k = Klijent('DESKTOP-8VOCI2K', 10002)
