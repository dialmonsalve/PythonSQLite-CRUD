import tkinter as tk
from tkinter import messagebox


class Boton(tk.Button):
	def __init__(self, master:None, texto):
		super().__init__(master,text= texto)

		self.texto = texto

	def configuracion(self, fondo, color_letra, hover_fondo,hover_letra, comando):

		self.config(
			width = 20, 
			font = ("Arial", 12, "bold"),
			cursor = "hand2",
			bg = fondo, 
			fg = color_letra,
			activebackground = hover_fondo,
			activeforeground = hover_letra,
			command = comando)

	def grilla(self, fila, columna, columnspan=None):

		self.grid(row=fila, 
			column=columna, 
			padx=10, pady=10, 
			columnspan=columnspan)

class Etiqueta(tk.Label):
	def __init__(self, master:None, texto, fila, columna):
		super().__init__(master, text= texto)

		self.config(font = ("Arial", 12,  "bold"))

		self.grid(row= fila, column= columna, padx= 10, pady= 10)

class CajaTexto(tk.Entry):
	def __init__(self, master:None, text_variable, fila, columna):
		super().__init__(master, textvariable= text_variable)

		self.config(width = 50, font = ("Arial", 12,  "bold"))

		self.grid(row = fila, column = columna, padx = 10, pady = 10, columnspan = 2)

def acercade():

	titulo= "app DiaMones"
	mensaje = "Todos los derechos reservados \nⓒ Diego Monsalve 2022"
	messagebox.showinfo(titulo, mensaje)