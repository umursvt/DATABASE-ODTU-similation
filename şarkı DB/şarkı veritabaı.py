import sqlite3

class Playlist():
    def __init__(self,name):
        self.name = name
        self.status = True
        self.connect()

    def run(self):
        self.menu()
        self.status= True

        choice= self.choice()

        if choice == 1:
            self.sarkiEkle()
        elif choice == 2:
            self.sarkiSil()
        elif choice == 3:
            self.sureHesap()
        elif choice == 4:
            self.tumSarkilar()
        elif choice == 5:
            self.status=False




    def menu(self):
        print("************")
        print(""""
        1)Şarkı Ekle\n
        2)Şarkı Sil\n
        3)Toplam Süre\n
        4)Tüm Şarkılar\n
        5)Çıkış
        """)

    def choice(self):
        while True:
            try:
                progress=int(input("Seçiminiz:"))
                if progress <1 or progress >5:
                    print("Yanlış giriş. 1-5 için seçim yapınız")
                    continue
                break
            except ValueError:
                print("Hatalı giriş. sadece rakam!")
        return progress


    def sarkiEkle(self):
        isim = input("şarkı ismi: ").lower().capitalize()
        sanatci = input("Sanatçı: ").lower().capitalize()
        while True:
            try:
                sure = float(input("Süre:"))
                break
            except:
                print("hatalı giriş")
        self.cursor.execute("INSERT INTO Sarkilar VALUES('{}','{}',{})".format(isim,sanatci,sure))
        self.connect.commit()
        print("{}' {}' şarkısı Eklendi".format(sanatci,isim))

    def sarkiSil(self):
        self.cursor.execute("SELECT * FROM Sarkilar")
        tum_sarkilar=self.cursor.fetchall()
        string_sarkilar= lambda x:[str(y) for y in x]
        for i,j in enumerate(tum_sarkilar,1):
            print("{}) {}".format(i," ".join(string_sarkilar(j))))

        while True:
            try:
                secim=int(input("Silinecek Şarkıyı Seç:"))
                break
            except ValueError:
                print("Yanlış giriş. Sadece sayı girişi")
        self.cursor.execute("DELETE FROM Sarkilar Where rowid={}".format(secim))
        self.connect.commit()
        print("ŞARKI SİLİNDİ.")




    def connect(self):
        self.connect = sqlite3.connect("Sarki.db")
        self.cursor=self.connect.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Sarkilar(sakiismi TEXT, sanatci TEXT, süre INT)")
        self.connect.commit()

    def sureHesap(self):
        self.cursor.execute("SELECT SUM(süre) FROM Sarkilar")
        print(self.cursor.fetchall()[0])
        self.connect.commit()

    def tumSarkilar(self):
        self.cursor.execute("SELECT * FROM Sarkilar")
        tumSarkilar =self.cursor.fetchall()
        converted = lambda x:[str(y) for y in x]

        for i, j in enumerate(tumSarkilar,1):
            print("{}) {}".format(i," ".join(converted(j))))
        self.connect.commit()



sarki=Playlist("Kafama Göre")
while sarki.status:
    sarki.run()