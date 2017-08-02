from math import floor
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
		

                         
datos = [4,5645,8788,2,52,78785,5548,547,47,5]
Heapsort(datos)
print(datos)

