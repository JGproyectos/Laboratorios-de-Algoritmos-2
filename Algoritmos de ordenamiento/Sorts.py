from math import floor
import math
import time
import random

a = [31,41,59,26,41,58]

"""
En este apartado comienza 

		############ INSERTION-SORT###########33
"""		

def InsertionSortUPPER(A,p,r):	
	print(p)

	print(r)

	for j in range (p,r+1):
		key = A[j]
		i = j-1
		while i >= p and A[i] > key:
			A[i+1], A[i] = A[i], A[i+1]
			i = i - 1
		A[i+1] = key
	return(A)

#print(InsertionSortUPPER(a,0,5))

def InsertionSortLOWER(A,p,r):	
	print(p)

	print(r)

	for j in range (p,r+1):
		key = A[j]
		i = j-1
		while i >= p and A[i] < key:
			A[i+1], A[i] = A[i], A[i+1]
			i = i - 1
		A[i+1] = key
	return(A)

"""
En este apartado FINALIZA 

		############ INSERTION-SORT###########33
"""		


"""
En este apartado comienza 

		############ SELECTION-SORT###########33
"""		
def SelectionSort(A,p,r):

	for j in range(p,r):
		key = A[j]
		h = j + 1
		for i in range(h,len(A)):
			if A[i] < A[j]:
				A[i] , key = key, A[i]
				A[j] = key
			elif A[i] > A[j]:
				pass
		print(A)
	return A

print(a)
print("\n")
print(SelectionSort(a,0,5))

"""
En este apartado FINALIZA 

		############ SELECTION-SORT###########33
"""		

			

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
def QuickSort(arreglo,primer,ultimo):
  global aritmeticas
  aritmeticas = aritmeticas + 2
  if primer < ultimo:
    global comparacion
    comparacion = comparacion + 1
    global asignacion
    asignacion = asignacion + 1
    q = particionRandomizada(arreglo,primer,ultimo)

    QuickSort(arreglo,primer,q - 1)
    QuickSort(arreglo,q + 1,ultimo)


def particionRandomizada(arreglo,primer,ultimo):
  global asignacion

  asignacion = asignacion + 1 
  i = random.randrange(primer,ultimo)
  asignacion = asignacion + 1
  arreglo[i],arreglo[ultimo] = arreglo[ultimo],arreglo[i]
  q = particion(arreglo,primer,ultimo)

  return q

def particion(arreglo,primer,ultimo):
  global asignacion
  global comparacion
  global logicas
  global aritmeticas

  asignacion = asignacion + 1
  x = arreglo[primer]
  asignacion = asignacion + 2
  izquierdo = primer + 1
  derecho = ultimo

  while True:
 
    comparacion = comparacion + 1
    logicas = logicas + 1 
    while izquierdo <= derecho and arreglo[izquierdo] <= x:
      
      asignacion = asignacion + 1
      aritmeticas = aritmeticas + 1
      izquierdo = izquierdo + 1

    comparacion = comparacion + 1
    logicas = logicas + 1 
    while arreglo[derecho] >= x and derecho >= izquierdo:
      derecho = derecho - 1
      asignacion = asignacion + 1
      aritmeticas = aritmeticas + 1

    if derecho < izquierdo:
      break

    else:
      arreglo[izquierdo],arreglo[derecho] = arreglo[derecho],arreglo[izquierdo]
      asignacion = asignacion +  1

  arreglo[primer],arreglo[derecho] = arreglo[derecho],arreglo[primer]
  asignacion = asignacion + 1


  ##############FINDELQUICKSORT#######################

###############HEAPSORT############################

### con este ordenaremos el arreglo ###
def Heapsort(A):
    n = len(A)
    BuildHeap(A)
    for i in range(n-1, 0,-1):
        var = A[0]
        A[0] = A[i]
        A[i] = var
        Heapify(A, 0 , i)


def BuildHeap(A): # funcion para crear el arbol
    n = len(A)
    for i in range((n//2)-1, -1,-1):
        Heapify(A, i , n)
        
        
        
def Heapify(A, j, x):#intercambio de orden de los hijos y padres
    largest = j
    left = 2*j +1
    right = 2*j + 2
    
    
    if left < x and A[left]> A[j]:
        largest = left 
    if right < x and A[right] > A[largest]:
        largest = right
    if largest != j:
        var = A[j]
        A[j] =  A[largest] 
        A[largest] = var 
        Heapify(A, largest, x)

  return derecho




##############FIN DEL HEAPSORT#############

##############POO#########################3

class Canvas:
	
	# Inicializando los atributos
	def __init__(self, largo, alto):
		self.largo = largo
		self.alto = alto
		matriz =[]  # Almacenamos los - en esta matriz vacía al iniciarse
		matriz2 = [] # Para después almacenar matriz aquí
		for i in range(largo):
			for j in range(alto):
				matriz.append("-")
			matriz2.append(matriz)
			matriz = []  # Reiniciando la matriz
		self.matriz = matriz2
	
	# Generando los metodos
	def setpixel(self,largo,alto):
		self.matriz[largo][alto] = "*"  # Colocamos esto en la posicion
		
	def getpixel(self, largo, alto):
		return self.matriz[largo][alto]
		
	def get_todo(self):
		return self.matriz
		
	def deletepixel(self, largo, alto):
		self.matriz[largo][alto] = "-"
		
	def salida(self):
		matriz_otra = self.matriz
		for i in range(len(matriz_otra)):
			for j in range(len(matriz_otra)):
				print(matriz_otra[i][j],end = "  ")
			print("\n") 
				  
				  
class Rectangulo:
	
	def __init__(self,SupIzq,SupDer,InfIzq,InfDer):
		self.SupIzq = SupIzq
		self.SupDer = SupDer
		self.InfIzq = InfIzq
		self.InfDer = InfDer
		
		LenAlt = SupIzq - SupDer
		LenLar = SupIzq - InfIzq

	def pintar(self,SupIzq,SupDer,InfIzq,InfDer,otra):
		for i in range(SupIzq, SupDer + 1):
			for j in range(InfIzq, InfDer + 1):
				
				otra.setpixel(i,j)
				
class Cuadrado(Rectangulo):

	def __init__(self,SupIzq,SupDer,tam):

		Rectangulo.__init__(self,SupIzq,SupDer,tam +SupIzq , tam + SupDer)
		



		#self.InfIzq = self.SupIzq + tam  # Para igual distancia
		#self.InfDer = self.SupDer + tam  # Para igual distancia
		#global esquina1
		#esquina1 = self.InfIzq
		#global esquina2
		#esquina2 = self.InfDer
			
# Ingreso de datos
alto = input("ingrese el alto de la matriz ")
alto = int(alto)  # Se trata como numero
ancho = input("ingrese el ancho de la matriz ")
ancho = int(ancho)  # Se trata como numero

# Creamos el objeto                    
otra = Canvas(alto,ancho)
rec = Rectangulo(0,3,4,5)
cuad = Cuadrado(0,3,3)
#rec.pintar(0,3,4,5,otra)
cuad.pintar(0,3,0,3,otra)
otra.salida() 
#########333 FIN DE POO ###############

#########Bubblesort#################

# Definimos nuestras funciones
def busqueda_binaria(arreglo:list,valor:int)->int:
	inicio = 0
	final = len(arreglo) - 1

	while inicio <= final:
		medio = (inicio + final) // 2

		if arreglo[medio] < valor:
			inicio = medio + 1 

		elif arreglo[medio] > valor:
			final = medio - 1 

		else:
			return medio

def bubble_sort(arreglo:list)->list:
	# Precondicon
	assert(all(isinstance(arreglo[i],int) for i in range(len(arreglo)-1)))

	# Algoritmo de ordenamiento (Bubble Sort)
	n = 0 # Para el bucle
	b = False  # Para usarlo en un bucle condicional

	while n != len(arreglo) and (not b):  # Permite actualizar el n del seugndo bucle
		k = len(arreglo) - 1
		b = True  # Usado para terminar de iterar 

		while k != n:  # Este bucle permite tomar el primer par que se arrastrará

			if arreglo[k - 1] > arreglo[k]:  # Intercambia los componentes
				b = False
				arreglo[k - 1],arreglo[k] = arreglo[k],arreglo[k - 1]

			# Ajustamos la variable de iteración
			k = k - 1

		n = n + 1	

	# Postcondicion
	assert(all(arreglo[i] <= arreglo[i+1] for i in range(len(arreglo)-1)))
	return arreglo

# Datos iniciales	
componentesActuales = [40,20,5,5,10,6,7,8,16,9,11,14,5]
componentesBuscar = [4,7,8,9,14]

componentesActuales = bubble_sort(componentesActuales) # Reasignamos su valor pero ahora ordenado

print("los componentes ordenandos son: ",componentesActuales)
print("los componentes a buscar son: ",componentesBuscar)

for i in range(len(componentesBuscar)):
	valor = busqueda_binaria(componentesActuales,componentesBuscar[i])

	# Condicion de salida
	if valor != None:
		print("el elemento ",componentesBuscar[i]," está en la lista y su posicion es: ",valor)

	else:
		print("el elemento ",componentesBuscar[i]," no está en el laboratorio")	

###### fin del bubble #############

######Insertion############

def insertion(arreglo:list)->list:
	n = 1

	while n != len(arreglo):

		k = n
 
		while k != 1 and arreglo[k-1] > arreglo[k]:
			arreglo[k-1],arreglo[k] = arreglo[k],arreglo[k-1]
			k = k - 1

		if arreglo[0] > arreglo[1]:
			arreglo[0],arreglo[1] = arreglo[1],arreglo[0]

		n = n + 1
	# Postcondicion
	assert(all(arreglo[i] <= arreglo[i+1] for i in range(len(arreglo)-1)))
	return arreglo	

# Datos iniciales	
componentesActuales = [40,20,5,5,10,6,7,8,16,9,11,14,5]
componentesBuscar = [4,7,8,9,14]

componentesActuales = insertion(componentesActuales) # Reasignamos su valor pero ahora ordenado

print("los componentes ordenandos son: ",componentesActuales)
print("los componentes a buscar son: ",componentesBuscar)

for i in range(len(componentesBuscar)):
	valor = busqueda_binaria(componentesActuales,componentesBuscar[i])

	# Condicion de salida
	if valor != None:
		print("el elemento ",componentesBuscar[i]," está en la lista y su posicion es: ",valor)

	else:
		print("el elemento ",componentesBuscar[i]," no está en el laboratorio")
		
############### Fin del Insertion##############

########## selectionSort ###########

def seleccion(arreglo:list)->list:
	n = 0
	ComponentesOrdenados= []
	while n != len(arreglo):
		a = n
		b = len(arreglo)-1
		print(arreglo[b])
		#print(arreglo[b])
		while a != b:
			if arreglo[a] >= arreglo[b]:
				b = b - 1
				ComponentesOrdenados.append(arreglo[a])
			else:
				a = a + 1

		#arreglo[n] = arreglo[a]
		n = n + 1
	
	#print(ComponentesOrdenados)
	return arreglo

# Datos iniciales	
componentesActuales = [40,20,5,5,10,6,7,8,16,9,11,14,5]
componentesBuscar = [4,7,8,9,14]

componentesActuales = seleccion(componentesActuales) # Reasignamos su valor pero ahora ordenado	
print("los componentes ordenandos son: ",componentesActuales)	

#######fin de select############

#############CountingSort "con fallas"################

"""
def CountingSort(A, B):
    k = max(A)
    C=[]
   
    for i in range(len(A)):
        B.append(0)
       
       
    for i in range(0,k+1):
        C.append(0)
   
    for j in range(len(A)):
        C[A[j]] = C[A[j]] + 1
        print(C)

    print("\n")
    for i in range(k):
    	if i == 0 :
    		C[i] = C[i] + C[i-1]
        #print(C)

    try:

	    for j in range(len(A)-1,0,-1):
	   
	        B[C[A[j]]] = A[j]
	        C[A[j]] = C[A[j]] - 1  
    except:
    	pass
    #print(C)
    return B

a = CountingSort(A, B)  
print(a)
print (B)
"""
#####3 Fin del counting ###########

###### Colas de prioridad #########

class ColaDePrioridad():
	def __init__(self):
		self.Cola = []
		
	
	def eliminar(self):
		del self.Cola
		
	def AgregarElem(self,p,k):
		tupla = (p,k) 
		self.Cola.append(tupla)

		
	def ConsultarMax(self):
		BuildaHeap(self.Cola)
		a = self.Cola[0,0]
		print(a)
		
	def ExtraerMax(self):
		BuildHeap(self.Cola)
		a = self.Cola[0]
		self.Cola.pop(0)
		print("se ha eliminado el elemento:", a)
		
	def eliminarelemento(self,p):
## No terminada####

############Randomize Select###########

def RandomizeSelect(A,p,r,i):
    if p == r:
        print("El elemento que estaba buscando es el siguiente:")
        return A[p]
    q = RandomizePartition(A,p,r)
    k = q-p+1
    if i == k:
        return A[q]
        
    elif i<k:
        return RandomizeSelect(A,p,q-1,i)
    else:
        return RandomizeSelect(A,q+1,r,i-k)

def RandomizePartition(A,p,r):
    try:
        i = random.randrange(p,r)
        A[i], A[r] =A[r], A[i] 
    except ValueError:
        pass
        
    return Partition(A,p,r)


def Partition(A,p,r):
    try:
        x = A[r]
        i = p-1
    except IndexError:
        r = len(A) 
        x = A[r]
        i = p-1
        if i < 0:
            i = 0
    for j in range(p,r):
        if A[j] <= x:
        
            i = i+1
            
            A[i],A[j]= A[j],A[i]
    try:
        A[i+1],A[r] =A[r],A[i+1]
    except IndexError:
        pass
    
    print("arreglo particionado: ",A, "el pivote es: ", A[i+1])
    return i+1



A= []
for i in range(100):
	b = random.randrange(1,101)
	if b not in A:
		A.append(b)

print(A)
tiempo1 = time.time()
print(RandomizeSelect(A,0,len(A)-1,9))
tiempo2 = time.time() - tiempo1
print(tiempo2)
 ################ fin###############

 #############Select################

def Partition(A,p,r):
   try:
       x = A[r]
       i = p-1
   except IndexError:
       r = len(A) 
       x = A[r]
       i = p-1
       if i < 0:
           i = 0
   for j in range(p,r):
       if A[j] <= x:
       
           i = i+1
           
           A[i],A[j]= A[j],A[i]
   try:
       A[i+1],A[r] =A[r],A[i+1]
   except IndexError:
       pass
   
   print("arreglo particionado: ",A, "el pivote es: ", A[i+1])    
   return i+1

"""                        
datos = [4,5645,8788,2,52,78785,5548,547,47,5]
Heapsort(datos)
print(datos)
"""

def Select(A,p,r,i):
    N = len(A)
    if r - p + 1 <= N:      #constante a determinar
        Heapsort(A)
        return A[i]

    ###Calculo de medianas###

    l = math.ceil((r-p+1)/5)
    M = [0 for x in range(l)] #arreglo que almacenará las medianas
    for j in range(l):
        u = min(p + 5 * j + 4,r)
        Heapsort(A)
        M[j+1] = A[((p + 5*j + u)//2)+1]
    x =  Select(M,1,l,(l//2)+1)
    q =  Partition(A,p,r)
    k = q - p + 1
    if i == k:
        return A[q]
    elif i < k:
        return Select(A,p,q-1,i)
    else:
        return Select(A,q+1,r,i-k)

A= []
for i in range(100):
	b = random.randrange(1,101)
	if b not in A:
		A.append(b)
tiempo1 =time.time()
Select(A,0,len(A)-1,9)
tiempo2 = time.time() - tiempo1
print(tiempo2)

######## fin #######################################

############Merge#############33333
def Merge(A,p,q,r):
	print("Q es igaul a :",q)
	print("r es igaul a :",r)
	n = q - p + 1
	m = r - q - 1
	print("El tama;o de L es:", n)
	print("El tama;o e R es:",m)

	L = [] #arreglo que contiene la primera mitad del  los que estan por ordenarse
	R = []# segunda mitad
	for i in range (0,n):
		L.append(A[p+i])

	for j in range(0,m):
		R.append(A[q+j + 1])

	print("L):",L)
	print("R):", R)
	

	i, j = 0,0

	for k in range(0,6):

		if i < n and j < m:
			if L[i] <= R[j]:
				A[k] = L[i]
				i = i + 1
			else:
				A[k] = R[j]
				j = j + 1
			print("1:",A)

		else:
			if i >= n:
				for g in range(j,m):
					A[k] = R[g]
					k = k + 1
					print("algo1")
			elif j >= m:
				for g in range(i,n):
					A[k] = L[g]
					k = k + 1
					print(L[g])
					print("algo2")
			break

		
		print("\n")
	return(A)
		
		

A = [3,27,38,43,80,90,100]
l = len(A) 
h = (len(A)//2) 
print(Merge(A,0,h,l))
####################Fin del Merge##############