import random as r

rastgelesayi = r.randint(0, 20)

print("Tahmin Oyunu'na Hoş Geldiniz!")

hak = 3

while hak > 0:
    tahmin = int(input("Tahmini bir sayı girin: "))

    if tahmin == rastgelesayi:
        print("Teşekkürler")
        print("****** Doğru tahmin ******")
        break
    elif tahmin < rastgelesayi:
        print("Tekrar dene")
        print("Daha büyük bir sayı tahmin et")
    elif tahmin > rastgelesayi:
        print("Tekrar dene")
        print("Daha küçük bir sayı tahmin et")
    hak -= 1

else:
    print("Hakkınız bitti! Doğru sayı", rastgelesayi, "idi.")