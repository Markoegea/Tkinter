from tkinter import *
ventana=Tk()
ventana.title('funciona!!')

def accion():
    print('Sii, Funciona!!')

boton=Button(ventana, text='Mostar',command=accion)
boton.pack()
ventana.mainloop()