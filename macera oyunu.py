import random
import time

def intro():
    print("Hazine avı oyununa hoş geldiniz")
    time.sleep(1)
    print("Ormanda kayboldunuz!")
    time.sleep(1)
    print("Kurtulmak için bir yol bulmalısınız.")
    time.sleep(1)
    print("Dikkatli olun ve seçimlerinizi dikkatli yapın!\n")

def kazandiniz():
    print("Tebrikler, ormandan başarıyla kurtuldunuz, hazineye ulaştınız!")
    quit()

def kayboldunuz():
    print("Üzgünüz, ormanda kaybolup mahsur kaldınız.")
    print("Belki bir sonraki sefer daha şanslı olursunuz!")
    quit()
    
def yaralandınız():
    print("Üzgünüz, canavarla savaşırken yaralandınız.")
    print("Belki bir sonraki sefer daha şanslı olursunuz!")
    secim_yap()
    
def kaybettiniz():
    print("Üzgünüz, canavar sizi yakaladı.")
    print("Belki bir sonraki sefer daha şanslı olursunuz!")
    quit()

def boguldunuz():
    print("Üzgünüz, nehirde yüzerek boguldunuz.")
    print("Belki bir sonraki sefer daha şanslı olursunuz!")
    quit()

def secim_yap():
    print("Karşınıza iki yol çıktı:")
    print("1. Ormanda devam etmek")
    print("2. Yavaşça geri dönmek")
    secim = input("Hangi yol? (1/2): ")
    if secim == "1":
        ormanda_devam()
    elif secim == "2":
        geri_don()
    else:
        print("Geçersiz giriş. Lütfen 1 veya 2 seçeneğinden birini girin.")
        secim_yap()
        
def canavarla_yuzles():
    print("Karşına bir canavar çıktı:")
    print("1. Canavarla savaş")
    print("2. Yavaşça geri dönmek")
    secim = input("Hangi yol? (1/2): ")
    if secim == "1":
        yaralandınız()
    elif secim == "2":
        kaybettiniz()
    else:
        print("Geçersiz giriş. Lütfen 1 veya 2 seçeneğinden birini girin.")
        secim_yap()
        
def nehri_gec():
    print("Karşınıza iki seçenek çıktı:")
    print("1. Nehri yüzerek geç")
    print("2. Ormanda başka yol ara")
    secim = input("Hangi seçenek? (1/2): ")
    if secim == "1":
        boguldunuz()
    elif secim == "2":
        canavarla_yuzles()
    else:
        print("Geçersiz giriş. Lütfen 1 veya 2 seçeneğinden birini girin.")
        secim_yap()

def ormanda_devam():
    print("Ormanda devam ediyorsunuz...")
    time.sleep(1)
    print("Bir nehirle karşılaştınız.")
    time.sleep(1)
    print("Nehri yüzerek mi geçmeli yoksa başka bir yol mu aramalısınız?")
    eylem = input("Nasıl devam etmelisiniz? (yüz/geç): ")
    if eylem.lower() == "geç":
        print("Nehri köprüden geçiyorsunuz.")
        tahmin_oyunu("Hazineyi açmak için")
    elif eylem.lower() == "yüz":
        print("Boğulabilirsiniz, belki de diğer yol daha güvenlidir.")
        nehri_gec()
    else:
        print("Geçersiz giriş. Lütfen 'yüz' veya 'geç' seçeneğinden birini girin.")
        ormanda_devam()

def geri_don():
    print("Geri dönüyorsunuz...")
    time.sleep(1)
    print("Ormanın derinliklerinde kayboldunuz...")
    time.sleep(1)
    print("Bu sefer başarılı olamadınız!")
    kayboldunuz()

def tahmin_oyunu(mesaj):
    print("Tebrikler, nehri geçtiniz")
    print(f"\n{mesaj} bir tahmin oyunu oynayalım!")
    print("1 ile 10 arasında bir sayıyı tahmin etmelisiniz.")
    rastgele_sayi = random.randint(1, 10)
    tahmin_hakki = 3
    while tahmin_hakki > 0:
        tahmin = int(input("Tahmininiz: "))
        if tahmin == rastgele_sayi:
            print("Tebrikler! Doğru tahmin ettiniz!")
            kazandiniz()
        elif tahmin < rastgele_sayi:
            print("Daha yüksek bir sayı girin.")
        else:
            print("Daha düşük bir sayı girin.")
        tahmin_hakki -= 1
        print("Kalan tahmin hakkınız:", tahmin_hakki)
    print("Üzgünüm, tahmin hakkınız bitti.")
    print("Doğru sayı:", rastgele_sayi)
    kaybettiniz()

def main():
    intro()
    secim_yap()

if __name__ == "__main__":
    main()
