"""
Nombres: Gaspar Hermán Sandoval, Jesus Marcano Carnets: 13-10637, 12-10359

Descripcion: Proyecto I Algoritmos y Estructuras II
"""
# Importando modulos necesarios
import sys
import time
from math import floor
import random
"""
Quicksort
"""


sys.setrecursionlimit(10000)  # Ajustamos el número de recursiones

#################QUICKSORT######################


import random
import time
global comparacion
comparacion = 0
global logicas
logicas = 0
global asignacion
asignacion = 0
global aritmeticas
aritmeticas =0
def QuickSort(arreglo):
	primer = 0 
	ultimo = len(arreglo)
	global aritmeticas
	
	if primer < ultimo:
		q = particion(arreglo,primer,ultimo)

		QuickSort(arreglo,primer,q - 1)
		QuickSort(arreglo,q + 1,ultimo)
	return(arreglo)


def particionRandomizada(arreglo,primer,ultimo):
	global asignacion

	 
	i = random.randrange(primer,ultimo)
	
	arreglo[i],arreglo[ultimo] = arreglo[ultimo],arreglo[i]
	q = particion(arreglo,primer,ultimo)

	return q

def particion(arreglo,primer,ultimo):
	global asignacion
	global comparacion
	global logicas
	global aritmeticas

	
	x = arreglo[primer]
	
	izquierdo = primer + 1
	derecho = ultimo

	while True:
		print("izq",izquierdo, derecho,"arrg",arreglo[izquierdo][0],x[0])
		print("\n")
		while izquierdo <= derecho and arreglo[izquierdo][0] <= x[0]:
			izquierdo = izquierdo + 1

		while arreglo[derecho][0] >= x[0] and derecho >= izquierdo:
			print(arreglo[derecho][0],x[0])
			derecho = derecho - 1

		if derecho < izquierdo:
			break

		else:
			arreglo[izquierdo],arreglo[derecho] = arreglo[derecho],arreglo[izquierdo]
			asignacion = asignacion +  1

	arreglo[primer],arreglo[derecho] = arreglo[derecho],arreglo[primer]
	asignacion = asignacion + 1


# Postcondicion


# Definiendo algunas variables iniciales
global ADNbasura
ADNbasura = []
global frecuencia1
frecuencia1 = []

def merge(arreglo1:list,arreglo2:list)->list:
	
	final = []  # Como el método consiste en agregar a una lista el primero de cada sublista se guarda aquí
	contador1 = 0  # Se usa un contador saber donde agregar cada elemento
	contador2 = 0 

	while(contador1 < len(arreglo1) or contador2 < len(arreglo2)): 

		if(contador1 >= len(arreglo1)):
			final.append(arreglo2[contador2]) 
			contador2 = contador2 + 1 

		elif(contador2 >= len(arreglo2)): 
			final.append(arreglo1[contador1]) 
			contador1 = contador1 + 1 

		elif(arreglo1[contador1] < arreglo2[contador2]): 
			final.append(arreglo1[contador1]) 
			contador1 = contador1 + 1 

		else: 
			final.append(arreglo2[contador2]) 
			contador2 = contador2 + 1 

	# Postocondicion
	return final	

def mergesort(arreglo:list)->list:  # El valor inicial de p suele ser 0 y el de r len(arreglo)
	if len(arreglo) == 1:
		return arreglo

	else:
		izquierdo = arreglo[:len(arreglo)//2]  # Cortamos el arreglo a la mitad izquierda
		derecho = arreglo[len(arreglo)//2:]  # Coramos el arreglo en su mitad derecha

		izquierdo = mergesort(izquierdo)
		derecho = mergesort(derecho)

		return merge(izquierdo,derecho)

# Definiendo esta mitosis para su uso más adelante
def mitosis1(arreglo):
	# Lo primero que hay que hacer es separar en dos cadenas la cadena actual usando unzip
	simple1 = []  # Se almacenará aquí una mitad de la cadena doble
	simple2 = []  # Se almacenará aquí la otra mitad de la cadena doble de entrada

	try:
		# Precondicion
		assert(all(isinstance(arreglo[i],tuple)) for i in range(len(arreglo)))

	except AssertionError:
			print("hubo un error leyendo datos. Por favor revise")
			sys.exit()	

	for i in range(len(arreglo)):
		for j in range(2):  # Esto es debido a que es un arreglos de tuplas de dos elementos
			if j % 2 == 0:
				simple1.append(arreglo[i][j])

			else:
				simple2.append(arreglo[i][j])

	# Postcondicion
	assert(len(simple1) == len(simple2) and (len(arreglo) == len(simple2)))

	# Ahora hay que buscar el complemento de cada una usando el método de complementar
	complemento_para1 = []  # Se guarda el complemento para simple1
	complemento_para2 = []  # Se guarda el complemento para simple2

	# Hay que recorrer todo el arreglo para conocer cual es el complemento
	# Para simple1
	for base in range(len(simple1)):
		if simple1[base] == "A":
			complemento_para1.append("T")

		elif simple1[base] == "T":
			complemento_para1.append("A")

		elif simple1[base] == "G":
			complemento_para1.append("C")

		else:
			complemento_para1.append("G")	

	# Postcondicion
	assert(len(complemento_para1) == len(simple1))

	# Para simple2
	for base in range(len(simple1)):
		if simple2[base] == "A":
			complemento_para2.append("T")

		elif simple2[base] == "T":
			complemento_para2.append	("A")

		elif simple2[base] == "G":
			complemento_para2.append("C")

		else:
			complemento_para2.append("G")	

	# Postcondicion
	assert(len(complemento_para2) == len(simple2))

	"""
	Ahora que tenemos simple1 y su complemento al igual que simple2 y su complemento
	buscaremos convertir ambas en una sola cadena usando zip.
	"""

	# Para 1
	cadena_final1 = []  # Almacenamos los complementos de la cadena dada junto a su original

	# Crearemos la doble
	for i in range(len(complemento_para1)):
		temporal = (simple1[i],complemento_para1[i])  # Almacenamos la cadena original y el complemento
		cadena_final1.append(temporal)

	# Postcondicion
	assert(len(cadena_final1) == len(complemento_para1))

	# Para 2
	cadena_final2 = []  # Almacenamos los complementos de la cadena dada junto a su original

	# Crearemos la doble
	for i in range(len(complemento_para2)):
		temporal = (simple2[i],complemento_para2[i])  # Almacenamos la cadena original y el complemento
		cadena_final2.append(temporal)

	# Postcondicion
	assert(len(cadena_final2) == len(complemento_para2))

	return (cadena_final1,cadena_final2)

"""
comienzo del codigo de 
		HEAPSORT
.............
"""

def Heapsort(A):
	n = len(A)
	BuildHeap(A)
	for i in range(n-1, 0,-1):
		var = A[0]
		A[0] = A[i]
		A[i] = var
		Heapify(A, 0 , i)
	return(A)


def BuildHeap(A): # funcion para crear el arbol
	n = len(A)
	for i in range((n//2)-1, -1,-1):
		Heapify(A, i , n)
		
		
		
def Heapify(A, j, x):#intercambio de orden de los hijos y padres
	largest = j
	left = 2*j +1 #hijo izquiero
	right = 2*j + 2 # hijo derecho
	
	
	if left < x and A[left]< A[j]:
		largest = left 
	if right < x and A[right] < A[largest]:
		largest = right
	if largest != j:
		var = A[j]
		A[j] =  A[largest] 
		A[largest] = var 
		Heapify(A, largest, x)

		
"""
Fin del 
	HEAPSORT
	............
"""
def borrar_espacios(x:str)->list:  # Funcion que carga una lista en un arreglo y quita el "\n"
	y = []  # lista vacia donde se almacenará todo

	# Se carga un archivo de texto que contenga la información necesaria de los productos
	with open(x,'r') as f:
		datos = f.readlines()  # Almacenamos todos los datos del archivo aquí

	for line in datos:  # Colocamos cada línea del archivo dentro del arreglo
		y.append(line)

	# Eliminamos el "\n" de cada elemento del arreglo
	for i in range(len(y)):
		y[i] = y[i].replace("\n","")

		if y[i].isnumeric():  # En caso de tener un número tratado como texto se convierte en un número
			y[i] = int(y[i])

		# Invariante
		assert(all(y[i] == y[i].replace("\n","")) for i in range(len(y)))	  
	print(y)
	return y


"""
Esta funcion tiene una particularidad curiosa: La idea consiste en sacar una cadena de ADN simple de un texto y 
convertira en doble. La idea consiste en usar el metodo zip que fue programado antes de esta función, aquí el detalle,
la cadena simple que se quiera convertir en doble, antes de eso debe convertirse en un objecto ADNdoble, luego
se llama al método ADNdoble.zip([]). ¿Por qué []?. Por detalles en la especificación se colocó que el método recibe una cadena.
Es más fácil de arreglar convirtiendo dicha cadena en un objeto y llamar al método que cambiar todos los métodos.
"""

def lectura_archivo(archivo):
	primera_lista = borrar_espacios(archivo)  # Aquí se guardará cada linea en un arreglo sin el "\n"
	lista_salida1 = []

	"""
	Aquí se almacenan listas, cada lista es una cadena de ADN, cuyos elementos están separados por comas.
	Además se iterará a lo largo de la primera_lista y luego a lo largo de cada elemento en dicha lista para
	que se agregue a la lista de salida.
	"""

	for i in range(len(primera_lista)):
		lista_temporal = []  # En esta lista se guardarán los elementos a agregar a lista_salida

		for j in range(len(primera_lista[i])):
			lista_temporal.append(primera_lista[i][j])

		lista_salida1.append(lista_temporal)  # Agregamos la cadena separa por comas en esta lista al salir de la iteración

	for i in range(len(lista_salida1)):
		lista_salida1[i] = ADNdoble(lista_salida1[i])
		lista_salida1[i] = lista_salida1[i].zip([])
	
	#print("esto es lo que devuelve (lectura_archivo)","\n",lista_salida1)
	return lista_salida1	

def leerAminoacidos(archivo):
	lectura = borrar_espacios(archivo)  # Aquí se guardará todo sin el "\n"
	salida = []  # Guardaremos los elementos aquí
	"""
	A partir de ahora hay que una vez leída la cadena de ADN simple convertirlas todas en aminoacidos
	sin sintetizar
	"""
	for i in range(len(lectura)):
		temporal = []

		for j in range(len(lectura[i])):
			temporal.append(lectura[i][j])

		salida.append(temporal)	
		#print(temporal)
	print("Salida:", salida)
	for i in range(len(salida)):
		salida[i] = ADNsimple(salida[i])  # Transforma cada elemento de esta lista en un objeto
		salida[i] = salida[i].transcribir()  # Devuelve los elementos convertidos en aminoacidos
		salida[i] = salida[i].traducir()
	#print("esto es lo que devuelve leer aminoacidos", "\n",salida)
	return salida

def SintetizarProteinas(archivo):
	dato_inicial = leerAminoacidos(archivo)  # Convertimos la cadena en un ARN para poder sintetizar proteínas

	for i in range(len(dato_inicial)):
		dato_inicial[i] = Proteina(dato_inicial[i]) # Convertimos el ARNt en una proteína
		dato_inicial[i] = dato_inicial[i].sintetizar()  # Creamos la sintetis ahora

	return dato_inicial	


# Creando las clases
class ADNsimple():
	def __init__(self,cadena):
		self.size = len(cadena)
		self.cadena = cadena
		self.complemento = []  # Se almacenarán aquí los complementos
	# Metodos	
	def complementar(self):  # Genera la cadena complemento
		# Precondicion
		try:

			assert(all(isinstance(self.cadena[i],str) for i in range(self.size)))

		except AssertionError:
			print("hubo un error leyendo los datos")
			sys.exit()	

		# Hay que recorrer todo el arreglo para conocer cual es el complemento
		for base in range(self.size):
			if self.cadena[base] == "A":
				self.complemento.append("T")

			elif self.cadena[base] == "T":
				self.complemento.append	("A")

			elif self.cadena[base] == "G":
				self.complemento.append("C")

			else:
				self.complemento.append("G")	

		# Postcondicion
		assert(len(self.complemento) == self.size)
		return self.complemento

	def transcribir(self):
		# Hacemos el llamado del método para complementar
		#ARN = self.complementar()  # En caso de usar esto absolutamente TODOS los casos se vuelven basura
		ARN = self.cadena

		print(ARN)
		# Realizamos el cambio de la Timina por Uralcio, para esto hay que recorrer todo el arreglo
		for i in range(len(ARN)):
			if ARN[i] == "T":
				ARN[i] = "U"

		ARN = ARNt(ARN)  # Convertimos nuestro ARN en un objeto de la clase ARNt para que tenda todos sus métodos y lo retornamos
		return ARN

class ADNdoble(ADNsimple):
	def __init__(self,cadena):
		self.nueva_cadena = []  # Aquí se almacenará la cadena doble completa
		self.size = len(cadena)
		self.cadena = cadena  # Cadena simple
		self.complemento = []  # Se almacenarán aquí los complementos
		self.simple1 = []  # Se almacena una simple para el proceso unzip
		self.simple2 = []  # Se almacena la otra simple para el proceso de unzip
		self.simple_doble1 = []  # Para almacenar datos una vez hecha la mitosis
		self.simple_doble2 = []  # Para almacenar datos una vez hecha la mitosis

	def zip(self,cadena):  # Crea una cadena doble a partir de una simple
		el_complemento = self.complementar()  # Almacenamos los complementos de la cadena dada
		cadena_final = []  # Se almacena aquí la cadena ya creada

		# Crearemos la doble
		for i in range(len(self.complemento)):
			temporal = (self.cadena[i],el_complemento[i])  # Almacenamos la cadena original y el complemento
			self.nueva_cadena.append(temporal)

		# Postcondicion
		assert(len(self.nueva_cadena) == len(self.complemento))
		cadena_final = self.nueva_cadena
		return cadena_final

	def unzip(self):  # Funcion para separar las cadenas de ADN
		try:
			# Precondicion
			assert(all(isinstance(self.nueva_cadena[i],tuple)) for i in range(len(self.nueva_cadena)))

		except AssertionError:
			print("hubo un error leyendo datos. Por favor revise")
			sys.exit()	

		for i in range(self.size):
			for j in range(2):  # Esto es debido a que es un arreglos de tuplas de dos elementos
				if j % 2 == 0:
					self.simple1.append(self.nueva_cadena[i][j])

				else:
					self.simple2.append(self.nueva_cadena[i][j])

		# Postcondicion
		assert(len(self.simple1) == len(self.simple2) and (self.size == len(self.simple2)))

		"""
		Como simple1 y simple 2 son atributos del objeto ADNdoble no hay necesidad de hacerles un return.
		En caso de querer acceder a estas listas, sólo hay que hacer un llamado simple al atributo, además
		de esta manera es posible usar los mismos atributos para el proceso de mitosis.
		"""	

	def mitosis(self):

		"""
		Se debe hacer un llamado a una función externa que haga todo el proceso de mitosis.
		La idea original era usar todos los metodos disponibles hasta el momento y fusionarlos 
		de forma tal que fuera posible hacer una mitosis. El problema recae en la forma de llamar 
		los métodos, la cual hace que se sobreescriba información, cosa que no se quiere.
		"""

		if len(self.nueva_cadena) != 0:
			cadena_a_separar = self.nueva_cadena			

			# Llamamos a la funcion
			salida = mitosis1(cadena_a_separar)

			# Guardamos esto como atributos del objeto
			self.simple_doble1 = salida[0]
			self.simple_doble2 = salida[1]

		else:
			print("no hay cadenas disponibles, por favor intentelo de nuevo")
			sys.exit()

	def busqueda(self,cadena):
		# Precondicion
		try:
			assert(len(cadena) <= len(self.nueva_cadena) and (len(self.nueva_cadena) > 0))

		except AssertionError:	
			print("Hubo uno de dos posibles errores:")
			print("1) la cadena a buscar es más grande que la que se tiene")
			print("2) aún no se usa el método de crear una cadena doble de ADNdoble, por favor hagalo")
			print("abortando en:")
			print(3)
			time.sleep(1)
			print(2)
			time.sleep(1)
			print(1)
			time.sleep(1)
			print(0)
			sys.exit()

		# Declaración de variables iniciales del proceso
		cadena_original = self.nueva_cadena
		cadena_simple1 = []  # Aquí almacenamos una parte de la cadena original
		cadena_simple2 = []  # Aquí almacenamos la otra parte de la cadena original

		for i in range(len(cadena_original)):
			for j in range(2):  # Esto es debido a que es un arreglos de tuplas de dos elementos
				if j % 2 == 0:
					cadena_simple1.append(cadena_original[i][j])

				else:
					cadena_simple2.append(cadena_original[i][j])

		# Postcondicion
		assert(len(cadena_simple1) == len(cadena_simple2) and (len(cadena_original) == len(cadena_simple1)))

		complemento_buscar = []  # Almacenamos el complemento de la sub cadena simple aquí

		# Hay que recorrer todo el arreglo para conocer cual es el complemento
		# Un método de ADNsimple más generalizado
		for base in range(len(cadena)):
			if cadena[base] == "A":
				complemento_buscar.append("T")

			elif cadena[base] == "T":
				complemento_buscar.append	("A")

			elif cadena[base] == "G":
				complemento_buscar.append("C")

			else:
				complemento_buscar.append("G")	

		# Postcondicion
		assert(len(complemento_buscar) == len(cadena))

		# Para hacer la busqueda más simple	
		variable = ""  # Aquí se colocará todo el string

		cadena_simple1 = variable.join(cadena_simple1)

		variable = ""  # Reiniciamos

		cadena_original = variable.join(cadena_simple2)

		variable = ""  # Reiniciamos

		complemento_buscar = variable.join(complemento_buscar)

		variable = ""  # Reiniciamos

		cadena_a_buscar = variable.join(cadena)

		Existencia = False  # Almacenamos si está o no la cadena dentro de la otra, por defecto estará en False

		if (cadena_a_buscar in cadena_simple1) or (cadena_a_buscar in cadena_simple2) or (complemento_buscar in cadena_simple1)\
		or (complemento_buscar in cadena_simple2):
			Existencia = True

		if Existencia:
			print("la subcadena pasada, si existe dentro de la cadena doble")

		else:
			print("la subcadena pasada no existe dentro de la cadena doble")

	def imprimir(self):
		print(self.nueva_cadena)

class Proteina():
	def __init__(self,cadena):
		self.cadena = cadena
		self.codones_existentes = ["AUG","UUU","UUC","UUA","UUG","CUU","CUC","CUA","CUG","AUU","AUC","AUA","GUU","GUC","GUA","GUG",\
		"UCU","UCC","UCA","UCG","CCU","CCC","CCA","CCG","ACU","ACC","ACA","ACG","GCU","GCC","GCA","GCG","UAU","UAC","CAU","CAC",\
		"CAA","CAG","AAU","AAA","AAG","GAU","GAC","GAA","GAG","UGU","UGC","UGG","CGU","CGC","CGA","CGG","AGU","AGC","AGA","AGG",\
		"GGU","GGC","GGA","GGG","UAG","UAA","UGA","AAC"]

		self.proteina = []  # Se almacenará aquí la proteína sintetizada, por partes
		self.proteinaFinal = []  # Aquí se almacena una proteina por cada proteina generada en el ARNT

	def sintetizar(self):
		abreviacion_proteinas = ["Met","Phe","Leu","Ile","Val","Ser","Pro","Thr","Ala","Tyr","His","Gln","Asn",\
		"Lys","Asp","Glu","Cys","Trp","Arg","Gly"]

		"""
		Iniciamos una iteración a lo largo de la cadena que se pasó de argumento, comparando uno a uno sus elementos,
		en base a los resultados le asignaremos un valor de la lista abreviaciom_proteinas a self.proteina
		"""
		for j in range(len(self.cadena)):
			for i in range(len(self.cadena[j])):
				try:
					if self.cadena[j][i] == self.codones_existentes[0]:
						self.proteina.append(abreviacion_proteinas[0])

					elif self.cadena[j][i] == self.codones_existentes[1] or self.cadena[j][i] == 	self.codones_existentes[2]:
						self.proteina.append(abreviacion_proteinas[1])

					elif self.cadena[j][i] == self.codones_existentes[3] or self.cadena[j][i] == self.codones_existentes[4] or \
					self.cadena[j][i] == self.codones_existentes[5] or self.cadena[j][i] == self.codones_existentes[6] or \
					self.cadena[j][i] == self.codones_existentes[7] or self.cadena[j][i] == self.codones_existentes[8]:
						self.proteina.append(abreviacion_proteinas[2])

					elif self.cadena[j][i] == self.codones_existentes[9] or self.cadena[j][i] == self.codones_existentes[10] or\
					self.cadena[j][i] == self.codones_existentes[11]:
						self.proteina.append(abreviacion_proteinas[3])

					elif self.cadena[j][i] == self.codones_existentes[12] or self.cadena[j][i] == self.codones_existentes[13] or\
					self.cadena[j][i] == self.codones_existentes[14] or self.cadena[j][i] == self.codones_existentes[15]:
						self.proteina.append(abreviacion_proteinas[4])

					elif self.cadena[j][i] == self.codones_existentes[16] or self.cadena[j][i] == self.codones_existentes[17] or\
					self.cadena[j][i] == self.codones_existentes[18] or self.cadena[j][i] == self.codones_existentes[19] or\
					self.cadena[j][i] == self.codones_existentes[53] or self.cadena[j][i] == self.codones_existentes[52]:
						self.proteina.append(abreviacion_proteinas[5])

					elif self.cadena[j][i] == self.codones_existentes[20] or self.cadena[j][i] == self.codones_existentes[21] or\
					self.cadena[j][i] == self.codones_existentes[22] or self.cadena[j][i] == self.codones_existentes[23]:
						self.proteina.append(abreviacion_proteinas[6])

					elif self.cadena[j][i] == self.codones_existentes[24] or self.cadena[j][i] == self.codones_existentes[25] or\
					self.cadena[j][i] == self.codones_existentes[26] or self.cadena[j][i] == self.codones_existentes[27]:
						self.proteina.append(abreviacion_proteinas[7])	

					elif self.cadena[j][i] == self.codones_existentes[28] or self.cadena[j][i] == self.codones_existentes[29] or\
					self.cadena[j][i] == self.codones_existentes[30] or self.cadena[j][i] == self.codones_existentes[31]:
						self.proteina.append(abreviacion_proteinas[8])

					elif self.cadena[j][i] == self.codones_existentes[32] or self.cadena[j][i] == self.codones_existentes[33]:
						self.proteina.append(abreviacion_proteinas[9])

					elif self.cadena[j][i] == self.codones_existentes[34] or self.cadena[j][i] == self.codones_existentes[35]:
						self.proteina.append(abreviacion_proteinas[10])

					elif self.cadena[j][i] == self.codones_existentes[36] or self.cadena[j][i] == self.codones_existentes[37]:
						self.proteina.append(abreviacion_proteinas[11])

					elif self.cadena[j][i] == self.codones_existentes[38] or self.cadena[j][i] == self.codones_existentes[63]: #Linea Editada "He extraido este fragmento or self.cadena[j][i] == self.codones_existentes[39]"
						self.proteina.append(abreviacion_proteinas[12])

					elif self.cadena[j][i] == self.codones_existentes[40] or self.cadena[j][i] == self.codones_existentes[39]: #Linea editrada, agregado "or self.cadena[j][i] == self.codones_existentes[39]""
						self.proteina.append(abreviacion_proteinas[13])

					elif self.cadena[j][i] == self.codones_existentes[42] or self.cadena[j][i] == self.codones_existentes[41] : #Linea editada, retiramos "or self.cadena[j][i] == self.codones_existentes[43]"
						self.proteina.append(abreviacion_proteinas[14])

					elif self.cadena[j][i] == self.codones_existentes[44] or self.cadena[j][i] == self.codones_existentes[43]: #Linea editada, retiramos #or self.cadena[j][i] == self.codones_existentes[45]
						self.proteina.append(abreviacion_proteinas[15])

					elif self.cadena[j][i] == self.codones_existentes[46] or self.cadena[j][i] == self.codones_existentes[45]: # Linea editada, introducimos or self.cadena[j][i] == self.codones_existentes[45], linea retirada or self.cadena[j][i] == self.codones_existentes[47] or
						self.proteina.append(abreviacion_proteinas[16])

					elif self.cadena[j][i] == self.codones_existentes[47] : #Extraemos or self.cadena[j][i] == self.codones_existentes[48]
						self.proteina.append(abreviacion_proteinas[17])

					elif self.cadena[j][i] == self.codones_existentes[49] or self.cadena[j][i] == self.codones_existentes[50] or\
					self.cadena[j][i] == self.codones_existentes[51] or self.cadena[j][i] == self.codones_existentes[54] or\
					self.cadena[j][i] == self.codones_existentes[55] or self.cadena[j][i] == self.codones_existentes[48] :#Extraemos "or self.cadena[j][i] == self.codones_existentes[56]", introducimos or self.cadena[j][i] == self.codones_existentes[48]
						self.proteina.append(abreviacion_proteinas[18])

					elif self.cadena[j][i] == self.codones_existentes[57] or self.cadena[j][i] == self.codones_existentes[58] or\
					self.cadena[j][i] == self.codones_existentes[59] or self.cadena[j][i] == self.codones_existentes[60] or\
					self.cadena[j][i] == self.codones_existentes[56]: #"insertamos or self.cadena[j][i] == self.codones_existentes[56]"
						self.proteina.append(abreviacion_proteinas[19])	
					else:
						print("el elemento no es un triplete hay algún error")  # Esto para poder verificar si no se está cumpliendo algo y revisarlo
				
				except IndexError:
					pass
			print("codon de prueba", self.codones_existentes[1])
            print("cadena", self.cadena)
            self.proteinaFinal.append(self.proteina)
            print(self.proteina)
            self.proteina = []  # Reinicamos luego de cada iteracion
            print("/n")
            print("proteina final", self.proteinaFinal)
			#self.proteinaFinal.append(self.proteina) "originales del codigo"
			#self.proteina = []  # Reinicamos luego de cada iteracion "originales del codigo"
		return self.proteinaFinal  # Esto para poder asignarlo al momento de leer un archivo

class ARNt():
	def __init__(self,cadena):
		self.cadena = cadena
		self.final = []  # Este objeto tendrá una cadena vacía para almacenar los aminoacidos que encuentre hasta el primer stop
		#self.basura = []  # Variable donde almacenaremos ADNbasura
		self.ARNbasura = []  # Variable donde almacenamos ARNbasura
		self.final2 = []  # Aquí se almacenarán cada cadena por separado
	def traducir(self):
		codon = ""  # Inicializamos aquí la variable que almacenará cada codon luego de una futura iteracion

		# Almacenamos todos los aminoacidos que existen
		codones_existentes = ["AUG","UUU","UUC","UUA","UUG","CUU","CUC","CUA","CUG","AUU","AUC","AUA","GUU","GUC","GUA","GUG",\
		"UCU","UCC","UCA","UCG","CCU","CCC","CCA","CCG","ACU","ACC","ACA","ACG","GCU","GCC","GCA","GCG","UAU","UAC","CAU","CAC",\
		"CAA","CAG","AAU","AAA","AAG","GAU","GAC","GAA","GAG","UGU","UGC","UGG","CGU","CGC","CGA","CGG","AGU","AGC","AGA","AGG",\
		"GGU","GGC","GGA","GGG","UAG","UAA","UGA","AAC"]

		frecuencia = []  # Frecuencia en la que aparecen los aminoacidos
		#frecuencia1 = []


		for i in range(len(codones_existentes)):  # Todos están inicialmente en cero
			frecuencia.append([0,codones_existentes[i]])

		# Primero formaremos el aminoacido de inicio
		try:

			for i in range(3):
				codon = codon + self.cadena[i]
		except IndexError:
			pass		
		

		if codon != codones_existentes[0]:  # En caso de que no tenga codon de iniciacion
			for i in range(len(self.cadena)): # Como nos pide devolver ADN basura entonces hay que devolver el cambio "U", "T"

				if self.cadena[i] == "U":
					self.cadena[i] = "T"	

			#self.basura.append(self.cadena)
			global ADNbasura
			
				
		else:  # Buscamos si es o no es ARN basura
			basura = True # Esta variable servirá para que si al final de esta iteracion sea clasificada o no como basura
			# Inicialmente se asume que es basura
			contador = True  # Otra condicion de verificación


			i = 3  # Variable para trabajar con un ciclo while

			"""
			originalmente se pensaba en un bucle for, pero como no se sabe exactamnte si la cadena de los casos de prueba
			son divisible entre 3, se decidió hacer un bucle while.
			"""
			while i < len(self.cadena):  # Subimos la iteracion de 3 en 3. Esto por la forma en que se hace el aminoacido

				codon = "" # Reiniciamos la variable de codon
				try:

					for j in range(i,i+3):  # Para crear el triplete a comparar
						codon = codon + self.cadena[j]

				except IndexError:
					break
				print(codon)
				if (codon == codones_existentes[60]) or (codon == codones_existentes[61]) or (codon == codones_existentes[62]):
					#codon = ""  # Reiniciamos esta variable
					codon2 = ""
					print("prueba", codones_existentes[60])
					i = i + 3	
					try:

						for j in range(i,i+3):
							codon2 = codon2 + self.cadena[j]
					except IndexError:
						pass  # Si este error surge, quiere decir que estamos en el último aminoacido			

					if codon2 != codones_existentes[0]:
						#i = i + 3  # En caso contrario ajustamos la variable de iteracion
						self.final2.append(self.final)  # Agregamos lo que tenemos tal como una protetina sin sintetizar
						
						self.final = []  # Reiniciamos
						
					else: 
						codon = "" 
						self.final2.append(self.final)  # Agregamos lo que tenemos tal como una protetina sin sintetizar
						self.final = []  # Reiniciamos

				else:  # Agregamos el aminoacido y la frecuencia
					for z in range(len(codones_existentes)):
						if codones_existentes[z] == codon:
							frecuencia[z][0] = frecuencia[z][0] + 1  # Agregamos la frecuencia 

					if codon != "": # Esta condicion permite que no se agreguen elementos vacios
						self.final.append(codon)  # Agregamos el elemento a la cadena de codones

				i = i + 3  # Ajustamos la variable de iteracion

			if basura and contador == True:  # En caso de que haya terminado de iterar y no haya encontrado un aminoácido de culminación
				for i in range(len(self.cadena)): # Como nos pide devolver ADN basura entonces hay que devolver el cambio "U", "T"

					if self.cadena[i] == "U":
						self.cadena[i] = "T"
						

				#self.basura.append(self.cadena)
				#if self.final
				ADNbasura.append(self.cadena)
				self.ARNbasura.append(self.final)
				#print(ADNbasura)
				self.final = []  # Aseguramos que no quede nada			

			else:
				self.final2.append(self.final)
				self.final = []

		global frecuencia1
		print("1",frecuencia1, "\n")
		#print("0",frecuencia, "\n")
		for f in range(len(frecuencia)):
			#print("esta es la iteranci[on:",f,frecuencia[f][0])
			if frecuencia[f][0] != 0:
				frecuencia1.append(frecuencia[f])
		Heapsort(frecuencia1)
		#print("esta es la frecuencia:",frecuencia1)
		return self.final2  # Se hace un return aquí para poder hacer la lectura de archivos sin que devuelva None

def creaciontxt(nombre,variable):  # Para la clase contenedora
	with open (nombre + ".txt","a") as f:
		for i in range(len(variable)):
			temporal = ""  # Alamcenaremos todos los elementos de cada lista aquí

			for j in range(len(variable[i])):
				temporal = temporal + variable[i][j]

			f.write(temporal + "\n")

class Contenedora():

	def __init__(self,cadena):
		self.cadena = cadena

	#def GuardarAdnsimple(self):
	#	creaciontxt(self.completar)
	#	print(self.completar)

	#def GuardarAdndoble(self):
	#	creaciontxt(self.busqueda)
	#	print(self.busqueda)


	def GuardaADNBasura(self): #Editado, exceso de prints
		global ADNbasura
		z = mergesort(ADNbasura)
		creaciontxt("ADNbasura", z) 


	def GuardaFrecuCodon(self):
		frecuencia2 = []
		global frecuencia1
		#print(frecuencia1)
		for i in range(len(frecuencia1)):
			y = ""
			for j in range(len(frecuencia1[i])):
				frecuencia1[i][j] = str(frecuencia1[i][j])
				y = y + frecuencia1[i][j]
				y = y + "-"
			frecuencia2.append(y)
		creaciontxt("Frecuencia Codon", frecuencia2)	

	def GuardaAminoacid(self):
		arreglo_vacio = []
		for i in range(len(self.cadena)):
			for j in range(len(self.cadena[i])):
				temporal = len(self.cadena[i][j])
				salida = [temporal,self.cadena[i]]
				arreglo_vacio.append(salida)
		Heapsort(arreglo_vacio)

		vacio_2 = []
		for i in range(len(arreglo_vacio)):

			vacio_2.append(arreglo_vacio[i][1])
			vacio_2[i] = str(vacio_2[i])
		creaciontxt("Aminoacidos ordenados", vacio_2)
		return(vacio_2)



	
		

# Casos de prueba simples con existo
prueba = lectura_archivo("aciditos.txt")
prueba2 = leerAminoacidos("aciditos.txt")
prueba3 = SintetizarProteinas("aciditos.txt")
prueba4 =[]
#
for i in range (len(prueba3)):
	prueba3[i]=str(prueba3[i])
prueba4.append(prueba3) #Tab eliminado "linea modificada"
creaciontxt("Proteinas sintetizadas",prueba4)	

print("Buenas, la manera de ejecucion es la siguiente:","\n" )
print("Se edita peurba, para probar las funciones de sisntesis de proteinas, leer aminoacidos y leer archivos")
print("Luego quedan almacenados en la carpatea donde se ha guardado este proyecto")

print("Estas son las proteinas sintetizadas","\n",prueba3)

hola1 = Contenedora(prueba2)
hola1.GuardaFrecuCodon()
hola2 = Contenedora(prueba2)
hola2.GuardaADNBasura()
#hola3 = Contenedora(prueba2)
#hola3.GuardaAminoacid()



