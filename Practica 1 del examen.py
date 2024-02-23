import tkinter as tk
from tkinter import messagebox

def verificar_edad():
    
        edad = int(entry_edad.get())
        if edad >= 18:
            messagebox.showinfo("Resultado", "La persona es mayor de edad.")
        else:
            messagebox.showinfo("Resultado", "La persona no es mayor de edad.")
  

root = tk.Tk()
root.title("Verificador de Edad")


label_edad = tk.Label(root, text="Ingrese la edad:")
label_edad.pack()
entry_edad = tk.Entry(root)
entry_edad.pack()


boton_verificar = tk.Button(root, text="Verificar Edad", command=verificar_edad)
boton_verificar.pack()

ventana.mainloop()
