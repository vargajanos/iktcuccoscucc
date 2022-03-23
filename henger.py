from tkinter import *
import math
foablak=Tk()

def térfogat():
    a=float(mezo1.get())
    b=float(mezo2.get())
    V = a**2 * b * math.pi
    mezo3.delete(0, END)
    mezo3.insert(0,''+str("%.2f" % V)+' cm3' )

def tomeg():
    p=7.8
    a=float(mezo1.get())
    b=float(mezo2.get())   
    V = a**2 * b * math.pi
    m = p * V    
    mezo4.delete(0, END)
    mezo4.insert(0,''+str("%.2f" % m)+' g')

def tomeg2():
    d=0.7
    a=float(mezo1.get())
    b=float(mezo2.get())   
    V = a**2 * b * math.pi
    m = d * V    
    mezo5.delete(0, END)
    mezo5.insert(0,''+str("%.2f" % m)+' g' )

cimke=Label(foablak, text='Sugár (cm):', fg='black',)
cimke.grid(row=0, column=0)
cimke2=Label(foablak, text='Magasság (cm):', fg='black')
cimke2.grid(row=1, column=0)
mezo1=Entry(foablak)
mezo1.grid(row=0, column=1)
mezo2=Entry(foablak)
mezo2.grid(row=1, column=1)
gomb4=Button(foablak, text='Kiszámít', command=lambda:[térfogat(), tomeg(), tomeg2()]) 
gomb4.grid(row=2, column=2)
cimke3=Label(foablak, text='Térfogat:', fg='black',)
cimke3.grid(row=3, column=0)
cimke4=Label(foablak, text='Vashenger:', fg='black')
cimke4.grid(row=4, column=0)
cimke5=Label(foablak, text='Fahenger:', fg='black',)
cimke5.grid(row=5, column=0)
mezo3=Entry(foablak)
mezo3.grid(row=3, column=1)
mezo4=Entry(foablak)
mezo4.grid(row=4, column=1)
mezo5=Entry(foablak)
mezo5.grid(row=5, column=1)




foablak.mainloop()