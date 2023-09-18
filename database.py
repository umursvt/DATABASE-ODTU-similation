import sqlite3

con = sqlite3.connect("kütüphane.db")
cursor = con.cursor()

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT,Yazar TEXT, Yayınevi TEXT, SayfaSayısı INT)")
    con.commit()

def veri_ekle():
    cursor.execute("insert into kitaplık Values('İstanbul Hatırası','Ahmet Ümit','Everest','561')")
    con.commit()


def ver_al():
    cursor.execute("select * from kitaplık")
    liste =cursor.fetchall()
    for i in liste:
        print(i)

def veri_al_2():
    cursor.execute("select İsim,Yazar from kitaplık")
    liste=cursor.fetchall()
    for i in liste:
        print(i)

def verileri_al_3(x):
    cursor.execute("select * from kitaplık where Yazar = ?",(x))
    liste = cursor.fetchall()
    for i in liste:
        print(i)

def guncelle(y,x):
    cursor.execute("update kitaplık set Yazar=? where İsim=? ",(y,x))
    con.commit()


def verileri_sil(x):
    cursor.execute("Delete from kitaplık where Yazar=?",(x,))
    con.commit()

veri_ekle()

verileri_sil("Ahmet Ümit")
con.close()
