"""
Nombres: Gaspar Hermán, Jesús Marcano Carnets: 13-10637 12-10359

Fecha: 23/04/2016

Descripcion:2
Las listas referidas anteriormente se muestran a continuación:
Los componentes que se encuentran en el laboratorio =[4,20,5,5,10,6,7,8,16,9,11,14,5]
Los componentes que la profesora necesita saber si se encuentran en el laboratorio =[4,7,8,9,14]
Como la profesora está muy apurada, deberán implementar el algoritmo de búsqueda que,
en general, sea más eficiente para esta tarea. Por otro lado la profesora desea comparar el
funcionamiento de los 3 algoritmos de ordenamiento (inserción, burbuja y selección) en dicho
problema, por lo que sus estudiantes deberán implementar los 3 algoritmos.
Deberán existir entonces tres archivos:
En el archivo lab01Ejer2B.py debe de estar implementada la solución del problema con
el Ordenamiento Burbuja.
En el archivo lab01Ejer2I.py debe de estar implementada la solución del problema con
el Ordenamiento por Inserción.
En el archivo lab01Ejer2S.py debe de estar implementada la solución del problema con
el Ordenamiento Selección.
Como la profesora se guía por el libro del curso, dichas implementaciones deberán de ser según
el pseudocódigo del Kaldewaij encontrado en este link: http://chimo.ldc.usb.ve/ProgrammingTheDerivationOfAlgorithms.pdf.
Es decir, no se podrá usar ningún otro pseudocodigo.
"""
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