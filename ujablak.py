from tkinter import *

abl1=Tk()

def ujablak():
    abl2= Toplevel(abl1)
    uz2= Message(abl2, text='Készítette: Gipsz Jakab\nPiripócs\n2009.06.04', width=300)
    gomb2= Button(abl2,text="Kilép", command=abl2.destroy)
    uz2.pack()
    gomb2.pack()
    abl2.mainloop()

szoveg1=Label(abl1, text="Kattints a gombra!")
gomb1=Button(abl1,text='Névjegy', command=ujablak)

szoveg1.pack()
gomb1.pack()

abl1.mainloop()

