import random

#bu oyunda skor tutuyoruz.
# Bu program, kullanıcının taş, kağıt veya makas seçimini alır ve ardından bilgisayarın rasgele bir seçim yapmasını sağlar. 
# Ardından, her iki seçimin sonucunu karşılaştırır ve sonucu ekrana yazdırır. 
# Skorlar her seferinde güncellenir ve sonuçta en yüksek skora sahip oyuncu kazanır.
# Son olarak, kullanıcıya yeniden oynamak isteyip istemediğini sorar.
#  Kullanıcı 'E' harfine basarsa, oyun yeniden başlar. 'H' harfine basarsa, program sonlandırılır.

print("Taş-Kağıt-Makas oyununa hoş geldiniz!")
oyuncu_skor = 0
yapayzeka_skor = 0

while True:
    secenekler = ["taş", "kağıt", "makas"]
    yapayzeka_secimi = random.choice(secenekler)
    
    oyuncu_secimi = input("Taş mı, kağıt mı, makas mı? ").lower()
    while oyuncu_secimi not in secenekler:
        oyuncu_secimi = input("Geçersiz seçim! Tekrar deneyin (taş/kağıt/makas): ").lower()

    print("Bilgisayarın seçimi: ", yapayzeka_secimi)

    if oyuncu_secimi == yapayzeka_secimi:
        print("Berabere! Tekrar deneyin.")
    elif oyuncu_secimi == "taş":
        if yapayzeka_secimi == "kağıt":
            print("Kaybettiniz! Bilgisayar kağıt seçti.")
            yapayzeka_skor += 1
        else:
            print("Tebrikler! Kazandınız. Bilgisayar makas seçti.")
            oyuncu_skor += 1
    elif oyuncu_secimi == "kağıt":
        if yapayzeka_secimi == "makas":
            print("Kaybettiniz! Bilgisayar makas seçti.")
            yapayzeka_skor += 1
        else:
            print("Tebrikler! Kazandınız. Bilgisayar taş seçti.")
            oyuncu_skor += 1
    elif oyuncu_secimi == "makas":
        if yapayzeka_secimi == "taş":
            print("Kaybettiniz! Bilgisayar taş seçti.")
            yapayzeka_skor += 1
        else:
            print("Tebrikler! Kazandınız. Bilgisayar kağıt seçti.")
            oyuncu_skor += 1

    print(f"Aktif Skor: Oyuncu {oyuncu_skor} - Bilgisayar {yapayzeka_skor}")

    play_again = input("Tekrar oynamak istiyor musunuz? (E/H) ").lower()
    if play_again != "e":
        break

print("Oyundan çıktınız. Tekrar bekleriz!")
