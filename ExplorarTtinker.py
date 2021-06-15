from tkinter import *
from tkinter.ttk import *


ventana=Tk()
ventana.title('funciona!!')

def seleccionar():
    valor=sexo.get()
    if (valor == 1):
        print('Femenino')
    else:
        print('Masculino')

sexo=IntVar()
rdSexo1= Radiobutton(ventana, text='Masculino', variable=sexo, value=0, command=seleccionar)
rdSexo2= Radiobutton(ventana, text='Femenino', variable=sexo, value=1, command=seleccionar)
rdSexo1.pack()
rdSexo2.pack()
ventana.mainloop()