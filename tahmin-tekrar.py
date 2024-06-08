import random as r

rastgelesayi = r.randint(0, 20)

print("Tahmin Oyunu'na Hoş Geldiniz!")

hak = 3
tahminler = []

while hak > 0:
    tahmin = int(input("Tahmini bir sayı girin: "))

    if tahmin in tahminler:
        print("Daha önce bu sayıyı denediniz! Farklı bir sayı girin.")
        continue

    tahminler.append(tahmin)

    if tahmin == rastgelesayi:
        print("****** Doğru tahmin ******")
        print("Teşekkürler")
        break
    elif tahmin < rastgelesayi:
        print("Tekrar Dene")
        print("Daha büyük bir sayı tahmin et")
    elif tahmin > rastgelesayi:
        print("Tekrar Dene")
        print("Daha küçük bir sayı tahmin et")
    hak -= 1
    
else:
    print("Hakkınız bitti! Doğru sayı", rastgelesayi, "idi.")
    print(tahminler)