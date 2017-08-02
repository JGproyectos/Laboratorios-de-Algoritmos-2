"""
Nombres: Gaspar Hermán Sandoval, Jesús Marcano	Carnets: 13-10637,	12-10359

Descripción: Implementar la tabla de Hash estática del laboratorio 7 Abr-Jul 2016
"""
# Importando modulos
import random  # Para la elección de números de una lista
# Creando las clases
class Entrada():
	def __init__(self,clave,dato):
		self.clave = clave  # Almacenamos la clave
		self.dato = dato  # Almacenamos el dato

# Definimos la funcion de Hash para la busqueda
def BusquedaHash(n):
	
	"""
	Hay que buscar un número primo más grande que n, lo cual se hará a partir de n. 
	Se buscará un primo un tanto más grande, a partir de 50 elementos mayores a n.
	"""

	divisores = 0  # se usará para guardar la cantidad de divisores encotrados
	n2 = n + 50  # Para empezar a buscar un número primo

	while True:  # Con esto buscará a partir de n + 50 en un intervalo de 50

		for i in range (1, n2 + 1):  # se hace así ya que al empezar en cero causaría que i se dividiera entre 0
			
			if (j % i == 0):
				divisores = divisores + 1

				if divisores > 2:  # Ya no es primo y no vale la pena seguir iterando respecto a este número salimos
					break

		n2 = n2 + 1  # Ajustamos el número a determinar si es primo
		if divisores == 2: # Es primo
			primo = j
			break  # Salimos del ciclo principal
	

	# primo = 123455681  # Número primo lo suficientemente grande

	a = random.randrange(1,primo)
	b = random.randonrange(0,primo)

class Hash():
	def crearTabla(self,n):
		self.Tablainicial = []  # Creamos el atributo aquí y lo inicializamos vacío
		for i in range(n):
			self.Tablainicial.append(None)  # Para que tome las dimensiones de n y además esté vacía


		"""
		Con este n se puede crear la idea de una función de hash que está dada por:
		(((ak +b) mod p) mod n), donde p es un primo mayor que n, a y b son tales que:

		(^a|a pertenezca a los naturales:[1..p))
		(^b|b pertenezca a los naturales: [0..p))

		realizar esa operación para ver un indice toma tiempo constante.

		Hay que buscar un número primo más grande que n, lo cual se hará a partir de n. 
		Se buscará un primo un tanto más grande, a partir de 50 elementos mayores a n.
		"""
		
		divisores = 0  # se usará para guardar la cantidad de divisores encotrados
		n2 = n + 50  # Para empezar a buscar un número primo

		while True:  # Con esto buscará a partir de n + 50 en un intervalo de 50

			for i in range (1, n2 + 1):  # se hace así ya que al empezar en cero causaría que i se dividiera entre 0
				
				if (n2 % i == 0):
					divisores = divisores + 1

					if divisores > 2:  # Ya no es primo y no vale la pena seguir iterando respecto a este número, salimos
						break

			n2 = n2 + 1  # Ajustamos el número a determinar si es primo
			if divisores == 2: # Es primo
				primo = n2
				break # Salimos del ciclo principal

			else:
				divisores = 0  # Reiniciamos		

		#primo = 123455681  # Número primo lo suficientemente grande

		self.a = random.randrange(1,primo)  # Para la funcion de busqueda
		self.b = random.randrange(0,primo)  # Para la funcion de busqueda
		self.primo = primo  # Para la función de busqueda

	def agregarelem(self,elemento):
		if len(self.Tablainicial) - 1 >= elemento.clave\
		and self.Tablainicial[elemento.clave] == None:  # En caso de que si haya esa posición en el arreglo
			self.Tablainicial[elemento.clave] = elemento.dato  # Sustituimos el elemento	

	def agregar(self,c,d):  # Agrega un elemento d en una clave c
		if c <= len(self.Tablainicial) - 1:  # En caso de que la clave esté dentro de la tabla
			if self.Tablainicial[c] != None:  # En este caso 
				self.Tablainicial.insert(c,d)  # Insertamos el elemento en esa posicion

			else:
				self.Tablainicial[c] = d  # En este caso sustituimos el elemento

		else:

			while len(self.Tablainicial) - 1 < c:
				self.Tablainicial.append(None)  # Insertamos elementos vacíos hasta que este alcance la posición

			"""
			Para este momento ya se ha llegado a la cantidad de elementos vacíos que están aquí, sólo falta 
			sustituir el último elemento de la lista por el que se quiere insertar. El inconveniente de esto
			se da para un c extremadamente más grande que n.
			"""

			self.Tablainicial[len(self.Tablainicial) - 1] = d

	def buscar(self,c):
		return self.Tablainicial[c]

	def elminar(self,c):
		if self.Tablainicial[c] == None:
			return self.Tablainicial[c]

		else:
			temporal = self.Tablainicial[c]  # Almacenamos el valor en una variable temporal
			self.Tablainicial.pop(c)
			return temporal

	def imprimir(self):
		claves = []
		elementos = []
		for i in range(len(self.Tablainicial)):
			if self.Tablainicial[i] != None:
				claves.append(i)
				elementos.append(self.Tablainicial[i])

		# Postcondicion
		assert(len(claves) == len(elementos))

		
		print("Claves: ",claves)

		print ("\n")
		print("Elementos: ",elementos)