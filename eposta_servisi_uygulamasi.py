from datetime import datetime
import os,time


class epostaServisi():
    def __init__(self,isim):
        self.__isim = isim
        self.__uyeler = [("Maru", "Glass", "maruglass@ultramail.com", "abc123")]
        self.__gonderilmiş_mailler = []

    def __str__(self):
        return self.__isim + "servisine hosgeldiniz."

    def uyeOl(self,isim,soyisim,mail,sifre):
        if self.kontrol(mail):
            print("Mail kullanima uygun.")
            yeni_uye = isim,soyisim,mail,sifre
            self.__uyeler.append(yeni_uye)
            print("Kayit gerceklesti")
            input("Devam etmek icin bir tusa basin")
        else:
            print("Bu mail zaten alinmis")
            input("Baska bir mail denemek icin bir tusa basin")
    
    def girisYap(self,mail,sifre):
        if self.sifreKontrol(mail,sifre):
            print("Giris yapildi.")
            time.sleep(1)
            self.kullaniciMenusu(mail)
            
        else:
            print("Mail veya sifre hatalidir.")


    def kullaniciMenusu(self,mail):
        while True:
            os.system("cls")
            print("""
            
               [1]Mail gonder [2]Mail kutusuna git [3]Cikis yap            
            
        
                """)

            secim=int(input("Seciminizi yapiniz."))

            if secim == 1:
                self.mailGonder(mail)
            elif secim == 2:
                self.mailKutusu(mail)
            elif secim == 3:
                break


    def mailGonder(self,mail):
        alici = input("Alicinin mailini giriniz.")
        baslik = input("Mail basligini giriniz.")
        mesaj = input("Mesajinizi yaziniz.")
        yeni_mail=Mail(mail,alici,baslik,mesaj)
        self.__gonderilmiş_mailler.append(yeni_mail)
        print("Mail gonderildi.")
        


    def mailKutusu(self,mail):
        mail_var = False
        for m in self.__gonderilmiş_mailler:
            if m.getGonderici() == mail or m.getAlici() == mail:
                mail_var = True
                print(m)
        if not mail_var:
            print("Mail kutunuz bos.")
        input("Devam etmek icin bir tusa basiniz.")

    def sifreKontrol(self,mail,sifre):
        for uye in self.__uyeler:
            kayitli_mail = uye[2]
            kayitli_sifre = uye[3]
            if kayitli_mail == mail and kayitli_sifre == sifre:
                return True
        return False


    def kontrol(self,mail):
        for uye in self.__uyeler:
            kayitli_mail = uye[2]
            if kayitli_mail == mail:
                return False
        return True



class Mail():
    def __init__(self,gonderen,alan,baslik,mesaj):
        self.__gonderen = gonderen
        self.__alan = alan
        self.__baslik = baslik
        self.__mesaj = mesaj
        self.__tarih = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def getGonderici(self):
        return self.__gonderen

    def getAlici(self):
        return self.__alan
    
    def __str__(self):
        return """ 

        ===============================================================
            
        Gonderici: {gonderici}  Alici: {alici}  Tarih: {tarih}

        ===============================================================

        Baslik = {konu_basligi}

        ===============================================================
               
        Mesaj: {mesaj}
        
        ===============================================================

        """.format(gonderici=self.__gonderen, alici=self.__alan, tarih=self.__tarih, konu_basligi=self.__baslik, mesaj = self.__mesaj)



e1 = epostaServisi("Ultra Mail")

menu = """
        {baslik}
        [1]Yeni mail adresi al
        [2]Giris yap
        [3]Cikis



""".format(baslik=e1)

while True:
    try:
        os.system("cls")
        print(menu)
        secim = int(input("Seciminizi giriniz: "))

        if secim == 1:
            isim = input("İsim: ")
            soyisim = input("Soyisim: ")
            mail = input("Mail: ")
            sifre = input("Sifre: ")
            if isim and soyisim and mail and sifre:
                e1.uyeOl(isim,soyisim,mail,sifre)
            else:
                print("Tum bilgileri gerekmektedir.")


        elif secim == 2:
            e1.girisYap(mail=input("Mail: "),sifre=input("Sifre: "))

        elif secim == 3 :
            quit()

        else:
            raise ValueError("Girdiginiz sayilar sadece 1 2 3 olabilir.")
    
    except ValueError as mesaj:
        print("Gecersiz bir deger girdiniz: " + str(mesaj))
        time.sleep(1)