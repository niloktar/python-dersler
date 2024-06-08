print("Bilgi Oyununa Hoş Geldiniz!")

playing = input("Başlayalım mı? ")
if playing.lower() != "evet":
    quit()

print("Hadi oynayalım! :)")
score = 0
puan = 100

answer = input("Bu program hangi yazılım dil ile yazıldı? : ")
if answer.lower() == "python":
    print('Doğru!')
    score += 1
    puan -= 10
else:
    print("Yanlış!:(")

answer = input("Python yazı değişkenine ne denir? : ")
if answer.lower() == "string":
    print('Doğru!')
    score += 1
else:
    print("Yanlış!:(")

answer = input("onbes ile str(15) toplamı kaçtır? : ")
if answer.lower() == "onbes15":
    print('Doğru!')
    score += 1
else:
    print("Yanlış!:(")

answer = input("değişken hangi sembol ile atanır? : ")
if answer.lower() == "esittir":
    print('Doğru!')
    score += 1
else:
    print("Yanlış!:(")

print(str(score) + " Soruyu doğru bildin, Tebrikler!")
print("Skor Yüzde " + str((score / 4) * 100) + "%.")
