from tkinter import *
ventana=Tk()
ventana.title('funciona!!')
texto='Mision Tic 2022'
etiqueta = Label(ventana, text=texto)
etiqueta.config(bg='red', fg='blue', font=('Calibri',33))
etiqueta.pack()
ventana.mainloop()
