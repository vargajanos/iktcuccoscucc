from tkinter import *
ablak1 = Tk()
gyoker = 'H:\\ikt\\python\\első\\'
ablak1.geometry('450x450')
ablak1.title('Ikt Tkinter')
icon = PhotoImage(file=gyoker+'kép.png')
ablak1.iconphoto(True, icon)
ablak1.config(background='black')
elsokep= PhotoImage(file=gyoker+"kép3.png")

cimke= Label(ablak1, text='Üdvözlet', fg="white", bg='blue', font=('Comic sans', 45, 'bold'), bd=10, relief=RAISED, padx=25, pady=30, image=elsokep, compound='center')
cimke.pack()


ablak1.mainloop()
