# radio button = simillar to checkbox, but you can only select one from a goup

from tkinter import *

food =['Pizza', 'Hamburguer', 'Hotdog']

window = Tk()
window.geometry('800x300')

pizzaimage = PhotoImage(file='C:\\Users\\Helder Roque\\Documents\\GitHub\\Exercices_Python\\GUI_Tkinter\\pizza.png')
hamburguerimage = PhotoImage(file='C:\\Users\\Helder Roque\\Documents\\GitHub\\Exercices_Python\\GUI_Tkinter\\hamburguer.png')
hotdogimage = PhotoImage(file='C:\\Users\\Helder Roque\\Documents\\GitHub\\Exercices_Python\\GUI_Tkinter\\hotdog.png')
foodimages = ['pizzaimage', 'hamburguerimage', 'hotdogimage']

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index], # ads text to radio buttons
                              variable=x, # groups radio buttons if they share the same value
                              value=index, # assigns each radiobutton a diferent value
                              font=('Arial',20),
                              padx='20',
                              pady='2',
                              bg='#8920d4',
                              relief=RAISED,
                              image=foodimages[index], # adds images to radio button
                              compound='left') 
    
    radiobutton.pack()



window.mainloop()