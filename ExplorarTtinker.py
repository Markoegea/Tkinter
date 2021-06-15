from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext

ventana=Tk()
ventana.title('funciona!!')

textolargo=scrolledtext.ScrolledText(ventana, width=20, height=10)
textolargo.grid(column=3, row=0)
ventana.mainloop()