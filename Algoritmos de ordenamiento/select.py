from math import floor
import math
import time
import random

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
