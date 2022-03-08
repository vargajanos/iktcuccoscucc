from tkinter import *
import math
def osszeg():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = a + b
    mezo3.delete(0, END)
    mezo3.insert(0, 'Összeg: '+str(c))
def szorzás():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = a * b
    mezo3.delete(0, END)
    mezo3.insert(0, 'Összeg: '+str(c))
def osztás():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = (a / b) if b !=0 else 'Nem lehet nullával osztani'
    mezo3.delete(0, END)
    mezo3.insert(0, 'Összeg: '+str(c))
def kivonás():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = a - b
    mezo3.delete(0, END)
    mezo3.insert(0, 'Összeg: '+str(c))
def gyökvonás():
    a = int(mezo1.get())
    c = math.sqrt(a) if a > 0 else 'Nem értelmezhető'
    mezo3.delete(0, END)
    mezo3.insert(0, 'Összeg: '+str(c))
def hatványozás():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = a ** a
    mezo3.delete(0, END)
    mezo3.insert(0, 'Összeg: '+str(c))
    
foablak=Tk()
cimke=Label(foablak, text='Első szám:', fg='red',)
cimke.grid(row=0, column=0)
cimke=Label(foablak, text='Második szám:', fg='red')
cimke.grid(row=1, column=0)
mezo1=Entry(foablak)
mezo1.grid(row=0, column=1)
mezo2=Entry(foablak)
mezo2.grid(row=1, column=1)
mezo3=Entry(foablak, width=32)
mezo3.grid(row=3, column=0,)
gomb4=Button(foablak, text='Összead', command=osszeg)
gomb4.grid()
gomb5=Button(foablak, text='Szorzás', command=szorzás)
gomb5.grid()
gomb6=Button(foablak, text='Osztás', command=osztás)
gomb6.grid()
gomb7=Button(foablak, text='Kivonás', command=kivonás)
gomb7.grid()
gomb8=Button(foablak, text='Hatványozás', command=hatványozás)
gomb8.grid()
gomb9=Button(foablak, text='Gyökvonás', command=gyökvonás)
gomb9.grid()
gomb3=Button(foablak, text='Kilépés', command=foablak.destroy)
gomb3.grid(row=11, column=1)


can1 = Canvas(foablak, width=460, height=460, bg='white')
photo= PhotoImage(file='giphy.gif')
item = can1.create_image(170,150, image =photo)
can1.grid()


foablak.mainloop()