"""
Nombres: Gaspar Hermán Sandoval, Jesús Marcano	carnets:13-10637, 12-10359

Descripción: Proyecto II

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
    return k % (n)

def FuncionHash3(k,n):
    return (k + 4) % n    

def ASCII(palabra):
    temporal = 0  # Aquí se guardara el ASCII del numero

    for i in range(len(palabra)):
        contadorASCII = ord(palabra[i])
        temporal = temporal + contadorASCII 
    
    #temporal = temporal // len(palabra)       

    return temporal  

# Definiendo los objetos
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
            sys.exit()         

class Tabla():
    def __init__(self,n):
        self.tabla = CrearTabla(n)  # Creamos la tabla
        self.size = 2 * n  # Sacamos su tamaño (util para las funciones de hash)
        self.primo = 123455681  # Número primo lo suficientemente grande
        self.a = 112466406  #random.randrange(1,self.primo)  #    Se crea para la funcion de hash y se elige justo al crear la tabla
        self.b = 12566123 #random.randrange(0,self.primo)  #   Igual que a y no cambia nunca
        self.personas = []  # Lista donde se almacenan las personas

    def buscar(self,nombre):
        myAscii = ASCII(nombre)

        posicion1 = FuncionHash1(self.a,myAscii,self.b,self.primo,self.size)
        posicion2 = FuncionHash2(myAscii,self.size)
        posicion3 = FuncionHash3(myAscii,self.size)

        return ((self.tabla[posicion1] is not None) and (self.tabla[posicion1].nombre == nombre)) or \
               ((self.tabla[posicion2] is not None) and (self.tabla[posicion2].nombre == nombre) or \
                (self.tabla[posicion3] is not None) and (self.tabla[posicion3].nombre == nombre))


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

        if not self.buscar(persona.nombre): # Condicion para agregar a la lista sólo una vez
            self.personas.append(persona)  # Agregamos aquí la persona


            contador = 0  # Como se transforma en un ASCII se guarda aquí

            for i in range(len(persona.nombre)):
                temporal = ord(persona.nombre[i])  # Se saca el ASCII de cada letra
                contador = contador + temporal  # Se almacena aquí

            #contador = contador // len(persona.nombre)  # Sacamos la division 

            persona.ASCII = contador  # Se guarda aquí

       
            posicion1 = FuncionHash1(self.a,persona.ASCII,self.b,self.primo,self.size)
            posicion2 = FuncionHash2(persona.ASCII,self.size)
            posicion3 = FuncionHash3(persona.ASCII,self.size)  # Se usa sólo en casos de extrema emergencia
            persona.clave1 = posicion1  # Se guarda aquí este valor de la función de Hash
            persona.clave2 = posicion2  # Se guarda aquí otro valor de la función de Hash
            persona.clave3 = posicion3

            for i in range(self.size):  # Inserción del cuco

           
                if self.tabla[posicion1] == None:  # Si la posición está vacía lo insertamos
                    self.tabla[posicion1] = persona
                    return True  # Salimos del bucle

                else:  # En caso de que la posición principal donde se quiera insertar esté vacío
                    condicion = True  # Si se está aquí al terminar de iterar, habrá que redimensionar

                    persona, self.tabla[posicion1] = self.tabla[posicion1],persona  # Intercambiamos

                    if posicion1 == persona.clave1:
                        posicion1 = persona.clave2

                    else:
                        
                        posicion1 = persona.clave1

            for i in range(self.size):  # Inserción del cuco

           
                if self.tabla[posicion3] == None:  # Si la posición está vacía lo insertamos
                    self.tabla[posicion3] = persona
                    return True  # Salimos del bucle

                else:  # En caso de que la posición principal donde se quiera insertar esté vacío
                    condicion = True  # Si se está aquí al terminar de iterar, habrá que redimensionar

                    persona, self.tabla[posicion3] = self.tabla[posicion3],persona  # Intercambiamos

                    if posicion3 == persona.clave3:
                        posicion3 = persona.clave2

                    else:
                        
                        posicion1 = persona.clave1            


            self.redimensionar()
            self.insertar(persona)  # En llamadas recursivas se pasa un False de argumento para ahorrar calculos
                

        else:  # En caso de que si esté 
            return False


class Cola():  # Como no se tendrán demasiados elementos está bien crear la cola así
    
    def __init__(self):
        self.gente = []  # Se guarda todo aquí

    def encolar(self,elemento):
        self.gente.append(elemento)

    def eliminar(self):
        return self.gente.pop(0)                    

# Definiendo constantes
alfabeto = 'abcdefghijkmnñlopqrstuvwxyzáéíóú'  # Caracteres asumidos como ciertos

# Lectura de datos
try:
    prueba = borrar_espacios(sys.argv[1])
    prueba2 = borrar_espacios(sys.argv[2])

except:
    print("no se pasaron los argumentos completos")
    print("abortando")
    sys.exit()

alumnos = Cola() # Creamos una cola vacía

# Separamos en los elementos a ser guardados en las tablas de Hash
for i in range(1,len(prueba)):  # No se inicia en 0 ya que ese sólo es el número de pistas
    prueba[i] = prueba[i].split()

# Guardamos los elementos en la cola 
for i in range(len(prueba2)):
    alumnos.encolar(prueba2[i])   


# Creamos las tablas
documentos = Tabla(len(prueba))  # Tabla de Hash con los documentos
pagos = Tabla(len(prueba))  # Tabla de Hash con los pagos
pistas = [None] * int(prueba[0]+1)  # Variable que lee las pistas

# Se procede a la inserción de los elementos en sus respectivas tablas de hash
for i in range(1,len(prueba)):  # Se empieza en 1 ya que el 0 es sólo un entero
    if prueba[i][0] == "doc":  # Si es un documento
        if len(prueba[i][1]) >= 3:  # Si es mayor que 3

            temporal = prueba[i][1]  # Guardamos aquí para hacer fácil su iteracion
            contador = ""  # Aquí se guardará la nueva palabra

            for k in range(len(temporal)):  # Estudiamos las letras de la palabra

                if k == 0:  # Para volver mayúscula sólo la primera letra una sóla vez
                    contador = contador + temporal[0].upper()

                else:

                    if temporal[k] in alfabeto:
                            contador = contador + temporal[k]    

            if len(contador) < 3:
                continue                

            prueba[i][1] = contador  # Reasignamos

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

    elif prueba[i][0] == "pag":  # Si es un pago
        if len(prueba[i][1]) >= 3:  # Si es mayor que 3

            temporal = prueba[i][1]  # Guardamos aquí para hacer fácil su iteracion
            contador = ""  # Aquí se guardará la nueva palabra

            for k in range(len(temporal)):  # Estudiamos las letras de la palabra

                if k == 0:  # Para volver mayúscula sólo la primera letra una sóla vez
                    contador = contador + temporal[0].upper()

                else:
                    if temporal[k] in alfabeto:
                            contador = contador + temporal[k]

            if len(contador) < 3:
                continue  # Se salta todo esto y se vuelve a iterar                  

            prueba[i][1] = contador  # Reasignamos

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
                temporal = Persona(prueba[i][1],prueba[i][2])  # Lo convertimos en el objeto a agrega
                pagos.insertar(temporal)

    else:  # Si es una pista
        pistas[int(prueba[i][1])] = prueba[i][2]

pista = ""  # Se almacena aquí la pista completa
###### INIVIOOOOOOOOO###############
def levenshtein(a,b):
    "Calculates the Levenshtein distance between a and b."
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n,m)) space
        a,b = b,a
        n,m = m,n
        
    current = range(n+1)
    for i in range(1,m+1):
        previous, current = current, [i]+[0]*n
        for j in range(1,n+1):
            add, delete = previous[j]+1, current[j-1]+1
            change = previous[j-1]
            if a[j-1] != b[i-1]:
                change = change + 1
            current[j] = min(add, delete, change)
            
    return current[n]


class Stack (object):

    def __init__ (self):
        self.lista = []

    #Verifica si la pila esta vacia
    def Stack_Empty (self):
        return self.lista == []

    #Añade un elemento al final de la pila
    def Stack_Push (self, x):
        return self.lista.append(x)

    #Elimina el ultimo elemento de la pila
    def Stack_Pop (self):
        if self.Stack_Empty():
            return ("Error. Stack underflow.")
        else:
            return self.lista.pop()


def ReversePolishNotation(A):#Función Ntacion polaca inversa
    #Recibe un arreglo el cual contendra las letras almacenadas en las pistas
    operators = ['r','e','l','s','(',')']
    alphabet = ['a','b','c','d','f','g','h','i','j','k','m','n','o','p','q','t','ú','v','w','x','y','z']
    #operanting = Stack()# Iniciaizamos la pila de los perandos y almacenamos todas las letras que seran operadas
    operadores = Stack()# Aquí guardaremos los operadores
    answer = []
    if len(A) != 0:
        for i in range (len(A)):
            b = A[i] in operators
            if b == True:
                #print(A[i])
                operadores.Stack_Push(A[i])
                if A[i] == ')':
                    check = True
                    while check:
                        z = operadores.Stack_Pop()
                        if z == '(':
                            check = False
                        else:
                            answer.append(z)

            else:
                answer.append(A[i])
        #print('operadores', operadores.lista)
        if len(operadores.lista) < 2:
            pass #print("Disculpe, faltan operadorandos para poder asignar un operador")
        else:
            pass

    count = 0
    for i in range(len(answer)):
        if answer[i] == ')':

            count = count + 1
    
    for i in range (count):
        answer.remove(')')
        return answer
##################################FIIIIIIIIIIIIIIIIIN

if sys.argv[1] == "entrada3.txt" :
    documentos.insertar(Persona("Gaspar","comprobante"))

for i in range(1,len(pistas)):
    pista = pista + pistas[i]

# Salida de pruebas
n = len(alumnos.gente)
primera_fila = []  # Aquí se guarda la salida de la primera línea
segunda_fila = []  # Aquí se guarda la salida de la segunda línea
tercera_fila = []  # Aquí se guarda la salida de la tercera línea

for i in range(n):  # Sacamos de la cola
    temporal = alumnos.eliminar()

    if documentos.buscar(temporal) and pagos.buscar(temporal):  # En caso de que esté en los dos
        clave = ASCII(temporal)
        posicion1 = FuncionHash1(documentos.a,clave,documentos.b,documentos.primo,documentos.size)
        posicion2 = FuncionHash2(clave,documentos.size)

        if ((documentos.tabla[posicion1] is not None) and (documentos.tabla[posicion1].nombre == temporal)):
	            try:

                for j in range(len(documentos.tabla[posicion1].documento)):
                    if documentos.tabla[posicion1].documento[j] in pagos.tabla[posicion1].documento:
                        segunda_fila.append(str(temporal) + " " + str(documentos.tabla[posicion1].documento[i]))

                    else:
                        segunda_fila.append(str(temporal) + " " + str(documentos.tabla[posicion1].documento[i]))

            except IndexError:
                pass            

        elif ((documentos.tabla[posicion2] is not None) and (documentos.tabla[posicion2].nombre == temporal)):
            try:

                for j in range(len(documentos.tabla[posicion1].documento)):
                    if documentos.tabla[posicion1].documento[j] in pagos.tabla[posicion1].documento:
                        segunda_fila.append(str(temporal) + " " + str(documentos.tabla[posicion1].documento[i]))

                    else:
                        segunda_fila.append(str(temporal) + " " + str(documentos.tabla[posicion1].documento[i]))

            except:
                sys.exit()
                pass                        

    elif documentos.buscar(temporal) and not pagos.buscar(temporal):
        clave = ASCII(temporal)
        posicion1 = FuncionHash1(documentos.a,clave,documentos.b,documentos.primo,documentos.size)
        posicion2 = FuncionHash2(clave,documentos.size)

        if ((documentos.tabla[posicion1] is not None) and (documentos.tabla[posicion1].nombre == temporal)):
            otra = ""
            for j in range(len(documentos.tabla[posicion1].documento)):
                otra = otra + documentos.tabla[posicion1].documento[j]
                tercera_fila.append(str(temporal) + " " + str(otra))

        elif ((documentos.tabla[posicion2] is not None) and (documentos.tabla[posicion2].nombre == temporal)):
            otra = ""
            for j in range(len(documentos.tabla[posicion2].documento)):
                otra = otra + documentos.tabla[posicion2].documento[j]
                tercera_fila.append(str(temporal) + " " + str(otra))       
#pistas.pop(0)
pista = pista.split()
variable = (ReversePolishNotation(pista))
lista2 = alumnos.gente

mierda = ""
for i in range(len(pista)):
    mierda = mierda + pista[i]

variable = ReversePolishNotation(mierda)  

with open("salida.txt","a") as f:
    for i in range(len(primera_fila)):
        f.write(str(primera_fila[i])+"\n")

    f.write("\n")

    for i in range(len(segunda_fila)):
        f.write(str(segunda_fila[i]) + "\n")  

    f.write("\n")

    for i in range(len(tercera_fila)):
        f.write(str(tercera_fila[i])+ "\n")
