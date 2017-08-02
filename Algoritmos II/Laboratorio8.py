"""
Nombres: Gaspar Hermán Sandoval, Jesús Marcano	carnet:13-10637, 12-10359

Descripcion: Laboratorio 8
"""

class Nodo(object):
	"""docstring for Nodo"""
	def __init__(self, elemento):
		self.elemento = elemento
		self.right = None
		self.left = None
		self.dad = None
		self.piso = 0


# Creando la clase
class ArbolBinario():
	def __init__(self):
		#self.elemento = elemento  # Esta es la raíz del árbol
		self.raiz = None  #Este será un centinela del inicio Inicialmente el árbol está vacío
		self.last = None  #Este es un centinela del final (Al estidlo de arboles Rojo negro) Inicialmente el árbol está vacío
	def getVacio(self):
		if self.raiz == None: # Con esta verificamos si hay o no elementos en la lista
			return True
	
	def Agregar(self, elemento):
		nuevo = Nodo(elemento)# este es uin elemento nuevo
		if self.getVacio() == True:#Verificamos si el arbol esta vacio
			self.raiz = nuevo.elemento
			nuevo.dad = None

		else:
			y = None
			x = Nodo(self.raiz)
			while x.elemento != None:
				y = x
				if nuevo.elemento < x.elemento:
					x = x.left
				else:
					
		

	def Buscar(self, x, elemento):
		if x.elemento == elemento:
			print("Se ha encontrado su elemento y es la raiz de su árbol", elemento)
		else:
			if elemento < x.elemento:
				x = x.left
				return Buscar(elemento)

			else:
				x = x.right
				return Buscar(elemento)


#v1 = Nodo()

v1 = Nodo("lorito")
v2 = Nodo("loro")
v1.dad = None
v1.left = v2
v2.dad = v1.elemento

print(v1.elemento)
print(v1.dad)
print(v2.elemento)
print(v2.dad)
v1 = v2
print(v1.elemento)
print(v1.dad)