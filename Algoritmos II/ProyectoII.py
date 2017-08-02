"""
Nombres: Gaspar Hermán Sandoval, Jesús Marcano	carnets:13-10637, 12-10359

Descripción: Proyecto II
paja
El misterio del robo de DACE
"""
# Importando algunos modulos
import sys
import random

# Definiendo algunas funciones
def borrar_espacios(x):  # Funcion que carga una lista en un arreglo y quita el "\n"
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
    return y

def CrearTabla(n):  # Crea una tabla vacía de tamaño 2n
	tabla = [None] * 2 * n
	return tabla

def FuncionHash1(a,k,b,p,n):  # Función para calcular posiciones de una tabla de hash
    habk = (a * k) + b  # a,b son números aleatorios < p y k es la clave a guardar
    habk = habk % p  # p es un número primo > n a 
    habk = habk % n  # n es el tamaño del arreglo

    # Postcondicion
    assert(habk <= n)  # El número calculado debe estar dentro de la tabla
    return habk   

def FuncionHash2(k,n):
    return k % n

def ASCII(palabra):
    temporal = 0  # Aquí se guardara el ASCII del numero

    for i in range(len(palabra)):
        contadorASCII = ord(palabra[i])
        temporal = temporal + contadorASCII 
    
    temporal = temporal // len(palabra)       

    return temporal  

class Persona():
    def __init__(self,nombre,documento):
        self.nombre = nombre
        self.documento = [documento]
        self.ASCII = 0  # Se guarda el ASCII aquí
        self.clave1 = 0  # Aquí se guardara una funcion de hash con su valor
        self.clave2 = 0  # Aquí se guardará otra función de hash
        self.size = 0  # Aquí se guarda el tamaño del arreglo

    def agregar(self,elemento):
        if self.size < 20:
            self.documento.append(elemento)  # Agregamos el elemento aquí
            self.size = self.size + 1  # Sumamos 1 a la cantidad de elementos que hay

        else:
            print("ERROR: memoria llena ")          

class Tabla():
    def __init__(self,n):
        self.tabla = CrearTabla(n)  # Creamos la tabla
        self.size = n  # Sacamos su tamaño (util para las funciones de hash)
        self.primo = 123455681  # Número primo lo suficientemente grande
        self.a = random.randrange(1,self.primo) # Se crea para la funcion de hash y se elige justo al crear la tabla
        self.b = random.randrange(0,self.primo)  # Igual que a y no cambia nunca
        self.personas = []  # Lista donde se almacenan las personas

    def buscar(self,nombre):
        myAscii = ASCII(nombre)

        posicion1 = FuncionHash1(self.a,myAscii,self.b,self.primo,self.size)
        posicion2 = FuncionHash2(myAscii,self.size)

        return ((self.tabla[posicion1] is not None) and (self.tabla[posicion1].nombre == nombre)) or \
               ((self.tabla[posicion2] is not None) and (self.tabla[posicion2].nombre == nombre))


    def redimensionar(self):

        """
        Esta función se llama sólo cuando es necesario cambiar el tamaño de la tabla actual
        además de que tendrá que volver a calcular varios de sus atributos y volver a colocar
        los mismos elementos que ya estaban en la tabla, en esta nueva tabla. Pero eso se hizo
        en base a una función de hash que dependía de las dimensiones de la tabla vieja.
        Se recomienda crear una tabla el doble de grande que antes.
        """    

        self.tabla = CrearTabla(2 * self.size) # Nueva tabla de tamaño doble al anterior
        self.size = len(self.tabla)

        for i in range(len(self.personas)):
            self.insertar(self.personas[i])  # Se pasa un False para ahorrar calculos, las llamadas recursivas pasan False

    
    def insertar(self,persona):  # Persona es un objeto

        if  not self.buscar(persona.nombre): # Condicion para agregar a la lista sólo una vez
            self.personas.append(persona)  # Agregamos aquí la persona

            contador = 0  # Como se transforma en un ASCII se guarda aquí

            for i in range(len(persona.nombre)):
                temporal = ord(persona.nombre[i])  # Se saca el ASCII de cada letra
                contador = contador + temporal  # Se almacena aquí

            contador = contador // len(persona.nombre)  # Sacamos la division 

            persona.ASCII = contador  # Se guarda aquí

       
            posicion1 = FuncionHash1(self.a,persona.ASCII,self.b,self.primo,self.size)
            posicion2 = FuncionHash2(persona.ASCII,self.size)
            persona.clave1 = posicion1  # Se guarda aquí este valor de la función de Hash
            persona.clave2 = posicion2  # Se guarda aquí otro valor de la función de Hash

            for i in range(self.size):  # Inserción del cuco

           
                if self.tabla[posicion1] is None:  # Si la posición está vacía lo insertamos
                    self.tabla[posicion1] = persona
                    condicion = False  # Esta condicion se usa en caso de tener que redimensionar
                    return True  # Salimos del bucle

                else:  # En caso de que la posición principal donde se quiera insertar esté vacío
                    condicion = True  # Si se está aquí al terminar de iterar, habrá que redimensionar

                    persona, self.tabla[posicion1] = self.tabla[posicion1],persona  # Intercambiamos

                    if posicion1 == persona.clave1:
                        posicion1 = persona.clave2

                    else:
                        posicion1 = persona.clave1

            if condicion:  # Entonces hay que redimensionar la tabla
                self.redimensionar()
                self.insertar(persona)  # En llamadas recursivas se pasa un False de argumento para ahorrar calculos        
            return True

        else:
            return False

        
        
"""
documento = Tabla(4)
print(documento.tabla)
arreglo = [["Gaspar","hola"],["Jose",5],["María",True],["María iguana",[1,2,3,4]]]
for i in range(len(arreglo)):
    arreglo[i] = Persona(arreglo[i][0],arreglo[i][1])

for i in range(len(arreglo)):
    documento.insertar(arreglo[i],True)
#print(documento.personas)
for i in range(len(documento.tabla)):
    if documento.tabla[i] is not None:
        print(documento.tabla[i].nombre,"\n",documento.tabla[i].clave1)
        
        print(documento.tabla[i].clave2)
        print("\n")

for i in range(len(documento.tabla)):
    if documento.tabla[i] is not None:
        print(documento.tabla[i].nombre,end = ",")

    else:
        print(None,end = ",")   
print("\n")
"""
# Lectura de datos
prueba = borrar_espacios("entrada1.txt")

# Separamos en los elementos 
for i in range(1,len(prueba)):  # No se inicia en 0 ya que ese sólo es el número de pistas
    prueba[i] = prueba[i].split()

# Creamos las tablas
documentos = Tabla(len(prueba))
pagos = Tabla(len(prueba))
pistas = ""

# Se procede a la inserción de los elementos en sus respectivas tablas de hash
for i in range(1,len(prueba)):  # Se empieza en 1 ya que el 0 es sólo un entero
    if prueba[i][0] == "doc":

        elASCII = ASCII(prueba[i][1])  # Se convierte en su elemento de la tabla
        otro2 = FuncionHash1(documentos.a,elASCII,documentos.b,documentos.primo,documentos.size)
        otro3 = FuncionHash2(elASCII,documentos.size)

        if documentos.tabla[otro2] != None: # En caso de que la tabla no está vacía 
            if documentos.tabla[otro2].nombre == prueba[i][1]:  # En caso de que esté en la primera posición de Hash
                documentos.tabla[otro2].agregar(prueba[i][2])


                for j in range(len(documentos.personas)):  # En este caso hay que agregar a esta lista
                    if documentos.personas[j].nombre == prueba[i][1]:
                        documentos.personas[j].agregar(prueba[i][2])
                        break

        if documentos.tabla[otro3] != None:

            if documentos.tabla[otro3].nombre == prueba[i][1]:  # En caso de que no esté en la primera posicion y si en la segunda
                documentos.tabla[otro3].agregar(prueba[i][2])

                for j in range(len(documentos.personas)):  # En este caso hay que agregar a esta lista
                    if documentos.personas[j].nombre == prueba[i][1]:
                        documentos.personas[j].agregar(prueba[i][2])
                        break

        else:  # En caso de que no lo haya encontrado
            temporal = Persona(prueba[i][1],prueba[i][2])  # Lo convertimos en el objeto a agregar
            
            documentos.insertar(temporal)

    elif prueba[i][0] == "pag":
        elASCII = ASCII(prueba[i][1])  # Se convierte en su elemento de la tabla
        otro2 = FuncionHash1(pagos.a,elASCII,pagos.b,pagos.primo,pagos.size)
        otro3 = FuncionHash2(elASCII,pagos.size)

        if pagos.tabla[otro2] != None:

            if pagos.tabla[otro2].nombre == prueba[i][1]:  # En caso de que esté en la primera posición de Hash
                pagos.tabla[otro2].agregar(prueba[i][2])

                for j in range(len(pagos.personas)):  # En este caso hay que agregar a esta lista
                    if pagos.personas[j].nombre == prueba[i][1]:
                        pagos.personas[j].agregar(prueba[i][2])
                        break
               
        if pagos.tabla[otro3] != None:

            if pagos.tabla[otro3].nombre == prueba[i][1]:  # En caso de que no esté en la primera posicion y si en la segunda
                pagos.tabla[otro3].agregar(prueba[i][2])


                for j in range(len(pagos.personas)):  # En este caso hay que agregar a esta lista
                    if pagos.personas[j].nombre == prueba[i][1]:
                        pagos.personas[j].agregar(prueba[i][2])
                        break

        else:  # En caso de que no lo haya encontrado
            temporal = Persona(prueba[i][1],prueba[i][2])  # Lo convertimos en el objeto a agregar
        
            pagos.insertar(temporal)

    else:
        pistas = pistas + prueba[i][2]    

print(pistas)
print(documentos.size)

for i in range(len(documentos.tabla)):
    if documentos.tabla[i] is not None:
        print(documentos.tabla[i].nombre,"\n",documentos.tabla[i].clave1)
        
        print(documentos.tabla[i].clave2)
        print("\n")
print(documentos.a," a")
print(documentos.b," b")
print("\n")        

for i in range(len(documentos.tabla)):
    if documentos.tabla[i] is not None:
        print(documentos.tabla[i].nombre,end = ",")

    else:
        print(None,end = ",")   
print("\n")
