print("Bir bilinmeyenli denklem çözme oyunu")
toplam = int(input("Toplam değerini gir: "))
a = float(input("a değerini gir: "))

def cikarma(toplam, a):
    return toplam - a

ilk_deger = cikarma(toplam, a)

deger = float(input("Değerin kaça bölündüğünü yazarak değeri bul: "))

def bolme(ilk_deger, deger):
    return ilk_deger / deger

print("Değeriniz: ", bolme(ilk_deger, deger))

