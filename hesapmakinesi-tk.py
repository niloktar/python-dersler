import tkinter as tk

font_size = 17
window_width = 250
window_height = 250

def toplama():
    try:
        sayi1 = float(entry_sayi1.get())
        sayi2 = float(entry_sayi2.get())
        sonuc = sayi1 + sayi2
        label_sonuc["text"] = "Sonuç: " + str(sonuc)
    except ValueError:
        label_sonuc["text"] = "Hatalı giriş!"

def cikarma():
    try:
        sayi1 = float(entry_sayi1.get())
        sayi2 = float(entry_sayi2.get())
        sonuc = sayi1 - sayi2
        label_sonuc["text"] = "Sonuç: " + str(sonuc)
    except ValueError:
        label_sonuc["text"] = "Hatalı giriş!"

def carpma():
    try:
        sayi1 = float(entry_sayi1.get())
        sayi2 = float(entry_sayi2.get())
        sonuc = sayi1 * sayi2
        label_sonuc["text"] = "Sonuç: " + str(sonuc)
    except ValueError:
        label_sonuc["text"] = "Hatalı giriş!"

def bolme():
    try:
        sayi1 = float(entry_sayi1.get())
        sayi2 = float(entry_sayi2.get())
        if sayi2 == 0:
            label_sonuc["text"] = "Sıfıra bölme hatası!"
        else:
            sonuc = sayi1 / sayi2
            label_sonuc["text"] = "Sonuç: " + str(sonuc)
    except ValueError:
        label_sonuc["text"] = "Hatalı giriş!"

app = tk.Tk()
app.title("Hesap Makinesi")
app.geometry(f"{window_width}x{window_height}")

label_sayi1 = tk.Label(app, text="Birinci Sayı:", font=("Arial", 17))
label_sayi1.grid(row=0, column=0)

entry_sayi1 = tk.Entry(app)
entry_sayi1.grid(row=0, column=1)

label_sayi2 = tk.Label(app, text="İkinci Sayı:", font=("Arial", 17))
label_sayi2.grid(row=1, column=0)

entry_sayi2 = tk.Entry(app)
entry_sayi2.grid(row=1, column=1)

button_toplama = tk.Button(app, text="Toplama", command=toplama, font=("Arial", 17))
button_toplama.grid(row=2, column=0)

button_cikarma = tk.Button(app, text="Çıkarma", command=cikarma, font=("Arial", 17))
button_cikarma.grid(row=2, column=1)

button_carpma = tk.Button(app, text="Çarpma", command=carpma, font=("Arial", 17))
button_carpma.grid(row=3, column=0)

button_bolme = tk.Button(app, text="Bölme", command=bolme, font=("Arial", 17))
button_bolme.grid(row=3, column=1)

frame_sonuc = tk.Frame(app)
frame_sonuc.grid(row=4, columnspan=2, pady=10)

label_sonuc = tk.Label(frame_sonuc, text="", font=("Arial", 18))
label_sonuc.pack()

app.mainloop()