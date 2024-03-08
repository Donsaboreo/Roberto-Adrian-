import tkinter as tk 
from tkinter import messagebox

def saludo_bienvenida():
    nombre=captura.get()
    if nombre:
        mensaje = "hola,"+nombre+"binvenido de nuevo a programacion"
        messagebox.showinfo("Bienvenido",mensaje)
    else:
        messagebox.showwarning("Error","por favor , ingrese su nombre.")


ventana = tk.Tk()
ventana.title("ventana saludo")
ventana.geometry("400x600")


letra=("Arial",18)
etiqueta= tk.label(ventana,text="ingresa tu nombre")
etiqueta.pack(pady=15)

captura = tk.Entry(ventana)
captura.pack(pady=15)

boton= tk.Button(ventana,text="saludar",command=saludo_bienvenida)
boton.pack(pady=15)


ventana.mainloop()