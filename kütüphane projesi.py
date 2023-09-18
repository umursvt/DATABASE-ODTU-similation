import  sqlite3
import time


class Kitap():
    def __init__(self,isim,yazar,yayinevi,tur,baski):
        self.isim = isim
        self.yazar = yazar
        self.yayinevi = yayinevi
        self.tur = tur
        self.baski = baski

    def __str__(self):
        return  """
        Kitap ismi: {} \n
        Yazar: {} \n
        Yayıınevi: {} \n
        Tür: {} \n
        Baskı: {} \n        
        """.format(self.isim,self.yazar,self.yayinevi,self.tur,self.baski)


class Kutuphane():
            def __init__(self):
                self.baglanti_olustur()


            def baglanti_olustur(self):
                self.baglanti=sqlite3.connect("Kütüphane.db")
                self.cursor =self.baglanti.cursor()
                sorgu= "Creat table if not exists kitaplar(isim TEXT, yazar TEXT, yayinevi TEXT, tur TEXT, baski INT"
                self.cursor.execute(sorgu)
                self.baglanti.commit()

            def baglanti_kes(self):
                self.baglanti.close()


            def kitaplari_goster(self):
                sorgu="select * from kitaplar"
                self.cursor.execute(sorgu)
                kitaplar=self.cursor.fetchall()

                if len(kitaplar) == 0:
                    print("Kütüphanede kitap yok")

                else:
                    for i in kitaplar:
                        kitap =Kitap(i[0],i[1],i[2],i[3],i[4])
                        print(kitap)

            def kitap_sorgula(self,isim):
                sorgu="select * from kitapar where isim=?"
                self.cursor.execute(sorgu,(isim,))

                kitaplar=self.cursor.fetchall()

                if len(kitaplar) == 0:
                    print(isim, "diye bir kitap yok")

                else:
                    kitap = Kitap(kitaplar[0][0],kitaplar[0][1],kitaplar[0][2],kitaplar[0][3],kitaplar[0][4])
                    print(kitap)


            def kitap_ekle(self,kitap):
                sorgu="insert into kitaplar Values(?,?,?,?,?)"
                self.cursor.execute(sorgu,(kitap.isim,kitap.yazar,kitap.yayinevi,kitap.tur,kitap.baski))
                self.baglanti.commit()

            def kitap_sil(self,isim):
                sorgu="Delete from kitaplar where=?"
                self.cursor.execute(sorgu,isim)


            def baski_yukselt(self,isim):
                sorgu ="selct * from kitaplar where isim=?"
                self.cursor.execute(sorgu,(isim,))
                kitaplar = self.cursor.fetchall()

                if len(kitaplar) == 0:
                    print("Kitap mevcut değil")

                else:
                    baski = kitaplar[0][4]
                    baski += 1
                    sorgu2 = "update kitaplar set baski where isim=?"
                    self.cursor.execute(sorgu2,(baski,isim))
                    self.baglanti.commit()


