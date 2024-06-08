print("Sınav Notu Hesaplama")
isim = input("adınızı girin: ")
okul_no = input("Okul numaranızı girin: ")
ders_adi = input("Ders adını girin: ")
birinci_sinav = int(input("Birinci sınav notunuzu girin: "))
ikinci_sinav = int(input("İkinci sınav notunuzu girin: "))
ortalama = (birinci_sinav + ikinci_sinav) / 2 
if ortalama < 50:
    print(ders_adi, "Dersinden kaldın!")
elif ortalama >= 50:
    print(ders_adi, "Dersini geçtin!")




