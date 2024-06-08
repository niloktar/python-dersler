# ad = "Bera" #string
# sayi1=5 #integer
# sayi2=8.5 #float
# toplam=sayi1+sayi2
# print(toplam)
# print(ad)

# kullaniciadi = input("Kullanıcı adınızı giriniz: ")
# parola = input("Parolanızı giriniz: ")
# print("Kullanıcı Adınız:" , kullaniciadi)
# print("parolanız: ", parola)

# ad = (input("adınızı giriniz: "))
# soyad = (input("soyadınızı giriniz: "))
# toplam = ad + soyad
# print("girdiğiniz sayıların toplamı: ", toplam)

# list= [ad,soyad]
# print(list)

# sayi1 = int(input("bir sayı giriniz: "))
# sayi2 = int(input("bir sayı giriniz: "))
# toplam = sayi1 + sayi2
# print("girdiğiniz sayıların toplamı: ", sayi1 + sayi2)

# sayi1 = int(input("bir sayı giriniz: "))
# sayi2 = int(input(" bir sayı giriniz: "))
# carpim =sayi1 * sayi2
# print("girdiğiniz sayıların carpimi: ", carpim)

# list = [kullaniciadi, parola]
# print(list)

# list = [sayi1,sayi2]
# print(list)

meyve1 = input("sevdiğiniz bir meyve: ")
meyve2 = input("sevdiğiniz bir meyve: ")
meyve3 = input("sevdiğiniz bir meyve: ")
list = [meyve1, meyve2, meyve3]
print("sevdiğiniz meyveler: " , list)
print("listeye öge ekleme")
list.append("kiraz")
print(list)
print("belirli bir sıraya eklemek için")
list.insert(1,"armut")
print(list)
print("listeden öğe çıkarmak")
list.remove(meyve1)
print(list)
list.pop(1)
print(list)
print("Alfabeye göre sıralama")
list.sort()
print(list)