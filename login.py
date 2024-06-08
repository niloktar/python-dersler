import tkinter as tk
from tkinter import messagebox

# Kayıt bilgilerini gösteren fonksiyon
def show_info():
    name = name_entry.get()
    kullaniciadi = kullaniciadi_entry.get()
    mail = mail_entry.get()
    parola = parola_entry.get()
    parola2 = parola2_entry.get()
    takim = takim_entry.get()
    
    info = f"Ad: {name}\nKullanıcı adınız: {kullaniciadi}\nMail adresiniz: {mail}\n Parolanız: {parola}\n Tuttuğunuz takım: {takim}"
    messagebox.showinfo("Kaydınız gerçekleşti", info)   

# Ana pencereyi oluşturma
root = tk.Tk()
root.title("Kayıt Formu")

# Etiketler ve Giriş Kutuları
tk.Label(root, text="Adınızı girin:").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Kullanıcı adınızı girin:").grid(row=1, column=0, padx=10, pady=5)
kullaniciadi_entry = tk.Entry(root)
kullaniciadi_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Mail adresinizi girin:").grid(row=2, column=0, padx=10, pady=5)
mail_entry = tk.Entry(root)
mail_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Parola oluşturun:").grid(row=3, column=0, padx=10, pady=5)
parola_entry = tk.Entry(root)
parola_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Tekrar girin:").grid(row=4, column=0, padx=10, pady=5)
parola2_entry = tk.Entry(root)
parola2_entry.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Tuttuğunuz takım:").grid(row=5, column=0, padx=10, pady=5)
takim_entry = tk.Entry(root)
takim_entry.grid(row=5, column=1, padx=10, pady=5)

# Kayıt ol butonu
register_button = tk.Button(root, text="Kayıt Ol", command=show_info)
register_button.grid(row=6, column=0, columnspan=2, pady=10)

# Ana döngüyü başlatma
root.mainloop()
