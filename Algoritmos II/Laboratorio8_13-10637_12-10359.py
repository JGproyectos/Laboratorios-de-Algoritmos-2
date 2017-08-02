"""
Nombres: Gaspar Hermán	Jesús Marcano, Carnets: 13-10637	12-10359

Fecha:25/06/2016

Descripción: Arbol Binario de búsqueda.
"""
# Importando modulos necesarios
import random
import time
import sys
sys.setrecursionlimit(10000)  # Ajustamos el número de recursiones

# Definiendo algunas funciones

def Altura(nodo):
		if nodo is None:
			return -1

		else:
			temporal1 = Altura(nodo.izq)
			temporal2 = Altura(nodo.der)
			return (1 + max(temporal1,temporal2))

def imprimir(nodo):

	if nodo.der and nodo.izq is None:  # En caso de que no tenga hijos izquierdos
		print("$",nodo.valor)
		imprimir(nodo.der)

	if nodo.der is None and nodo.izq:
		print(nodo.valor,"$")
		imprimir(nodo.izq)

	if nodo.der is None and nodo.izq is None:
		print("\n","$ ",nodo.valor," $")

	if nodo.der and nodo.izq:
		print(nodo.izq.valor,"\t",nodo.der.valor,"\n")
		imprimir(nodo.izq)
		imprimir(nodo.der)

def mediana(arbol,lista):
	# Precondicion
	assert(all(lista[i] <= lista[i+1] for i in range(len(lista)-1)))

	if len(lista) != 1:
		n = len(lista) // 2
		print("se insertó el elemento: ",lista[n]," al árbol")
		arbol.insertar(lista[n])
		mediana(arbol,lista[n:])
		mediana(arbol,lista[:n])

def particion(arreglo, inicio, final):
    x = arreglo[inicio]
    izquierdo = inicio + 1
    derecho = final
   
    while True: # Bucle principal

        while izquierdo <= derecho and arreglo[izquierdo] <= x:
            izquierdo = izquierdo + 1 # Ajustamos el primer elementos

        while arreglo[derecho] >= x and derecho >=izquierdo:
            derecho = derecho -1

        if derecho < izquierdo:
            break

        else:

            arreglo[izquierdo],arreglo[derecho] = arreglo[derecho],arreglo[izquierdo]  # Realizamos el intercambio
    
    arreglo[inicio],arreglo[derecho]= arreglo[derecho],arreglo[inicio]
    return derecho

def randomparticion(arreglo,inicio,final):
	i = random.randint(inicio,final)
	arreglo[i],arreglo[final] = arreglo[final],arreglo[i]
	return particion(arreglo,inicio,final)

def RandomQuicksort(arreglo, inicio, final):
    if inicio < final:
		
        split = randomparticion(arreglo, inicio, final)
        RandomQuicksort(arreglo, inicio, split-1)
        RandomQuicksort(arreglo, split+1, final)

def Quicksort(arreglo,inicio,final):
	if inicio < final:
		
		split = particion(arreglo,inicio,final)
		Quicksort(arreglo, inicio, split-1)
		Quicksort(arreglo, split+1, final)

# Creando las clases
class Nodo():
	def __init__(self,elemento):
		self.valor = elemento  # Este es el valor númerico del nodo
		self.der = None  # Hijo Derecho
		self.izq = None  # Hijo Izquierdo


	def insertar(self,elemento):
		if self.valor >= elemento:  # Para insertar en el lado derechp

			if self.izq:  # En caso de que exista un hijo izquierdo para ese valor
				return self.izq.insertar(elemento)

			else:
				self.izq = Nodo(elemento)  # Convertimos el valor en un nodo y lo insertamos aquí
				return True

		else:

			if self.der:  # En caso de que si tenga un hijo derecho
				return self.der.insertar(elemento)

			else:
				self.der = Nodo(elemento)  # Convertimos esto en un nodo
				return True	

	def buscar(self,elemento):
		if self.valor == elemento:  # Justo en la raíz del árbol
			return True  # Indica que si está

		elif self.valor > elemento:

			if self.izq:
				return self.izq.buscar(elemento)  # Llamada recursiva

			else:
				return False  # Ya que no está dicho elemento

		else:
			if self.der:
				return self.der.buscar(elemento)  # Llamada recursiva

			else:
				return False  # Ya que no está dicho elemento			

	def preorder(self):
		if self:
			print(str(self.valor))

			if self.izq:
				self.izq.preorder()

			if self.der:
				self.der.preorder()

	def postorder(self):
		if self:
			
			if self.izq:
				self.izq.postorder()

			if self.der:
				self.der.postorder()

			print(str(self.valor))	

	def inorder(self):
		if self:
			if self.izq:
				self.izq.inorder()

			print(str(self.valor))	

			if self.der:
				self.der.inorder()


class Arbol():
	def __init__(self):
		self.raiz = None

	def insertar(self,elemento):
		if self.raiz:
			return self.raiz.insertar(elemento)

		else:
			self.raiz = Nodo(elemento)
			return True

	def buscar(self,valor):
		if self.raiz:  # En caso de que sea la raíz existente
			return self.raiz.buscar(valor)

		else:
			return False  # En caso de que no esté el valor

	def altura(self,nodo):

		self.alturas = Altura(nodo)
		return self.alturas

	def eliminar(self,valor):

		if self.raiz is None:  # El árbol está vacío
			return False
			
		elif self.raiz.valor == valor: # Se elimina la raíz 

			if self.raiz.izq is None and self.raiz.der is None:  # No tiene hijos
				self.raiz = None

			elif self.raiz.izq and self.raiz.der is None:  # Sólo tiene hijos izquierdos
				self.raiz = self.raiz.izq

			elif self.raiz.izq is None and self.raiz.der:  # Sólo tiene hijos derechos
				self.raiz = self.raiz.der

			elif self.raiz.izq and self.raiz.der:  # Tiene dos hijos

				delNodeParent = self.raiz
				delNode = self.raiz.der

				while delNode.izq:
					delNodeParent = delNode
					delNode = delNode.izq
					
				self.raiz.valor = delNode.valor

				if delNode.der:

					if delNodeParent.valor > delNode.valor:
						delNodeParent.izq = delNode.der

					elif delNodeParent.valor < delNode.valor:
						delNodeParent.der = delNode.der
				else:
					if delNode.valor < delNodeParent.valor:
						delNodeParent.izq = None

					else:
						delNodeParent.der = None
						
			return True
		
		parent = None
		node = self.raiz
		
		while node and node.valor != valor:
			parent = node

			if valor < node.valor:
				node = node.izq

			elif valor > node.valor:
				node = node.der
		
		if node is None or node.valor != valor:  # Valor no encontrado
			return False
			
		elif node.izq is None and node.der is None:  # No tiene hijos

			if valor < parent.valor:
				parent.izq = None

			else:
				parent.der = None

			return True
			
		elif node.izq and node.der is None:  # Sólo tiene hijos izquierdos

			if valor < parent.valor:
				parent.izq = node.izq

			else:

				parent.der = node.izq

			return True
			
		elif node.izq is None and node.der:  # Sólo tiene hijos derechos
			if valor < parent.valor:

				parent.izq = node.der

			else:
				parent.der = node.der

			return True
			
		else:  # Tiene dos hijos
			delNodeParent = node
			delNode = node.der
			while delNode.izq:
				delNodeParent = delNode
				delNode = delNode.izq
				
			node.valor = delNode.valor
			if delNode.der:
				if delNodeParent.valor > delNode.valor:
					delNodeParent.izq = delNode.der
				elif delNodeParent.valor < delNode.valor:
					delNodeParent.der = delNode.der
			else:
				if delNode.valor < delNodeParent.valor:
					delNodeParent.izq = None
				else:
					delNodeParent.der = None

	def preorder(self):
		print("Preorder")
		self.raiz.preorder()

	def postorder(self):
		print("Postorrder")
		self.raiz.postorder()

	def inorder(self):
		print("inorder")
		self.raiz.inorder()

# Inicio del programa

while True:
	print("escoja un caso para trabajar")
	print("caso 1 (escriba 1)")
	print("caso 2 (escriba 2")
	print("cero para salir")

	try:
		n = input()
		n = int(n)  # Se trata como un entero en lugar de texto
	except:
		print("marcó incorrecto")
		continue
	break

n = 1
# Condicionales
if n == 1:

	arbolito = Arbol()  # Creamos el arbol

	arreglo = [1942, 8728, 9150, 5444, 653, 6792, 9925, 5495, 600, 8960, 1439,\
292, 2456, 103, 4685, 8398, 8734, 4453, 1069, 6395, 2965, 5859, 5166, 7787, 209,\
7100, 5658, 1883, 8441, 5646, 2464, 9461, 693, 8706, 4974, 4673, 725, 4867, 187, 2310,\
6275, 2065, 1107, 60, 728, 1331, 6528, 8405, 4463, 8495, 119, 952, 5611, 2293, 355, 2018,\
5634, 8463, 9827, 7366, 1053, 3787, 6084, 2839, 7183, 508, 9479, 7510, 1568, 9943, 4215, 9345,\
554, 2812, 7565, 593, 9446, 1008, 7903, 2777, 21, 1248, 1647, 147, 6865, 3418, 9123, 1635, 7561, 841,\
9144, 2244, 5749, 5881, 3089, 695, 3023, 7729, 1291, 9513]


	for i in range(len(arreglo)): # Agregamos al árbol
		arbolito.insertar(arreglo[i])

	while True:
		print("\tEscoja que hacer")
		print("1 reordenar")
		print("2 calcular altura")
		print("3 comparar alturas")
		print("4 imprimir")
		print("5 salir")
		arbolito2 = Arbol()

		try:
			entrada = input()
			entrada = int(entrada)

		except:
			print("error")
			continue

		if entrada == 1:

			RandomQuicksort(arreglo,0,len(arreglo)-1)
			mediana(arbolito2,arreglo)
			arbolito2.insertar(arreglo[0])

		elif entrada == 2:
			altura1 = arbolito.altura(arbolito.raiz)
			altura2	= arbolito2.altura(arbolito2.raiz)

		elif entrada == 3:
			if altura1 < altura2:
				print(-1," es menor")	

			elif altura1 > altura2:
				print(1," es mayor")

			else:
				print(0"es igual")

		elif entrada == 4:
			print("que arbol quiere ver ")
			print("1 o 2")
			entrada2 = input()
			try:
				entrada2 = int(entrada2)
			except:
				print("error")
				continue

			if entrada2 == 1:
				imprimir(arbolito)

			elif entrada2 == 2:
				imprimir(arbolito2)

		elif entrada == 5:
			break
if n == 2:

	arbolito = Arbol()  # Creamos el arbol

	arreglo = [8093, 1939, 1949, 6724, 295, 7596, 9079, 4484, 3749, 4273, 727, 1614, 139, 2984, 9041, 9019, 5753, 6960, 72, 8602, 6176, 3543, 4948, 2521, 622, 3118, 3661, 2782, 1799, 9479, 488, 5991, 5057, 6217, 8772, 11, 4158, 5461, 6956, 3299, 8978, 8225, 6260, 329, 6804, 6843, 6128, 269, 3644, 1299, 9799, 8902, 2638, 3681, 390, 7568, 680, 3537, 5388, 3975, 1374, 1255, 3387, 4906, 4042, 6354, 7809, 9327, 59, 1175, 5543, 8383, 3656, 7555, 3029, 5796, 819, 597, 6317, 111, 7348, 6603, 4899, 7404, 4871, 180, 7226, 6036, 1851, 1913, 7723, 8919, 1128, 6378, 825, 6065, 178, 842, 8026, 9812, 9260, 593, 3298, 1104, 7488, 1680, 9958, 4815, 9537, 2120, 6195, 4578, 6428, 6158, 9273, 4902, 2102, 4343, 8122, 4047, 1654, 8719, 5074, 203, 8193, 9428, 6079, 9419, 1840, 9427, 2509, 228, 450, 4791, 5951, 1984, 845, 3066, 7965, 9190, 2432, 5300, 6965, 7791, 8377, 2996, 4112, 4968, 6575, 7623, 1847, 9927, 8046, 8721, 7485, 1123, 3734, 1214, 8088, 6312, 4940, 1996, 650, 6204, 293, 8945, 3483, 6192, 1052, 6012, 6863, 1397, 748, 4110, 555, 2391, 8119, 6243, 1978, 2574, 3701, 1235, 6283, 9376, 2200, 7269, 2000, 8522, 5447, 8817, 7764, 6690, 8886, 7733, 9839, 490, 16, 371, 4300, 6096, 917, 614, 7495, 2368, 5255, 260, 9785, 6834, 9617, 8781, 2783, 6709, 7050, 6190, 9028, 732, 305, 7401, 4447, 702, 7836, 816, 3934, 3521, 5700, 5636, 4250, 9589, 4854, 7560, 2563, 2674, 5678, 6118, 2736, 5880, 920, 3518, 6512, 1322, 22, 7853, 8052, 4228, 1015, 1424, 4142, 2705, 6694, 5113, 5838, 6588, 3590, 7297, 3878, 6554, 5649, 5403, 525, 1677, 1694, 8058, 8070, 8435, 5010, 2512, 3910, 9251, 8925, 2203, 306, 9493, 4190, 2031, 5503, 2732, 8230, 83, 2990, 9142, 710, 6819, 1042, 1272, 2587, 7419, 743, 8129, 1346, 9137, 3699, 3857, 2881, 6696, 3231, 7900, 7058, 5512, 5825, 5763, 247, 2068, 9774, 3667, 1546, 2, 7707, 924, 6552, 3740, 4429, 7875, 7437, 1283, 6655, 8609]

	for i in range(len(arreglo)): # Agregamos al árbol
		arbolito.insertar(arreglo[i])

	while True:
		print("\tEscoja que hacer")
		print("1 reordenar")
		print("2 calcular altura")
		print("3 comparar alturas")
		print("4 imprimir")
		print("5 salir")
		arbolito2 = Arbol()

		try:
			entrada = input()
			entrada = int(entrada)

		except:
			print("error")
			continue

		if entrada == 1:

			RandomQuicksort(arreglo,0,len(arreglo)-1)
			mediana(arbolito2,arreglo)
			arbolito2.insertar(arreglo[0])

		elif entrada == 2:
			altura1 = arbolito.altura(arbolito.raiz)
			altura2	= arbolito2.altura(arbolito2.raiz)

		elif entrada == 3:
			if altura1 < altura2:
				print(-1," es menor")	

			elif altura1 > altura2:
				print(1," es mayor")

			else:
				print(0"es igual")

		elif entrada == 4:
			print("que arbol quiere ver ")
			print("1 o 2")
			entrada2 = input()
			try:
				entrada2 = int(entrada2)
			except:
				print("error")
				continue

			if entrada2 == 1:
				imprimir(arbolito)

			elif entrada2 == 2:
				imprimir(arbolito2)

		elif entrada == 5:
			break