# Importando los modulos necesarios
from time import time
import random
from math import log10
# Iniciando los datos
#a = []  # Arreglo donde se guardarán los elementos a ordenar
#ordenado = []  # Arreglo final ya ordenado
#c = []  # Arreglo donde se guardarán los ceros que cuentan los elementos de otro Arreglo


#contador = 
#for i in range()

A = [10,5,5,4,4,6,3,7,7,4,15,0]
B = []
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

def Insercion(arreglo,d):
	n = 1
	maximo = max
	while n != len(arreglo):

		k = n

		while k != 0 and (((arreglo[k-1] // (10 ** d)) % 10) <= (((arreglo[k] // (10 ** d)) % 10))):
			arreglo[k-1],arreglo[k] = arreglo[k], arreglo[k-1]
			k = k - 1

		n = n + 1
	print (arreglo)
	print("\n")
	return arreglo

for i in range(5):
	def RadixSort (A):
		d = int(log10(max(A)) // 1)
		for i in (0,d+1):
			A = Insercion(A,i)
		return A		

paja = [9602,7540,959,8000,7596,841,7534,7931,3437,6871]

paja = RadixSort(paja)

# Postcondicion
#assert(all(paja[i] <= paja[i+1] for i in range(len(paja)-1)))
print(paja)