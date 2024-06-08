import random

#bu oyunda 3 elde kazanan oyunu kazanır.
#Bu program, kullanıcının her turda taş, kağıt veya makas seçimini alır 
# ve bilgisayarın rasgele bir seçim yapmasını sağlar. 
# Ardından, her iki seçimin sonucunu karşılaştırır ve sonucu ekrana yazdırır. 
# Skorlar her tur sonunda güncellenir ve sonunda en yüksek skora sahip oyuncu kazanır.
# Son olarak, oyun sonunda kazanan açıklanır ve oyun biter.

print("Taş-Kağıt-Makas oyununa hoş geldiniz!")
oyuncu_skor = 0
yapayzeka_skor = 0

for round in range(3):
    print(f"--- {round+1}. Tur ---")

    secenekler = ["taş", "kağıt", "makas"]
    yapayzeka_secimi = random.choice(secenekler)
    
    oyuncu_secimi = input("Taş mı, kağıt mı, makas mı? ").lower()
    while oyuncu_secimi not in secenekler:
        oyuncu_secimi = input("Geçersiz seçim! Tekrar deneyin (taş/kağıt/makas): ").lower()

    print("Bilgisayarın seçimi: ", yapayzeka_secimi)

    if oyuncu_secimi == yapayzeka_secimi:
        print("Berabere!")
    elif oyuncu_secimi == "taş":
        if yapayzeka_secimi == "kağıt":
            print("Kaybettiniz! Kağıt Taşı Sarar!")
            yapayzeka_skor += 1
        else:
            print("Tebrikler! Kazandınız. Makas Kağıdı Keser.")
            oyuncu_skor += 1
    elif oyuncu_secimi == "kağıt":
        if yapayzeka_secimi == "makas":
            print("Kaybettiniz! Makas Kağıdı Keser.")
            yapayzeka_skor += 1
        else:
            print("Tebrikler! Kazandınız. Taş Makası Kırar.")
            oyuncu_skor += 1
    elif oyuncu_secimi == "makas":
        if yapayzeka_secimi == "taş":
            print("Kaybettiniz! Taş Makası Kırar.")
            yapayzeka_skor += 1
        else:
            print("Tebrikler! Kazandınız. Bilgisayar kağıt seçti.")
            oyuncu_skor += 1

    print(f"Aktif Skor: Oyuncu {oyuncu_skor} - Bilgisayar {yapayzeka_skor}\n")

print("Oyun Bitti!")
if oyuncu_skor > yapayzeka_skor:
    print(f"Tebrikler! Oyuncu kazandı! ({oyuncu_skor} - {yapayzeka_skor})")
elif oyuncu_skor < yapayzeka_skor:
    print(f"Kaybettiniz! Bilgisayar kazandı. ({oyuncu_skor} - {yapayzeka_skor})")
else:
    print("Oyun berabere!")
