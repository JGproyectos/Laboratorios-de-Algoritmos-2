"""
Nombres: Gaspar Hermán Sandoval y Jesús Marcano, carnets: 13-10637 12-10359

Fecha: 19/05/2016/

Descripcion: Implementación de un select

adhocmed == mierda
"""
# Importando los modulos necesarios
import math

# Creando las funciones

def mediana(arreglo):
    n = len(arreglo)
    if n <= 5:
        return mierda(arrreglo)

    z = math.floor(n / 5)  # Calculamos el piso de un arreglo de 5

    Z = []  # Arreglo vacio

    for i in range(z):
        if i == 0 :
            Z.append(mierda(arreglo[5 * i]))
        else:
            Z.append(mierda(arreglo[5*i - 4:5*i]))  
        
    return Seleccion(Z,z // 2)  

def mierda(arreglo): #Leer el comentario inicial, eso fue a peticion de Gaspar
    try:
        assert(isinstance(arreglo,list))
    except:
        print(type(arreglo))
    #l = len(A)
    sorts = Quicksort.Quicksort(arreglo,0,len(arreglo))
    length = len(sorts)
    if not length % 2:
        return (sorts[length / 2] + sorts[length / 2 - 1]) / 2.0
    return sorts[length / 2]

        
"""
def Seleccion(arreglo,s):
    n = len(arreglo)
    i = 1
    j = n
"""

datos = [2,67,3,21,5,7,89,53,21,43,6,8,9,4,2,5567,4356]

hola = mediana(datos)

print(hola)