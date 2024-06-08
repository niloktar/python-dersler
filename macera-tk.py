import random
import tkinter as tk

def basla():
    intro()

def intro():
    baslik_etiket.config(text="Hazine Avı Oyununa Hoş Geldiniz Pamuk Prenses/Avcı")
    aciklama_etiket.config(text="Ormanda kayboldunuz!\nKurtulmak için bir yol bulmalısınız.\nDikkatli olun ve seçimlerinizi dikkatli yapın!\n")
    secim1_buton.config(text="Ormanda Devam Et", command=ormanda_devam)
    secim2_buton.config(text="Geri Dön", command=geri_don)
    secim1_buton.pack_forget()
    secim2_buton.pack_forget()
    secim1_buton.pack(pady=20)
    secim2_buton.pack(pady=20)

def ormanda_devam():
    baslik_etiket.config(text="Ormanda Devam Ediyorsunuz...")
    aciklama_etiket.config(text="Bir nehirle karşılaştınız.\nNehri yüzerek mi geçmeli yoksa başka bir yol mu aramalısınız?")
    secim1_buton.config(text="Yüzerek geç", command=nehri_gec)
    secim2_buton.config(text="Ormanda Yol Ara", command=baska_yol)
    secim1_buton.pack_forget()
    secim2_buton.pack_forget()
    secim2_buton.pack(pady=20)  # Baska_yol butonunu görünür yap
    secim1_buton.pack(pady=20)

def geri_don():
    baslik_etiket.config(text="Geri Dönüyorsunuz...")
    aciklama_etiket.config(text="Ormanın derinliklerinde kayboldunuz...\nBu sefer başarılı olamadınız!")
    secim1_buton.config(text="Baştan Başla", command=basla)
    secim1_buton.pack_forget()
    secim1_buton.pack(pady=20)

def nehri_gec():
    baslik_etiket.config(text="Nehri Geçiyorsunuz...")
    aciklama_etiket.config(text="Tebrikler! Nehri geçtiniz.\nBir hazine sandığı buldunuz\nSandığın parolasını tahmin et!\n1 ile 10 arasında bir sayıyı tahmin et.")
    secim1_buton.config(text="Tahmin Et", command=tahmin_oyunu)
    secim1_buton.pack_forget()
    secim1_buton.pack(pady=20)

def baska_yol():
    baslik_etiket.config(text="Ormanda Yol Arıyorsunuz...")
    aciklama_etiket.config(text="Canavarınızla karşılaştınız!\nCanavarla savaşmalı mısınız yoksa geri dönmeli misiniz?")
    secim1_buton.config(text="Canavarla Savaş", command=canavarla_yuzles)
    secim2_buton.config(text="Geri Dön", command=geri_don)
    secim1_buton.pack_forget()
    secim2_buton.pack_forget()
    secim1_buton.pack(pady=20)
    secim2_buton.pack(pady=20)

def canavarla_yuzles():
    baslik_etiket.config(text="Canavarla Savaşıyorsunuz...")
    aciklama_etiket.config(text="Yaralandınız!\n")
    secim1_buton.config(text="Ormanda tedavi", command=iyiles)
    secim2_buton.config(text="Baştan Başla", command=basla)
    secim1_buton.pack_forget()
    secim2_buton.pack_forget()
    secim1_buton.pack(pady=20)
    secim2_buton.pack(pady=20)
    
def canavarla_yeni_yuzles():
    baslik_etiket.config(text="Canavarla Savaşıyorsunuz...")
    baslik_etiket.config(text="Hangi silahı tercih edeceksiniz")
    secim1_buton.config(text="Sihirli Asa", command=asa)
    secim2_buton.config(text="Zehirli Şişe", command=zehir)
    secim1_buton.pack_forget()
    secim2_buton.pack_forget()
    secim1_buton.pack(pady=20)
    secim2_buton.pack(pady=20)
    
def asa():
    baslik_etiket.config(text="Canavarı sis bulutuna çevirdiniz")
    aciklama_etiket.config(text="Kazandınız!\nHazine için tahmin oyunu oynayalım!")
    secim1_buton.config(text="Tahmin Et", command=tahmin_oyunu)
    secim1_buton.pack_forget()
    secim1_buton.pack(pady=20)
    
def zehir():
    baslik_etiket.config(text="Canavarın zehre bağışıklığı varmış")
    aciklama_etiket.config(text="Yaralandınız!\nBelki bir sonraki sefer daha şanslı olursunuz!")
    secim1_buton.config(text="Baştan Başla", command=basla)
    secim1_buton.pack_forget()
    secim1_buton.pack(pady=20)

def iyiles():
    baslik_etiket.config(text="Yaranızı tedavi etmek için\n iki yolunuz var")
    secim1_buton.config(text="Ormanda tedavi ara", command=orman_tedavi)
    secim2_buton.config(text="Nehre gidip yarayı yıka", command=nehir_tedavi)
    secim1_buton.pack_forget()
    secim2_buton.pack_forget()
    secim1_buton.pack(pady=20)
    secim2_buton.pack(pady=20)

def orman_tedavi():
    baslik_etiket.config(text="Ormanda büyücüyle karşılaştınız")
    secim1_buton.config(text="Büyücüye güven", command=buyucu_guven)
    secim2_buton.config(text="Nehre gidip yarayı yıka", command=nehir_tedavi)
    secim1_buton.pack_forget()
    secim2_buton.pack_forget()
    secim1_buton.pack(pady=20)
    secim2_buton.pack(pady=20)
    
def buyucu_guven():
    baslik_etiket.config(text="Büyücü size iki seçenek sundu")
    secim1_buton.config(text="Büyülü elma", command=elma)
    secim2_buton.config(text="Altın havuç", command=havuc)
    secim1_buton.pack_forget()
    secim2_buton.pack_forget()
    secim1_buton.pack(pady=20)
    secim2_buton.pack(pady=20)

def nehir_tedavi():
    baslik_etiket.config(text="Boğuldunuz...")
    secim1_buton.config(text="Baştan", command=basla)
    secim1_buton.pack_forget()
    secim1_buton.pack(pady=20)
    
def elma():
    baslik_etiket.config(text="Elmayı yiyerek uykuya daldınız.\n Büyücü sizi kandırdı.")
    secim1_buton.config(text="Baştan Başla", command=basla)
    secim1_buton.pack_forget()
    secim1_buton.pack(pady=20)
    
def havuc():
    baslik_etiket.config(text="Altın havuç yaranızı iyileştirdi\ndevam edebilirsiniz.")
    baslik_etiket.config(text="Doğru seçim yaptığınız için\nbüyücü sizi ödüllendirdi.")
    secim1_buton.config(text="Ödülü al", command=silah)
    secim1_buton.pack_forget()
    secim1_buton.pack(pady=20)
    
def silah():
    baslik_etiket.config(text="Asayı seçtiniz\n hazine avına devam edebilirsiniz.")
    baslik_etiket.config(text="İki seçeneğiniz var..")
    secim1_buton.config(text="Canavarla Yüzleş", command=canavarla_yeni_yuzles)
    secim2_buton.config(text="Geri dön", command=geri_don)
    secim1_buton.pack_forget()
    secim2_buton.pack_forget()
    secim1_buton.pack(pady=20)
    secim2_buton.pack(pady=20)

def tahmin_oyunu():
    global tahmin_hakki  # Declare tahmin_hakki as a global variable
    tahmin_hakki = 3

    def kontrol_et():
        global tahmin_hakki  # Refer to the globally defined variable
        try:
            tahmin = int(tahmin_girisi.get())
        except ValueError:
            return

        rastgele_sayi = random.randint(1, 10)

        if tahmin == rastgele_sayi:
            kazandi()
        elif tahmin_hakki > 1:
            tahmin_hakki -= 1
            tahmin_girisi.delete(0, tk.END)
            aciklama_etiket.config(text=f"Yanlış tahmin! {tahmin_hakki} tahmin hakkınız kaldı. Yeniden deneyin.")
        else:
            kaybettiniz(tahmin_buton)  # tahmin_buton'u kaybettiniz fonksiyonuna geçir

    tahmin_girisi = tk.Entry(pencere)
    tahmin_girisi.pack(pady=10)

    tahmin_buton = tk.Button(pencere, text="Tahmin Et", command=kontrol_et)
    tahmin_buton.pack(pady=10)

    secim1_buton.pack_forget()  # Hide
    secim2_buton.pack_forget()  # Hide

def kazandi():
    """Kazanma ekranı oluşturur ve oyunu sonlandırır."""
    baslik_etiket.config(text="Tebrikler!")
    aciklama_etiket.config(text="Hazineyi buldunuz! Oyunu kazandınız!")
    
def kaybettiniz(tahmin_buton):
    """Kaybetme ekranı oluşturur ve oyunu sonlandırır."""
    baslik_etiket.config(text="Malesef!")
    aciklama_etiket.config(text="Tahmin hakkınız bitti. Oyunu kaybettiniz!")

    # Tahmin butonunu devre dışı bırak
    tahmin_buton.config(state="disabled")

    # Yeniden başlama butonunu oluştur
    yeniden_basla = tk.Button(pencere, text="Yeniden Başla", font=("Arial", 12), command=basla)
    yeniden_basla.pack(pady=20)

# Pencere ve oyun başlatma
pencere = tk.Tk()
pencere.title("Hazine Avı Oyunu")

baslik_etiket = tk.Label(pencere, text="", font=("Arial", 18))
baslik_etiket.pack(pady=20)

aciklama_etiket = tk.Label(pencere, text="", font=("Arial", 12))
aciklama_etiket.pack(pady=10)

secim1_buton = tk.Button(pencere, text="", font=("Arial", 12))
secim2_buton = tk.Button(pencere, text="", font=("Arial", 12))

basla()  # Oyunu başlat

pencere.mainloop()  # Pencereyi çalıştır

