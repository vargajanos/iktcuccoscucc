from tkinter import *
def klikk():
    print("Klikkeltem")
ablak1 = Tk()
gyoker = 'H:\\ikt\\python\\első\\'
ablak1.geometry('450x450')
ablak1.title('Ikt Tkinter')
icon = PhotoImage(file=gyoker+'kép.png')
ablak1.iconphoto(True, icon)
ablak1.config(background='black')
elsokep= PhotoImage(file=gyoker+"kép3.png")
gombkep= PhotoImage(file=gyoker+"kép.png")

cimke= Label(ablak1, 
            text='Üdvözlet', 
            fg="white", 
            bg='blue', 
            font=('Comic sans', 45, 'bold'), 
            bd=10, 
            relief=RAISED, 
            padx=25, 
            pady=30, 
            image=elsokep, 
            compound='center')
cimke.pack()

gomb= Button(ablak1, 
            text="Kattints!", 
            fg="blue", 
            font=('Comis Sans', 35, 'bold'), 
            bg='yellow', 
            relief=SUNKEN, 
            bd=10, 
            command=klikk, 
            padx=12,
            pady=12, 
            #image=gombkep, 
            compound="bottom", 
            activebackground='blue', 
            activeforeground='yellow',
            state=ACTIVE).pack()


ablak1.mainloop()
