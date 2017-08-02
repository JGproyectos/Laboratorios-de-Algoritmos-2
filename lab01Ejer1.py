"""
Nombres: Gaspar Hermán , Jesús Marcano carnets: 13-10637, 12-10359

Fecha: 21/04/2016
"""

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
