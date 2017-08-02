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
		Heapify(A, largest, x)s	
		

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
		
		 
	
	
