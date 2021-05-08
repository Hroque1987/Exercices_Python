from tkinter import *

def display():
    if(x.get()==1):
        print('You agree')
    else:
        print('You dont agree')



window = Tk()

x = IntVar()

check_button = Checkbutton(window,
                           text='I egree',
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=('Arial',20),
                           fg='#34ebdb',
                           bg='#2f403c',
                           activeforeground='#34ebdb',
                           activebackground='#2f403c',
                           padx='10',
                           pady='10',
                           relief=RAISED,
                           bd='5')

check_button.pack()


window.mainloop()