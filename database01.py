import sqlite3

baglanti = sqlite3.connect('deneme.sqlite3')
cursor = baglanti.cursor()

def tablo_olustur():
    cursor.execute('create table if not exists ogrenci (isim TEXT, soyisim TEXT, no INT)')
    baglanti.commit()
    print('Tablo Oluşturuldu.')



def veri_ekle():
    cursor.execute("insert into ogrenci Values('Mervan','Koncuk',01)")
    cursor.execute("insert into ogrenci Values('umur','savut',02)")
    baglanti.commit()
    print('Veri Eklendi')


def veri_ekle2():
    isim = input("Bir isim giriniz: ")
    soyisim= input('Soyisim giriniz: ')
    no =int(input('Noyu giriniz'))
    cursor.execute("insert into ogrenci Values(?,?,?)",(isim,soyisim,no))
    baglanti.commit()
    print("Veriler Eklendi")

def veri_cek():
    cursor.execute("select * from ogrenci")
    liste = cursor.fetchall()
    for i in liste: 
        print(i)

def veri_guncelleme(isim,no):
    cursor.execute("update ogrenci set isim=? where no=?",(isim,no))
    baglanti.commit()
    print("Veri Güncellendi")

def veri_sil(isim):
    cursor.execute("delete from ogrenci where isim=?",(isim,))
    baglanti.commit()
    print("Veri Silindi")

def tablo_sil():
    cursor.execute("drop table ogrenci")
    baglanti.commit()
    print("Tablo Silindi")




tablo_olustur()
veri_ekle()
veri_ekle2()