import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("encuesta")
ventana.geometry("400x400")

def mostrar_mensaje(mensaje):
    messagebox.showinfo("resultado: ",mensaje)

def mostrar_Resultado():
    ciudad=comboCiudades.get()
    mostrar_mensaje(ciudad)
    Resultados()
    generos()
    

def Resultados():
    if chk_hamburguesa.get():
        mostrar_mensaje("si te tusgan las hamburguesas")
    else:
        mostrar_mensaje("no te tusgan las hamburguesas")

def generos():
    generos=grupoSexo.get()
    mostrar_mensaje("genero selecionado: "+generos)

letra= ("Arial",20)
titulo= tk.Label(ventana,text="Encuesta",font=letra)
titulo.pack(pady=10)

ciudad=["veracruz","oxaca","puebla"]
comboCiudades=ttk.Combobox(ventana,values=ciudad)
comboCiudades.set("veracruz")
comboCiudades.pack(pady=10)

chk_hamburguesa=tk.BooleanVar()
checkbox_hamburguesa=tk.Checkbutton(ventana,text="me tusgan las hamburguesas",variable=chk_hamburguesa)
checkbox_hamburguesa.pack(pady=10)

grupoSexo=tk.StringVar()
grupoSexo.set("hombre")
radio_H=tk.Radiobutton(ventana,text="masculino",variable=grupoSexo,value="hombre")
radio_M=tk.Radiobutton(ventana,text="Femenino",variable=grupoSexo,value="Mujer")
radio_H.pack(pady=10)
radio_M.pack(pady=10)


botonR= ttk.Button(ventana,text="Mostrar resultado",command=mostrar_Resultado)
botonR.pack(pady=10)



ventana.mainloop()
