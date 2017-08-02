"""
Laboratorio 8 de Algoritmos y estructuras II
Jesus Marcano y Gaspar Herman
12-10359 _ 13-10637
Ejercicio 1, listas enlazadas.
"""
class Nodo(object):
	"""docstring for Nodo"""
	def __init__(self, dato):
		
		self.dato = dato
		self.prev = None
		self.prox = None
	
	def __str__(self):
		return str(self.dato)




class ListaDobleEnlazada(object):
	"""docstring for Listaenlazada"""
	def __init__(self):
		self.primero = None # esto sirve para decir que la lista esta vacia
		self.ultimo = None

	def getVacio(self):
		if self.primero == None: # Con esta verificamos si hay o no elementos en la lista
			return True

	def agregarI(self,elemento): #
		nuevo = Nodo(elemento)

		if self.getVacio()== True:
			self.primero = self.ultimo = nuevo
		else:
			nuevo.prox = self.primero
			self.primero.prev = nuevo
			self.primero = nuevo
		

	def Eliminar_elemto(self):
		if self.getVacio() == True: #Esto mes para indicar que la lista esta vacia lo verificamos si el primero o el ultimo es true
			print("La lista no contiene elementos para eliminar")

		elif self.primero == self.ultimo: # si nos queda un solo elemento, eliminamos y simplemente reiniciamos la lista con el primero y el ultimo vacioas
			self.primero = None #Ponemos el primero y el ultimo iguales a None, para que la lista nos quede vacia
			self.ultimo = None

		else:
			temp = self.primero #hacemos una variable temporal para almacenar el elemento a eliminar
			self.primer = self.primero.prox #Asignamos el valor de "primer elemento al proximo en la lista"
			self.primero.prev = None #Asiganmos el valor none para colocarlo como el primeor de ;a ;osta
			temp = None #eliminamos el elemento
			print("El elemento ha sido eliminado")

	def Imprimir_lista(self): 
		if self.getVacio() == True: #Verificamos si no hay elementos en la lista, si no hay se imprime, esta vacia
			print("La lista se encuentra vacia")
		else:
			validar = True #creamos una variable booleana para que verifique cada vez que estemos dentro del ciclo, al llegar al ultimo se convierte en False para concluir con el mismo
			temp = self.primero #Variable donde vamos a seleccionar el primer elemento, el cual se ir[a rodando del primero al ultimo para imprimir de orden de menor a mayor posicion de cada uno de los elementos (nodo)
			while validar:#verificamos en el ciclo while
				print(temp.__str__()) #imprimimos elemento
				if temp == self.ultimo: #Si temporal es el ultimo de la lista, terminamos y salimos del while con el false
					validar = False
				else: #De lo contrario simpre se tomara el siguiente al impreso
					temp = temp.prox


v1 = ListaDobleEnlazada()
#print(v1.agregarI("Manzanas"))
v1.agregarI("Peras")
v1.agregarI("Mango")
v1.agregarI("Durazno")
v1.agregarI("Pinhia")
v1.agregarI("PArchita")
v1.Imprimir_lista()
v2 = Nodo("Manzana")

print(v2)