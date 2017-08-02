"""
Nombres: Gaspar Hermán, Jesús Marcano	Carnets: 13-10637,12-10359

Descripcion: Cliente de hash.py
"""
# Importando modulos necesarios
import Hash

# Generando el menu
while True:
	try:

		print("\t¿Qué quiere hacer?")
		print(1," Crear una tabla")
		print(2," Salir")
		n = input()
		n = int(n)  # Se trata como entero en lugar de texto

		# Precondicion
		assert(n == 1 or n == 2)

		break  # Salimos del bucle

	except:
		print("debe elegir la opcion correcta vuelva a intentarlo")
		continue

if n == 1:
	tamanio = input("ingrese el tamaño de la tabla a crear ")
	tamanio = int(tamanio)  # Se trata como un número en lugar de un texto

	tabla = Hash.Hash()  # Creamos el objeto
	tabla.crearTabla(tamanio)		

	respuesta = input("¿Quiere crear una Entrada? ")
	respuesta.lower()  # Lo volvemos todo minuscula

	if respuesta == "si":
		clave = input("ingrese la clave: ")
		clave = int(clave)  # Se trata como un entero en lugar de un string

		dato = input("ingrese el dato: ")
		dato = int(dato)  # Se trata como un entero en lugar de un string

		entrada = Hash.Entrada(clave,dato)  # Creamos el objeto
		print("para agregar esta entrada use la opción 1 que se presenta ahora")

	while True:  # Buscamos otras opciones

		print("\n")  # Linea en blanco
		print("\t¿Qué quiere hacer ahora?")
		print(0,"crear Objeto Entrada")
		print(1," agregar Objeto Entrada")
		print(2," agregar")
		print(3," buscar")
		print(4," eliminar")
		print(5," imprimir")
		print(6," Salir")

		# En caso de ingresar algo distinto
		try:

			opcion = input()
			opcion = int(opcion)  # Se trata como un entero en lugar de un texto

		except:
			print("Ha ocurrido un error, trate de nuevo")
			continue  # Volvemos al principio de la iteracion

		# Condicionales basados en la respuesta dada
		print("\n")  # Imprimimos una línea en blanco

		if opcion == 0:
			clave = input("ingrese la clave: ")
			clave = int(clave)  # Se trata como un entero en lugar de un string

			dato = input("ingrese el dato: ")
			dato = int(dato)  # Se trata como un entero en lugar de un string

			entrada = Hash.Entrada(clave,dato)  # Creamos el objeto
			print("para agregar esta entrada use la opción 1 que se presenta ahora")

		elif opcion == 1:

			try:				
				tabla.agregarelem(entrada)

			except NameError:
				print("para usar esta opción es necesario haber creado una Entrada")
				print("usted no tiene una Entrada, por favor creela y trate de nuevo")
				continue

		elif opcion == 2:

			try:

				c = input("Ingrese la clave: ")
				c = int(c)  # Se trata como un numero en lugar de texto
				d =	input("Ingrese el elemento: ")

				if d.isnumeric():  # En caso de que se ingrese un texto que pueda ser número
					d = int(d)

			except:
				print("Ha habido un error, trate de nuevo")
				continue  # Volvemos al principio de la iteración

			tabla.agregar(c,d)  # Agregamos

		elif opcion == 3:

			try:
				c = input("ingrese indice donde buscará el elemento")
				c = int(c)  # Se trata como número en lugar de texto

			except ValueError:
				print("Ha habido un error, por favor trate de nuevo")
				continue  # Volvemos a iterar
			
			busqueda = tabla.buscar(c)  # Llamamos al metodo

			print(busqueda)

		elif opcion == 4:

			try:
				c = input("ingrese indice donde buscará el elemento a borrar")
				c = int(c)  # Se trata como número en lugar de texto

			except ValueError:
				print("Ha habido un error, por favor trate de nuevo")
				continue  # Volvemos a iterar

			tabla.eliminar(c)  # Llamamos al método

		elif opcion == 5:
				tabla.imprimir()

		elif opcion == 6:
			break  # Salimos del ciclo

		else:
			print("no ha elegido ninguna opcion correcta, por favor intente de nuevo")
			continue  # Enviamos al principio de la iteración