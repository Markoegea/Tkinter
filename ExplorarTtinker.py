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

boton=Button(ventana, text='Mostar',command=accion)
boton.pack()
ventana.mainloop()