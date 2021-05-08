from tkinter import *

window = Tk()

photo = PhotoImage(file='C:\\Users\\Helder Roque\\Documents\\GitHub\\Exercices_Python\\GUI_Tkinter\\logo.png')
count = 0
def click():
    global count
    print('You clicked the button!')
    count += 1
    print(count)
button = Button(window,
                text='click me',
                command=click,
                font=('Comic Sans',30),
                fg='green',
                bg='black',
                activeforeground='red',
                activebackground='blue',
                image=photo,
                compound='top',
                )
button.pack()

window.mainloop()