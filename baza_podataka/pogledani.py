from sqlite3 import *

#Povezivanje s bazom podataka
conn = connect('pogledani_filmovi_serije.db')
#Kreiranje kursora za izvođenje SQL upita
c = conn.cursor()
upit = '''  CREATE TABLE Godine (
            IDGodine INTEGER PRIMARY KEY AUTOINCREMENT,
            Oznaka INTEGER NOT NULL)'''
#Izvođenje SQL upita
c.execute(upit)
#Spremanje promjena u bazi podataka
conn.commit()
#Kraj rada s bazom podataka
conn.close()

print('Tablica Godine je kreirana')

with connect('pogledani_filmovi_serije.db') as conn:
    c = conn.cursor()
    upit = '''  CREATE TABLE Filmovi (
                Ime TEXT PRIMARY KEY NOT NULL,
                IDGodine INTEGER REFERENCES GodinaIzdanja(IDGodine))'''
    c.execute(upit)
    conn.commit()

print('Tablica Filmovi je kreirana')
