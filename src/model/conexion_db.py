import sqlite3

class conexionBD:
	def __init__(self) -> None:
		self.base_datos = "src/database/peliculas.db"
		self.conexion = sqlite3.connect(self.base_datos)
		self.cursor = self.conexion.cursor()


	def cerrar(self):
		self.conexion.commit()
		self.conexion.close()
		