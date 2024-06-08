import random as r

rastgelesayi=r.randint(0,20)

print("Tahmin Oyunu'na Hoş Geldiniz!")

while True:
    tahmin=int(input("tahmini bir sayı girin: "))
    print("teşekkürler")
     
    if tahmin == rastgelesayi:
        print("****** Doğru tahmin ******")
        break
    elif tahmin < rastgelesayi:
        print("Daha büyük bir sayı tahmin et")
    elif tahmin> rastgelesayi:
        print("Daha küçük bir sayı tahmin et")
    
    