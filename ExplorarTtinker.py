from tkinter import *
from tkinter.ttk import *
ventana=Tk()
ventana.title('funciona!!')
combo=Combobox(ventana)
combo['values']=(1,2,3,4,5, 'Texto',9.8)
combo.current(0)
combo.grid(column=0, row=0)
combo.pack()
ventana.mainloop()