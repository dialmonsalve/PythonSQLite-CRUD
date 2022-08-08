#-------dialmonsalve@dialmonsalve.onmicrosoft.com------
""" This is the module wich includes the main exec window """
# ###########################################################################
# 	Project: App for training												#
# 	Create by: Diego Alejandro Monsalve	E									# 
#	Start date: 07/08/2022													#
#	End date: 																#
# 	Copryght: 2022															#
# ###########################################################################
import tkinter as tk
from cliente.app_frame import MiFrame, barra_menu

def main():
	root = tk.Tk()
	root.title('Catalogo de peliculas')
	root.iconbitmap('src/img/2Movies_37443.ico')
	root.minsize(width=850,height=470)

	barra_menu(root)

	miFrame = MiFrame(root)

	miFrame.mainloop()


if __name__ =='__main__':
	main()
