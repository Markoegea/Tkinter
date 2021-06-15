from tkinter import *
from tkinter.ttk import *


ventana=Tk()
ventana.title('funciona!!')

def verificar():
    valor=checkeo.get()
    if (valor == 1):
        print('Ciclismo Seleccionado')
    else:
        print('Ciclismo no seleccionado')

checkeo=IntVar()
chkHobbie1= Checkbutton(ventana, text='Ciclismo', variable=checkeo, onvalue=1, offvalue=0, command=verificar)
chkHobbie1.pack()

ventana.mainloop()