from tkinter import *


# label = an area widget that holds text anr/or an image within a window

window = Tk()

photo = PhotoImage(file='C:\\Users\\Helder Roque\\Documents\\GitHub\\Exercices_Python\\GUI_Tkinter\\logo.png')

label = Label(window,
              text='Hello world',
              font=('Arial',40,'bold'),
              fg='green',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=10,
              image=photo,
              compound='left')
label.pack()
#abel.place(x=110,y=50)


window.mainloop()