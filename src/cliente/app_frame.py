import tkinter as tk
from tkinter import ttk

def barra_menu(master):
	barra_menu = tk.Menu(master)
	master.config(menu = barra_menu, width = 300, height = 300)

	menu_inicio = tk.Menu(barra_menu, tearoff = 0)
	barra_menu.add_cascade(label = "Inicio", menu = menu_inicio)

	menu_inicio.add_command(label = "Crear Registro en DB")
	menu_inicio.add_command(label = "Eliminar Registro en DB")
	menu_inicio.add_command(label =" Salir", command=master.destroy)

	barra_menu.add_cascade(label = "Consultas")
	barra_menu.add_cascade(label = "Confifuración")
	barra_menu.add_cascade(label = "Ayuda")
	barra_menu.add_cascade(label = "Acerca de")

class MiFrame(tk.Frame):
	def __init__(self, master: None):
		super().__init__(master, width = 480, height = 320)

		self.master = master
		self.pack()
		#self.config(bg="green")
		

		self.campos_pelicula()
		self.deshabitar_campos()
		self.tabla_peliculas()

	def campos_pelicula(self):
		# Labels de los campos
		self.label_nombre = tk.Label(self, text="Nombre: ")
		self.label_nombre.config(font = ("Arial", 12,  "bold"))
		self.label_nombre.grid(row = 0, column = 0, padx = 10, pady = 0)

		self.label_duracion = tk.Label(self, text = "Duración: ")
		self.label_duracion.config(font = ("Arial", 12, "bold"))
		self.label_duracion.grid(row = 1, column = 0, padx = 10, pady = 10)

		self.label_genero = tk.Label(self, text = "Genero: ")
		self.label_genero.config(font = ("Arial", 12, "bold"))
		self.label_genero.grid(row = 2, column = 0, padx = 10, pady = 10)

		# Entrys de los campos
		self.mi_nombre = tk.StringVar()
		self.entry_nombre = tk.Entry(self, textvariable= self.mi_nombre)
		self.entry_nombre.config(width = 50, font = ("Arial", 12))
		self.entry_nombre.grid(row = 0, column = 1, padx = 10, pady = 10, columnspan = 2)

		self.mi_duracion = tk.StringVar()
		self.entry_duracion = tk.Entry(self, textvariable= self.mi_duracion)
		self.entry_duracion.config(width=50, font=("Arial", 12))
		self.entry_duracion.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

		self.mi_genero = tk.StringVar()
		self.entry_genero = tk.Entry(self, textvariable= self.mi_genero)
		self.entry_genero.config(width=50, font=("Arial", 12))
		self.entry_genero.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

		#Botones
		self.boton_nuevo = tk.Button(self, text="Nuevo")
		self.boton_nuevo.config(
			width=20,
			font=("Arial", 12, "bold"),
			fg="#DAD5D6", bg="#158645", 
			cursor="hand2", 
			activebackground="#35bd6f",
			activeforeground="red",
			command = self.habitar_campos
			)
		self.boton_nuevo.grid(row=3, column=0, padx=10, pady=10)

		self.boton_guardar = tk.Button(self, text="Guardar")
		self.boton_guardar.config(
			width=20,
			font=("Arial", 12, "bold"),
			fg="#DAD5D6", bg="#1658A2", 
			cursor="hand2", 
			activebackground="#3586df",
			activeforeground="red",
			command = self.guardar_datos
			)
		self.boton_guardar.grid(row=3, column=1, padx=10, pady=10)

		self.boton_cancelar = tk.Button(self, text="Cancelar")
		self.boton_cancelar.config(
			width=20,
			font=("Arial", 12, "bold"),
			fg="#DAD5D6", bg="#bd152e", 
			cursor="hand2", 
			activebackground="#e15370",
			activeforeground="white",
			command = self.deshabitar_campos
			)
		self.boton_cancelar.grid(row=3, column=2, padx=10, pady=10)

	def habitar_campos(self):
		self.mi_nombre.set("")
		self.mi_genero.set("")
		self.mi_duracion.set("")

		self.entry_nombre.config(state="normal")
		self.entry_duracion.config(state="normal")
		self.entry_genero.config(state="normal")

		self.boton_guardar.config(state="normal")
		self.boton_cancelar.config(state="normal")

	def deshabitar_campos(self):
		self.mi_nombre.set("")
		self.mi_genero.set("")
		self.mi_duracion.set("")

		self.entry_nombre.config(state="disabled")
		self.entry_duracion.config(state="disabled")
		self.entry_genero.config(state="disabled")

		self.boton_guardar.config(state="disabled")
		self.boton_cancelar.config(state="disabled")

	def guardar_datos(self):

		self.deshabitar_campos()

	def tabla_peliculas(self):

		self.tabla = ttk.Treeview(self, columns=("Nombre", "Duracón", "Genero"))
		self.tabla.grid(row = 4, column=0, columnspan=4)

		self.tabla.heading("#0", text="ID")
		self.tabla.heading("#1", text="NOMBRE")
		self.tabla.heading("#2", text="DURACIÓN")
		self.tabla.heading("#3", text="GENERO")

		self.tabla.insert("", 0, text="1", values=("los vengadores", "2.35", "Accion"))

		#Botones
		self.boton_editar = tk.Button(self, text="Editar")
		self.boton_editar.config(
			width=20,
			font=("Arial", 12, "bold"),
			fg="#DAD5D6", bg="#158645", 
			cursor="hand2", 
			activebackground="#35bd6f",
			activeforeground="red",
			)
		self.boton_editar.grid(row=5, column=0, padx=10, pady=10)

		self.boton_eliminar = tk.Button(self, text="Eliminar")
		self.boton_eliminar.config(
			width=20,
			font=("Arial", 12, "bold"),
			fg="#DAD5D6", bg="#bd152e", 
			cursor="hand2", 
			activebackground="#e15370",
			activeforeground="white",
			)
		self.boton_eliminar.grid(row=5, column=2, padx=10, pady=10)
