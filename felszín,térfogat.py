from tkinter import *

abl1=Tk()
abl1.title("Téglatest adatok")
abl1.minsize(width=254, height=100)

def ujablak():
    abl2=Toplevel(abl1)
    abl2.title("Eredmények")
    abl2.minsize(width=254, height=100)

    sz1=Label(abl2, text="Felszín")
    sz2=Label(abl2,text="Térfogat")
    m1=Entry(abl2)
    m2=Entry(abl2)


    sz1.grid(row=1)
    sz2.grid(row=2)
    m1.grid(row=1, column=2)
    m2.grid(row=2, column=2)

    a=eval(mezo1.get())
    b=eval(mezo2.get())
    c=eval(mezo3.get())

    felszin= 2*(a*b+a*c+b*c) 
    terfogat= a*b*c

    m1.delete(0,END)
    m1.insert(0,str(felszin))
    m2.delete(0,END)
    m2.insert(0,str(terfogat))

    gomb4=Button(abl2,text="Kilép", command=abl2.destroy)
    gomb4.grid()
    abl2.mainloop()

szoveg1= Label(abl1,text='a')
szoveg2= Label(abl1,text='b')
szoveg3= Label(abl1,text='c')
gomb1=Button(abl1,text='Számítás', command=ujablak)
mezo1=Entry(abl1)
mezo2=Entry(abl1)
mezo3=Entry(abl1)

szoveg1.grid(row=1)
szoveg2.grid(row=2)
szoveg3.grid(row=3)
gomb1.grid(row=4, column=2)
mezo1.grid(row=1, column=2)
mezo2.grid(row=2, column=2)
mezo3.grid(row=3, column=2)

abl1.mainloop()
