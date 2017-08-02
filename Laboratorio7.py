"""
Nombres: Gaspar Hermán, Jesús Marcano	carnets: 13-10637,12-10359

Fecha: 09/06/2016/

Descripcion: Laboratorio7
"""
# Creando las clases 
class Piso():
	def __init__(self,top):
		self.lista = []  # Cada vez que se cree una pila(piso) este debe de estar vacío
		self.capacidad = top  # Este será el tamaño máximo que podrá recibir la pila 
		self.ocupacion = 0 # Cada vez que se inicialice estará vacío
		self.piso_cerrado = []  #  Pisos cerrados
		self.espacio = True  # Se almacenan si hay espacio o no en el piso, se asume cierta por defecto

	def estacionar(self,elemento):
		if self.ocupacion < self.capacidad:
			#print("\n")
			self.lista.append(elemento)  # Agregamos el elemento a la lista
			self.ocupacion = self.ocupacion + 1  # Aquí agregamos un nuevo elemento

	def retirar(self):
			if len(self.lista) != 0:
				self.ocupacion = self.ocupacion - 1  # Se resta para que quede el espacio libre
				print("se retiró el elemento: ",self.lista[len(self.lista)-1])
				self.lista.pop()
				

	def cercano(self,piso):
			if len(self.lista) != 0:
				return self.lista[len(self.lista) -1]
			
			else:
				return None

	def cabe(self):
		if self.ocupacion < self.capacidad:
			return True

		else:
			return False


class Estacionamiento():
	"""docstring for Estacionamiento"""
	def __init__(self):
		self.piso_cerrado = []  #  Pisos cerrados
		self.piso = 0  # Contador que para saber cuantos pisos se tienen

	def insertar_piso(self, EL_):
		self.piso.append(EL_)

	def sacar_piso(self):
		return self.piso.pop(0)

	def Estacionar(self, vehiculo, variable,texto):  # Variable es el objeto piso y vehiculo es un objeto completo
		if variable.ocupacion < variable.capacidad:  # Evaluamos
			variable.estacionar(vehiculo)

			with open(texto,"a") as f:
				f.write("\n")
				f.write("P" + "\t" + str(vehiculo.placa) + "\t" + str(vehiculo.longitud) + " \t" + str(vehiculo.marca) + "\t" + str(vehiculo.anyo) + "\t" + str(vehiculo.color))
				f.write("\n")
				f.write("--> Entra vehiculo "+ str(vehiculo.placa) + " de longitud " + str(vehiculo.longitud))
				f.write("\n")
				f.write("--> Se estaciona vehiculo " +str(vehiculo.placa) + " en tubo " + str(self.piso) + " (ocupacion  " + str(variable.ocupacion) + ")")
				f.write("\n")

		else:
			self.piso_cerrado.append(variable.lista)  # Guardamos el piso cerrado
			self.piso = self.piso + 1  # Como creamos un nuevo piso le sumamos 1
			variable.lista = []  # Reiniciamos los datos
			variable.ocupacion = 0 


			with open(texto,"a") as f:
				f.write("\n")
				f.write("P" + "\t" + str(vehiculo.placa) + "\t" + str(vehiculo.longitud) + " \t" + str(vehiculo.marca) + "\t" + str(vehiculo.anyo) + "\t" + str(vehiculo.color))
				f.write("\n")
				f.write("--> Entra vehiculo "+ str(vehiculo.placa) + " de longitud " + str(vehiculo.longitud))
				f.write("\n")
				f.write("--> Capacidad de Tubo "+ str(self.piso - 1) + " Excedida ")
				f.write("\n")


			with open(texto,"a") as f:
				f.write("--> Se crea tubo " + str(self.piso) + " de capacidad 5 y ocupacion " + str(variable.ocupacion))
				f.write("\n")
				f.write("--> Se coloca Tubo" + str(self.piso) + " de ultimo en la cola de tubos de Tolon")
				f.write("\n")
				f.write("--> Se corren los tubos hasta que " + str(self.piso) + "hasta que el tubo " + str(self.piso) + " sea el primero")
				f.write("\n")
				f.write("--> Se estaciona vehiculo " +str(vehiculo.placa) + " en tubo " + str(self.piso) + " (ocupacion  " + str(variable.ocupacion + 1) + ")")
				f.write("\n")
			variable.estacionar(vehiculo)  # Lo agregamos

	def VaciarTodo(self,piso,texto):  # Esto vaciará todos los pisos cerrados en orden. piso1 es para poder usar el método de la pila del piso
		self.piso_cerrado.append(piso.lista)  # Colocamos el último piso activo 

		with open(texto,"a") as f:
			f.write("\n")
			f.write("K Bye Bye")
			f.write("\n")
			f.write("--> Se vacían los pisos en orden")

			for i in range(len(self.piso_cerrado)):
				f.write("\n")
				f.write("\n")
				f.write("--> Piso "+ str(i + 1))
				f.write("\n")

				for j in range(len(self.piso_cerrado[i])-1,-1,-1):
					f.write("<-- Sale Vehiculo "+ str(self.piso_cerrado[i][j].placa))
					f.write("\n")

			f.write("\n")
			f.write("\n")

		for i in range(len(self.piso_cerrado)):
			self.piso_cerrado.pop()
			self.piso = self.piso - 1

		with open(texto,"a") as f:
			f.write("--> Se destruyen estacionamiento, tubos y vehiculos remanentes")
			f.write("\n")
			f.write("--> Adios")

	def Retirar_Piso(self,variable):
		for i in range(len(variable)):
			for j in range(len(variable[i])):
				variable[i].pop(j)

	def Destruir_Piso(self):
		self.piso_cerrado.pop(0)

	def Vaciar_Cerrados(self):
		if len(self.piso_cerrado) != 0:
			Retirar_Piso(self.piso_cerrado)


class vehiculo():
	def __init__(self,arreglo):  # Guardamos las caracteristicas del objeto
		self.placa = arreglo[0]
		self.longitud = arreglo[1]
		self.marca = arreglo[2]
		self.anyo = arreglo[3]
		self.color = arreglo[4] 

		"""
		nota: originalmente esta funcion recibia 4 parametros, uno para cada atributo
		pero cuando se creaba la función de lectura de texto, para simplificar el trabajo
		se decidió cambiar todos los parametros de entraba por un arreglo y asignar a cada 
		atributo una posición del arreglo.
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

	for i in range(len(y)):  # Borrar los tabuladores en caso de que tenga
		for j in range(len(y[i])):
			if "\t" in y[i]:
				y[i] = y[i].replace("\t"," ")		  

	return y

"""
Esta función lo que hará será: llamar a borrar espacios, luego de eso ver cada una de las letras que tiene en el elemento cero
y seguir instrucciones como: crear el objeto carro y estacionarlos
"""

def lecturaDeDatos(archivo):
	# Precondicion
	assert(isinstance(archivo,str))  # Garantizamos que se ingrese un string

	contenedora = borrar_espacios(archivo)  # Esta variable tiene el archivo leído
	global carros
	carros = []  # Variable que almacenará todos los carros antes de convertirlos en objetos

	for i in range(len(contenedora)):  # Convertiremos cada elemento de la lista en una lista a partir de los espacios
		contenedora[i] = contenedora[i].split(" ")

	# Ciclo de condicionales anidados a for para saber que hacer
	for i in range(len(contenedora)):
		if contenedora[i][0] == "C":
			with open(contenedora[i][1],'w') as f:  # Simplemente por ahora hay que crear el archivo					
				f.write("C" + "\t" +  str(contenedora[i][1]))
				f.write("\n")
				f.write("->" + " Se crea Estacionamiento")
				f.write("\n")
				f.write("\n")

			# En este pto debía de crearse el estacionamiento, pero por misteriosas razones más adelante no lo reconoce
			contador = True # Para verificar más adelante
				

		elif contenedora[i][0] == "P":
			carros.append(contenedora[i][1:])  # Agregamos toda esta parte de la lista a carro

		elif contenedora[i][0] == "K":
			break  # Con esto se crearán carros hasta este punto

		else:
			print("hay algún error: no se encontró ni C ni P ni K")
			return None  # Esto con la finalidad de que termine de golpe todo 

	# Postcondicion
	assert(len(contenedora) - 2 == len(carros))  # los dos elementos que no se incluyen son los de orden de inicio/fin
	texto = contenedora[0][1]
	for i in range(len(carros)):
		carros[i] = vehiculo(carros[i])  # Se convierte en un objeto llamado vehiculo
	
	# A este pto aún no se crea ningun piso para el estacionamiento por lo tanto lo creamos
	el_piso = Piso(5)  # Capacidad de carros

	if contador:
		estacionamientoPrincipal = Estacionamiento()
		#print("Se crea Estacionamiento")

	# Procedemos a estacionar
	for i in range(len(carros)):
		estacionamientoPrincipal.Estacionar(carros[i],el_piso,texto)

	# Ahora se buscará si se tiene la orden de vaciar pisos
	
	if contenedora[len(contenedora)-1][0] == "K":  # Se pregunta primero esto ya que usualmente se encuentra en el ultimo lugar
		estacionamientoPrincipal.VaciarTodo(el_piso,texto)

	else:
		for i in range(len(contenedora)):
			if contenedora[i][0] ==	"K":
					estacionamientoPrincipal.VaciarTodo(el_piso,texto)
# Inicio
entrada = input("ingrese el nombre del archivo (incluya el .txt en el nombre) ")	
lecturaDeDatos(entrada)