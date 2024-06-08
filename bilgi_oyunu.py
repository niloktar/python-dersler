print("Hello World!")
play = input("Oyuna başlamak için herhangi bir tuşa basın : ")

#oyuna başlangıç sorgusu
if play == "no":
    exit = input("Oyundan çıkmak istediğinize emin misiniz? ")
    if exit == "yes":
        quit()
    

#başlıyor
print("Oyun Başlıyor! :)")
score = 20

#1.soru
cevap = input("Bu program hangi yazılım dil ile yazıldı? : ")
if cevap.lower() =="python":
    print("Doğru Cevap :)")
    score += 10
else:
    score -= 5
    print("Yanlış Cevap :(")
    
#2.soru
cevap = input("Python yazı değişkenine ne denir? : ")
if cevap.lower() =="string":
    print("Doğru Cevap :)")
    score += 10
else:
    score -= 5
    print("Yanlış Cevap :(")
#3.soru
cevap = input("onbes ile str(15) toplamı kaçtır? : ")
if cevap.lower() =="onbes15":
    print("Doğru Cevap :)")
    score += 10
else:
    score -= 5
    print("Yanlış Cevap :(")
    
#4.soru
cevap = input("değişken hangi sembol ile atanır? : ")
if cevap.lower() =="esittir":
    print("Doğru Cevap :)")
    score += 10
else:
    score -= 5
    print("Yanlış Cevap :(")
    
print("Oyunu tamamladın!")
print ("Tebrikler!"  + " " + "Oyun sonucundaki Skor" + " " + str(score))



