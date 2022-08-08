import tkinter as tk
from tkinter import ttk,messagebox

from model.pelicula_dao import crear_tabla, borrar_tabla
from model.pelicula_dao import Pelicula, guardar, listar, editar, eliminar
from cliente.app_widgets import Boton, CajaTexto, Etiqueta, acercade


def barra_menu(master):
	barra_menu = tk.Menu(master)
	master.config(menu = barra_menu, width = 300, height = 300)

	menu_inicio = tk.Menu(barra_menu, tearoff = 0)
	barra_menu.add_cascade(label = "Inicio", menu = menu_inicio)

	menu_inicio.add_command(label = "Crear Registro en DB", command=crear_tabla)
	menu_inicio.add_command(label = "Eliminar Registro en DB", command= borrar_tabla)
	menu_inicio.add_command(label =" Salir", command=master.destroy)

	barra_menu.add_cascade(label = "Consultas")
	barra_menu.add_cascade(label = "Confifuración")
	barra_menu.add_cascade(label = "Ayuda")
	barra_menu.add_cascade(label = "Acerca de", command= acercade)

class MiFrame(tk.Frame):
	def __init__(self, master: None):
		super().__init__(master, width = 480, height = 320)

		self.master = master
		self.pack()

		self.id_pelicula=None

		self.campos_pelicula()
		self.deshabitar_campos()
		self.tabla_peliculas()

	def campos_pelicula(self):
		# Labels de los campos
		self.label_nombre = Etiqueta(self, "Nombre",0 , 0)

		self.label_duracion = Etiqueta(self, "Duración",1 , 0)

		self.label_genero =  Etiqueta(self, "Genero",2 , 0)

		# Entrys de los campos
		self.mi_nombre = tk.StringVar()
		self.entry_nombre= CajaTexto(self, self.mi_nombre, 0, 1)

		self.mi_duracion = tk.StringVar()
		self.entry_duracion = CajaTexto(self, self.mi_duracion, 1, 1)

		self.mi_genero = tk.StringVar()
		self.entry_genero = CajaTexto(self, self.mi_genero, 2, 1)

		#Botones
		self.boton_nuevo= Boton(self, "Nuevo")
		self.boton_nuevo.configuracion("#158645", "#DAD5D6","#35bd6f","red",self.habitar_campos)
		self.boton_nuevo.grilla(3, 0)

		self.boton_guardar= Boton(self, "Guardar")
		self.boton_guardar.configuracion("#1658A2", "#DAD5D6","#3586df","red",self.guardar_datos)
		self.boton_guardar.grilla(3, 1)

		self.boton_cancelar = Boton(self, "Cancelar")
		self.boton_cancelar.configuracion("#bd152e", "#DAD5D6","#e15370","white",self.deshabitar_campos)
		self.boton_cancelar.grilla(3, 2)

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
		self.id_pelicula = None

		self.mi_nombre.set("")
		self.mi_genero.set("")
		self.mi_duracion.set("")

		self.entry_nombre.config(state="disabled")
		self.entry_duracion.config(state="disabled")
		self.entry_genero.config(state="disabled")

		self.boton_guardar.config(state="disabled")
		self.boton_cancelar.config(state="disabled")

	def guardar_datos(self):

		pelicula = Pelicula(
			self.mi_nombre.get(),
			self.mi_duracion.get(),
			self.mi_genero.get(),
		)

		if self.id_pelicula == None:

			guardar(pelicula)
		else:
			editar(pelicula, self.id_pelicula)

		self.tabla_peliculas()

		self.deshabitar_campos()

	def tabla_peliculas(self):

		#Recuperar la lista de peliculas
		self.lista_peliculas = listar()
		self.lista_peliculas.reverse()

		self.tabla = ttk.Treeview(self, columns=("Nombre", "Duracón", "Genero"))
		self.tabla.grid(row = 4, column=0, columnspan=4, sticky="nse")

		self.scroll = ttk.Scrollbar(self, orient="vertical", command=self.tabla.yview)
		self.scroll.grid(row=4, column=4, sticky="nse")
		self.tabla.configure(yscrollcommand=self.scroll.set)

		self.tabla.heading("#0", text="ID")
		self.tabla.heading("#1", text="NOMBRE")
		self.tabla.heading("#2", text="DURACIÓN")
		self.tabla.heading("#3", text="GENERO")


		for p in self.lista_peliculas:
			self.tabla.insert("", 0, text=p[0], values=(p[1], p[2], p[3]))

		#Botones
		self.boton_editar = Boton(self, "Editar")
		self.boton_editar.configuracion("#158645", "#DAD5D6",  "#35bd6f","red",self.editar_datos)
		self.boton_editar.grilla(5, 0)

		self.boton_eliminar= Boton(self, "Eliminar")
		self.boton_eliminar.configuracion("#bd152e", "#DAD5D6","#e15370","white",self.eliminar_datos)
		self.boton_eliminar.grilla(5, 2)

	def editar_datos(self):
		try:
			self.id_pelicula = self.tabla.item(self.tabla.selection())['text']
			self.nombre_pelicula = self.tabla.item(self.tabla.selection())['values'][0]
			self.duracion_pelicula = self.tabla.item(self.tabla.selection())['values'][1]
			self.genero_pelicula = self.tabla.item(self.tabla.selection())['values'][2]

			self.habitar_campos()

			self.entry_nombre.insert(0, self.nombre_pelicula)
			self.entry_duracion.insert(0, self.duracion_pelicula)
			self.entry_genero.insert(0, self.genero_pelicula)
		except:
			titulo = "Edición de datos"
			mensaje = "No se ha seleccionado ningún registro"
			messagebox.showerror(titulo, mensaje)

	def eliminar_datos(self):
		try:
			self.id_pelicula = self.tabla.item(self.tabla.selection())['text']
			eliminar(self.id_pelicula)

			self.tabla_peliculas()
			self.id_pelicula= None

		except:
			titulo = "Eliminar de datos"
			mensaje = "No se ha seleccionado ningún registro"
			messagebox.showerror(titulo, mensaje)

