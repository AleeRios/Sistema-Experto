#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 02:17:34 2022

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: Sistemas Expertos
Alumnos: Rios Campusano Beckham Alejandro
         Garduño Sanchez Bladimir Axley
Profesor: M. en C. Edith Cristina Herrera Luna
Descripción: Interfaz grafica para nuestra Sistema Experto
    
@author: alebe
"""

import tkinter as tk
from PIL import ImageTk
from Conocimiento import Turismo
from experta import *

def recomendarZona():
    sistemaExperto = Turismo()
    sistemaExperto.reset()
    
    sistemaExperto.declare(Fact(frio = str(tkFrio.get())))
    sistemaExperto.declare(Fact(calor = str(tkCaliente.get())))
    sistemaExperto.declare(Fact(naturaleza = str(tkNaturaleza.get())))
    sistemaExperto.declare(Fact(pueblo = str(tkPueblo.get())))
    sistemaExperto.declare(Fact(aventura = str(tkAventura.get())))
    sistemaExperto.declare(Fact(arqueologia = str(tkArqueologia.get())))
    sistemaExperto.declare(Fact(religioso = str(tkReligioso.get())))
    
    sistemaExperto.run()
    
    destino.config(state=tk.NORMAL)
    lugares.config(state=tk.NORMAL)
    descripcion.config(state=tk.NORMAL)
    
    destino.delete("1.0", "end")
    destino.insert(tk.INSERT, sistemaExperto.destino)
    lugares.delete("1.0", "end")
    lugares.insert(tk.INSERT, sistemaExperto.lugares)
    descripcion.delete("1.0", "end")
    descripcion.insert(tk.INSERT, sistemaExperto.descripcion)
    
def limpiar():
    destino.config(state=tk.NORMAL)
    lugares.config(state=tk.NORMAL)
    descripcion.config(state=tk.NORMAL)

    destino.delete("1.0", "end")
    lugares.delete("1.0", "end")
    descripcion.delete("1.0", "end")
    
    destino.config(state=tk.DISABLED)
    lugares.config(state=tk.DISABLED)
    descripcion.config(state=tk.DISABLED)
    
    tkFrio.set(False)
    tkCaliente.set(False)
    tkNaturaleza.set(False)
    tkPueblo.set(False)
    tkAventura.set(False)
    tkArqueologia.set(False)
    tkReligioso.set(False)
    
raiz = tk.Tk()
raiz.title("Formulario de Turistas")
raiz.geometry("+350+200")
raiz.config(bg="floral white")

tkFrio = tk.BooleanVar()
tkCaliente = tk.BooleanVar()
tkNaturaleza = tk.BooleanVar()
tkPueblo = tk.BooleanVar()
tkAventura = tk.BooleanVar()
tkArqueologia = tk.BooleanVar()
tkReligioso = tk.BooleanVar()

lb1 = tk.Label(raiz, text="Seleccione el clima que prefiere: ", width=30, bg="sky blue")
lb1.grid(row=0, column=1, pady=10)
#imgFrio = ImageTk.PhotoImage(file="C:/Users/alebe/OneDrive - Universidad Autónoma del Estado de México/Documents/Python Scripts/Sistemas Expertos/SE_Turismo/Imagenes/frio.jpg")
c1 = tk.Checkbutton(raiz, text="Frio", variable=tkFrio, width=10, height=2, compound="top", bg="cyan", fg="black")
c1.grid(row=1, column=0, pady=5)
#imgCaliente = ImageTk.PhotoImage(file="C:/Users/alebe/OneDrive - Universidad Autónoma del Estado de México/Documents/Python Scripts/Sistemas Expertos/SE_Turismo/Imagenes/caliente.jpg")
c2 = tk.Checkbutton(raiz, text="Caliente", variable=tkCaliente, width=10, height=2, compound="top", bg="red", fg="black")
c2.grid(row=1, column=2, pady=5)

lb2 = tk.Label(raiz, text="Seleccione el lugar que prefiere: ", width=30, bg="sky blue")
lb2.grid(row=2, column=1, pady=10)
#imgNaturaleza = ImageTk.PhotoImage(file="C:/Users/alebe/OneDrive - Universidad Autónoma del Estado de México/Documents/Python Scripts/Sistemas Expertos/SE_Turismo/Imagenes/Naturaleza.jpg")
c3 = tk.Checkbutton(raiz, text="Naturaleza", variable=tkNaturaleza, width=10, height=2, compound="top", bg="green2", fg="black")
c3.grid(row=3, column=0, pady=5)
#imgPueblo = ImageTk.PhotoImage(file="C:/Users/alebe/OneDrive - Universidad Autónoma del Estado de México/Documents/Python Scripts/Sistemas Expertos/SE_Turismo/Imagenes/Pueblo.jpg")
c4 = tk.Checkbutton(raiz, text="Pueblo", variable=tkPueblo, width=10, height=2, compound="top", bg="salmon3", fg="black")
c4.grid(row=3, column=2, pady=5)

lb3 = tk.Label(raiz, text="Seleccione la actividad que prefiere: ", width=30, bg="sky blue")
lb3.grid(row=4, column=1, pady=10)
#imgAventura = ImageTk.PhotoImage(file="C:/Users/alebe/OneDrive - Universidad Autónoma del Estado de México/Documents/Python Scripts/Sistemas Expertos/SE_Turismo/Imagenes/Aventura.jpg")
c5 = tk.Checkbutton(raiz, text="Aventura", variable=tkAventura, width=10, height=2, compound="top", bg="yellow2", fg="black")
c5.grid(row=5, column=0, pady=5)
#imgArqueologia = ImageTk.PhotoImage(file="C:/Users/alebe/OneDrive - Universidad Autónoma del Estado de México/Documents/Python Scripts/Sistemas Expertos/SE_Turismo/Imagenes/Arqueologia.jpg")
c6 = tk.Checkbutton(raiz, text="Arqueologia", variable=tkArqueologia, width=10, height=2, compound="top", bg="orange4", fg="black")
c6.grid(row=5, column=1, pady=5)
#imgReligioso = ImageTk.PhotoImage(file="C:/Users/alebe/OneDrive - Universidad Autónoma del Estado de México/Documents/Python Scripts/Sistemas Expertos/SE_Turismo/Imagenes/Religioso.jpg")
c7 = tk.Checkbutton(raiz, text="Religioso", variable=tkReligioso, width=10, height=2, compound="top", bg="purple1", fg="black")
c7.grid(row=5, column=2, pady=5)

l2 = tk.Label(raiz, text="Destino: ", bg="sky blue")
l2.grid(row=6, column=0, pady=2)
destino = tk.Text(raiz, state=tk.DISABLED, height=2, width=40)
destino.grid(row=6, column=1, pady=2)

l3 = tk.Label(raiz, text="Lugares: ", bg="sky blue")
l3.grid(row=7, column=0, pady=2)
lugares = tk.Text(raiz, state=tk.DISABLED, height=5, width=40)
lugares.grid(row=7, column=1, pady=2)

l4 = tk.Label(raiz, text="Descripción: ", bg="sky blue")
l4.grid(row=8, column=0, pady=2)
descripcion = tk.Text(raiz, state=tk.DISABLED, height=5, width=40)
descripcion.grid(row=8, column=1, pady=2)

btn1 = tk.Button(raiz, text="Aceptar", command=recomendarZona, bg="snow3")
btn1.grid(row=9, column=0, padx=5)

btn2 = tk.Button(raiz, text="Limpiar", command=limpiar, bg="snow3")
btn2.grid(row=9, column=2, padx=5)

raiz.mainloop()