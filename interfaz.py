import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
import os, sys
import main


def clear():
    for i in tabla.get_children():
        tabla.delete(i)

def antr():
    clear()
    if variable.get()=='2':
        matriz = [a2.get(),a1.get(),b.get()]
        print(matriz)
        x=main.resolver(matriz,2,xi.get())
    if variable.get()=='3':
        matriz = [a3.get(),a2.get(),a1.get(),b.get()]
        print(matriz)
        x=main.resolver(matriz,3,xi.get())
    if variable.get()=='4':
        matriz = [a4.get(),a3.get(),a2.get(),a1.get(),b.get()]
        print(matriz)
        x=main.resolver(matriz, 4,xi.get())
    if variable.get()=='5':
        matriz = [a5.get(),a4.get(),a3.get(),a2.get(),a1.get(),b.get()]
        print(matriz)
        x=main.resolver(matriz, 5,xi.get())

    for i in range(0,len(x)):
        tabla.insert("",END,text=x[i][0],values=(x[i][1],x[i][2]))

#Creamos la ventana

root = tk.Tk() #creamos la ventana
root.title("Analisis Numerico")
root.resizable(0,0)
root.geometry("700x500+500+100")

#variable de entrada
a1 = tk.DoubleVar()
a2 = tk.DoubleVar()
a3 = tk.DoubleVar()
a4 = tk.DoubleVar()
b = tk.DoubleVar()
a5 = tk.DoubleVar()
xi= tk.DoubleVar()
def callback(*args):
    if variable.get()=='4':
        etiquetax3.place(x=190,y=100)
        entradax3.place(x=140, y=100)
        etiquetax.place(x=370,y=100)
        entradax.place(x=320, y=100)
        etiquetax2.place(x=280,y=100)
        entradax2.place(x=230,y=100)
        entradab.place(x=410,y=100)
        etiquetax4.place(x=100, y=100)
        entradax4.place(x=50, y=100)
        etiquetax5.place_forget()
        entradax5.place_forget()
    if variable.get()=='5':
        etiquetax4.place(x=190, y=100)
        entradax4.place(x=140, y=100)
        etiquetax2.place(x=370, y=100)
        entradax2.place(x=320, y=100)
        etiquetax3.place(x=280, y=100)
        entradax3.place(x=230, y=100)
        etiquetax.place(x=460, y=100)
        entradax.place(x=410, y=100)
        entradab.place(x=500, y=100)
        etiquetax5.place(x=100, y=100)
        entradax5.place(x=50, y=100)
    if variable.get()=='3':
        etiquetax3.place(x=100, y=100)
        entradax3.place(x=50, y=100)
        etiquetax.place(x=280, y=100)
        etiquetax2.place(x=190,y=100)
        entradax2.place(x=140, y=100)
        entradax.place(x=230, y=100)
        entradab.place(x=320, y=100)
        entradax4.place_forget()
        etiquetax4.place_forget()
        etiquetax5.place_forget()
        entradax5.place_forget()
    if variable.get()=='2':
        etiquetax3.place_forget()
        entradax3.place_forget()
        etiquetax.place(x=220, y=100)
        etiquetax2.place(x=130,y=100)
        entradax2.place(x=80, y=100)
        entradax.place(x=170, y=100)
        entradab.place(x=260, y=100)
        entradax4.place_forget()
        entradax3.place_forget()
        etiquetax4.place_forget()
        etiquetax5.place_forget()
        entradax5.place_forget()

grados=['2','3','4','5']

variable = tk.StringVar(root)
variable.set(grados[0])

tabla = ttk.Treeview(root, columns=("1","2"))
tabla.heading("#0",text="Iteracion")
tabla.heading("1",text="Xi")
tabla.heading("2",text="Ea")


etiqueta1 = tk.Label(text="Newton-Raphson mejorado", font=("Arial", 20))
etiqueta1.place(x=80,y=10)
etiqueta2 = tk.Label(text="F(x)=", font=("Arial", 15))
etiqueta2.place(x=5,y=100)
etiquetax3 = tk.Label(text="x\u00B3 +", font=("Arial", 15))
entradax3 = tk.Entry(width=4,textvariable=a3,font=("Arial", 14))
etiquetax2 = tk.Label(text="x\u00B2 +", font=("Arial", 15))
entradax2 = tk.Entry(width=4,textvariable=a2,font=("Arial", 14))
etiquetax = tk.Label(text="x +", font=("Arial", 15))
entradax = tk.Entry(width=4,textvariable=a1,font=("Arial", 14))
entradab = tk.Entry(width=4,textvariable=b,font=("Arial", 14))


etiquetax5 = tk.Label(text="x\u2075 +", font=("Arial", 15))
entradax5 = tk.Entry(width=4,textvariable=a4,font=("Arial", 14))
etiquetax4 = tk.Label(text="x\u2074 +", font=("Arial", 15))
entradax4 = tk.Entry(width=4,textvariable=a4,font=("Arial", 14))

etiquetax.place(x=220, y=100)
etiquetax2.place(x=130, y=100)
entradax2.place(x=80, y=100)
entradax.place(x=170, y=100)
entradab.place(x=260, y=100)

etiquetaxi= tk.Label(text="x\u2080 =", font=("Arial", 15))
etiquetaxi.place(x=140,y=150)
entradaxi = tk.Entry(width=4,textvariable=xi,font=("Arial", 14))
entradaxi.place(x=190,y=150)


opcion=tk.OptionMenu(root,variable,*grados)
opcion.config(width=2, font=('Helvetica', 12))
opcion.pack()
opcion.place(x=320,y=70)

etiqueta3 = tk.Label(text="Grados del polinomio:", font=("Arial", 12))
etiqueta3.place(x=100,y=70)
variable.trace("w", callback)



boton1 = tk.Button(text="Resolver",command=antr)
boton1.place(x=280,y=130)

tabla.place(x=10,y =200)

root.mainloop()