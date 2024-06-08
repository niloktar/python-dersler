import tkinter as tk

import random

def kontrolEt():
    global sayac
    if tahmin.get().isdigit():
        tahmin1 = int(tahmin.get())
        sayac = sayac + 1
        if tahmin1 > rastgelesayi:
            yazi2.configure(text='Daha az')
        elif tahmin1 < rastgelesayi:
            yazi2.configure(text='Daha fazla')
        else:
            yazi2.configure(text='{} defa da tahmin ettiniz'.format(sayac))
    tahmin.selection_range(0, tk.END)

pencere = tk.Tk()
pencere.title('Tahmin Oyunu')
pencere.geometry('500x200')
pencere.configure(background='red')

yazi1 = tk.Label(pencere,  text='1-10 arasında bir sayı giriniz; ', font='Courier 14 bold', width=40, justify='center', )
yazi1.place(x=40, y=20)
tahmin = tk.Entry(pencere, font='Courier 14 bold', width=20, justify='center')
tahmin.place(x=70, y=50)
tahmin.focus()
tahmin.configure(background='yellow')
kontrol = tk.Button(pencere, text='Tahmin Et', font='Courier 14', width=10, command=kontrolEt)
kontrol.place(x=90, y=80)
yazi2 = tk.Label(pencere, text='', font='Courier 16 bold', width=25, justify='center')
yazi2.place(x=0, y=120)
rastgelesayi = random.randint(1, 10)
sayac = 0

pencere.mainloop()