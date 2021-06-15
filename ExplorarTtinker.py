from tkinter import *
from tkinter.ttk import *


ventana=Tk()
ventana.title('funciona!!')

combo=Combobox(ventana)
combo['values']=('HOMBRE', 'MUJER', 'Texto',9.8)
combo.current(0)
combo.grid(column=0, row=0)
combo.pack()

def accion():
    if combo.current() == 0:
        combo.current(1)
    if combo.current() == 1:
        boton=Button(ventana, text='Siii', command=accion2)
        boton.pack()

def accion2():
    print('Funciona mi pes')

boton=Button(ventana, text='Mostar', command=accion)
boton.pack()

ventana.mainloop()