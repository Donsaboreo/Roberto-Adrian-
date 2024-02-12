import tkinter as tk 
from tkinter import messagebox

def saludo_bienvenido():
    nombre=captura.get()
    if nombre:
        mensaje = "Hola ,"+nombre+" bienvenido de nuevo a programacion!"
        messagebox.showinfo("Bienvenido",mensaje)
    else:
        messagebox.showwarning("Error","Por favor , ingrese su nombre.")

ventana = tk.Tk()
ventana.title("Ventana Saludo")#title es para el titulo de la ventana
ventana.geometry("400x600")

#Fuente
letra=("Arial,18")
etiqueta = tk.Label(ventana,text = "Ingreses tu nombre : ",font=letra)
etiqueta.pack(pady=15)#pady me sirve para distanciar mis objetos 

captura = tk.Entry(ventana)
captura.pack(pady=15)

boton = tk.Button(ventana,text="Saludos",command=saludo_bienvenido)
boton.pack(pady=15)

ventana.mainloop()


