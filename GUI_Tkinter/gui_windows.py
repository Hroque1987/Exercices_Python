from tkinter import *


# windgets = GUI elemnts ; buttons, texboxes, labels, images etc
# windows = serves as a cantainer to old or contain these widgets

window = Tk()  # instantiate an instance of a window
window.geometry('420x420')
window.title('Cool window')

icon = PhotoImage(file='C:\\Users\\Helder Roque\\Documents\\GitHub\\Exercices_Python\\GUI_Tkinter\\logo.png')
window.iconphoto(True,icon)
window.config(background='black')


window.mainloop() # place window on computer screen, and listening to events

