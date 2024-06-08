import random
# Bu program, kullanıcının taş, kağıt veya makas seçimini alır ve 
# ardından bilgisayarın rasgele bir seçim yapmasını sağlar. 
# sonra her iki seçimin sonucunu karşılaştırır ve sonucu ekrana yazdırır. 
# Son olarak, kullanıcıya yeniden oynamak isteyip istemediğini sorar.
# Kullanıcı 'E' harfine basarsa, oyun yeniden başlar. 
# 'H' ya da başka bir harfe basarsa program sonlandırılır.

print("Taş-Kağıt-Makas oyununa hoş geldiniz!")
#while true başlama komutumuz
while True:
    secenekler = ["taş", "kağıt", "makas"]
    #random choice fonksiyonu yapay zekanın karışık bir şekilde üç seneçekten birini seçmesini sağlar.
    yapayzeka_secimi=random.choice(secenekler)
    # lower fonksiyonu kullanıcı girdilerini büyük-küçük harf duyarlılığından kurtarır, 
    # büyük TAŞ ya da taş yazabilirsin.
    # input komutu kullanıcıdan veri almak için kullanıyorduk.
    oyuncu_secimi = input("Taş mı, kağıt mı, makas mı?: ").lower()

    #while eğer anlamına gelir eğer yanlış bir şey yazarsak bu uyarı gelecek.
    while oyuncu_secimi not in secenekler:
        oyuncu_secimi = input("Geçersiz seçim! Tekrar deneyin (taş/kağıt/makas): ").lower()

    #print ekrana bir mesaj göndermek, input ise kullanıcıdan veri almak için kullanıyorduk.
    print("Bilgisayarın seçimi: ", yapayzeka_secimi)
#şimdi oyuna başlıyoruz.
# yanyana iki eşittir denk demektir. 
# kullanıcı seçimi yapay zeka seçimiyle aynısı olursa berabere olur. İkisi de taş seçerse mesela.
    if oyuncu_secimi == yapayzeka_secimi:
        print("Berabere! Tekrar deneyin.")

    #bir fonksiyon içinde birden fazla eğer ifadesi varsa elif içerisine yazabiliriz. 
    # burada 2 seçeneğimiz var o yüzden birden fazla.
    elif oyuncu_secimi == "taş":
        if yapayzeka_secimi == "kağıt":
            print("Kaybettiniz! Kağıt taşı sarar.")
        else:
            print("Tebrikler! Kazandınız. Taş makası kırar.")

        #kuralları biz belirliyoruz. print ile kullanıcıya gösteriyoruz.
    elif oyuncu_secimi == "kağıt":
        if yapayzeka_secimi == "makas":
            print("Kaybettiniz! Makas Kağıdı keser.")
        else:
            print("Tebrikler! Kazandınız. Kağıt taşı sarar.")

        #4 olasılık var o yüzden 4 adet mesajımız oldu.
    elif oyuncu_secimi == "makas":
        if yapayzeka_secimi == "taş":
            print("Kaybettiniz! Taş makası kırar.")
        else:
            print("Tebrikler! Kazandınız. Makas Kağıdı keser.")
            
#oyuncu eğer e harfine basarsa oyun tekrar oynanır, başka bir harfe basarsa oyun kapanır.
#lower küçük e yazılsa da kabul edileceği anlamına gelir:)
    play_again = input("Tekrar oynamak istiyor musunuz? (E/H) ").lower()
    if play_again != "e":
        break

print("Oyundan çıktınız!")
