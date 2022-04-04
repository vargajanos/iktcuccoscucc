from tkinter import *
from tkinter import messagebox
foablak=Tk()
import math

def terfogat():
    var=mezo1.get()
    if len(var) == 0:
        messagebox.showerror('Error', 'A mező üres')
    else:
        pass
    var = int(var)
    var=mezo2.get()
    if len(var) == 0:
        messagebox.showerror('Error', 'A mező üres')
    else:
        pass
    var = int(var)
    var=mezo4.get()
    if len(var) == 0:
        messagebox.showerror('Error', 'A mező üres')
    else:
        pass

    var = int(var)
            
    r = int(mezo1.get())
    m = int(mezo2.get())
    borocska= int(mezo4.get())

    if r>0 and m>0 and borocska>0:
        terfogat = round(math.pi * r * r * m)
        liter=round(0.001*terfogat)
        mezo3.delete(0, END)
        mezo3.insert(0, str(liter)+' l')
        telitett=0
        telitett=round(borocska*(100/liter), 2)
        if borocska<=liter:
            mezo3.delete(0, END)
            mezo3.insert(0, str(liter)+' l')
            mezo5.delete(0, END)
            mezo5.insert(0, str(liter-borocska)+' l')
            mezo6.delete(0, END)
            mezo6.insert(0, str(telitett)+" %")      
        else:
            mezo3.delete(0, END)
            mezo3.insert(0, 'A hordó túl kicsi')
            mezo6.delete(0, END)
            mezo6.insert(0, 'A hordó túl kicsi')

    else:
        mezo3.delete(0, END)
        mezo3.insert(0, "Nem értelmezhető")        
        mezo5.delete(0, END)
        mezo5.insert(0, "Nem értelmezhető")
        mezo6.delete(0, END)
        mezo6.insert(0, "Nem értelmezhető")


cimke4=Label(foablak, text="Hány liter bor (l):")
cimke4.grid(row=1, column=1, sticky="e")
mezo4=Entry(foablak)
mezo4.grid(row=1, column=2, columnspan=4)

cimke1=Label(foablak, text="Sugár (cm):")
cimke1.grid(row=2, column=1, sticky="e")
mezo1=Entry(foablak)
mezo1.grid(row=2, column=2, columnspan=4)

cimke2=Label(foablak, text="Magasság (cm):")
cimke2.grid(row=3, column=1, sticky="e")
mezo2=Entry(foablak)
mezo2.grid(row=3, column=2, columnspan=4)

can1 = Canvas(foablak, width=250, height=200)
photo= PhotoImage(file='hordo.png')
item = can1.create_image(100,100, image =photo)
can1.grid(column=3)

gomb1=Button(foablak, text="Kiszámít", command=lambda:[terfogat()]) 
gomb1.grid(row=4, column=2, sticky="w")

cimke3=Label(foablak, text="A hordó ennyi literes:")
cimke3.grid(row=5, column=1, sticky="e")
mezo3=Entry(foablak)
mezo3.grid(row=5, column=2, columnspan=4)

cimke5=Label(foablak, text="A hordóba ennyi liter fér még:")
cimke5.grid(row=6, column=1, sticky="e")
mezo5=Entry(foablak)
mezo5.grid(row=6, column=2, columnspan=4)

cimke6=Label(foablak, text="Telítetség:")
cimke6.grid(row=7, column=1, sticky="e")
mezo6=Entry(foablak)
mezo6.grid(row=7, column=2, columnspan=4)



foablak.mainloop()