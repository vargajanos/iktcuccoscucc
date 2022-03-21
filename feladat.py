from tkinter import *
foablak=Tk()
gyoker = 'H:\\ikt\\python\\első\\'
icon = PhotoImage(file=gyoker+'kép.png')
foablak.iconphoto(True, icon)
cimke1=Label(foablak, text='Első mező:', fg='red', compound="top", pady=10)
cimke1.grid(row=0, column=0)
mezo1=Entry(foablak)
mezo1.grid(row=0, column=1)
cimke2=Label(foablak, text='Második:', fg='red',compound="center")
cimke2.grid(row=1, column=0)
mezo2=Entry(foablak)
mezo2.grid(row=1, column=1)
cimke3=Label(foablak, text='Harmadik:', fg='red', compound="bottom")
cimke3.grid(row=2, column=0)
mezo3=Entry(foablak)
mezo3.grid(row=2, column=1)

can1 = Canvas(foablak, width=160, height=160, bg='white',)
photo= PhotoImage(file='kép3.png',)
item = can1.create_image(40,70, image =photo)
can1.grid(columnspan=1, rowspan=3, column=3, row=0, padx=15)

foablak.mainloop()