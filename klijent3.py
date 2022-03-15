# klijent
from socket import *
from tkinter import *
from threading import *
from tkinter.simpledialog import *

class Klijent(Frame):
    def __init__(self, host, port):
        self.H = host
        self.P = port
        self.S = socket()
        self.S.connect((self.H, self.P))
        self.kreirajSucelje()
        p = askstring('Chat', 'Upišite ime')
        self.S.send(p.encode('utf-8'))
        return

    def kreirajSucelje(self):
        self.R = Tk()
        super().__init__(self.R)
        self.R.title('Chat')
        self.R.protocol('WM_DELETE_WINDOW', self.close)
        self.grid()
        self.T = Text(self)
        self.T.grid(row = 1, column = 1)
        #self.T.bind('<KeyPress>', self.read_only)
        self.UV = StringVar()
        self.V = Entry(self, textvariable =self.UV)
        self.V.grid(row = 2, column = 1)
        self.V.bind('<KeyPress-Return>', self.salji)
        return

    def salji(self, e):
        t = self.UV.get()
        self.UV.set('')
        self.S.send(t.encode('utf-8'))
        return

    def close(self):
        self.S.send('@kraj@'.encode('utf-8'))
        self.R.destroy()
        return

    def citaj(self):
        while True:
            try:
                t = self.S.recv(1024).decode('utf-8')
                self.T.insert(END, t+ '\n')
            except:
                return
        return

if __name__ == '__main__':
    k = Klijent('DESKTOP-8VOCI2K', 10002)
    t = Thread(target = k.citaj)
    t.start()

def read_only(self, e):
    return 'break'
