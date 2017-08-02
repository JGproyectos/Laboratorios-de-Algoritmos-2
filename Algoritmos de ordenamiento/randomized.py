import random,time
def RandomizeSelect(A,p,r,i):
    if p == r:
        print("El elemento que estaba buscando es el siguiente:")
        return A[p]
    q = RandomizePartition(A,p,r)
    k = q-p+1
    if i == k:
        return A[q]
        
    elif i<k:
        return RandomizeSelect(A,p,q-1,i)
    else:
        return RandomizeSelect(A,q+1,r,i-k)

def RandomizePartition(A,p,r):
    try:
        i = random.randrange(p,r)
        A[i], A[r] =A[r], A[i] 
    except ValueError:
        pass
        
    return Partition(A,p,r)


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



A= []
for i in range(100):
	b = random.randrange(1,101)
	if b not in A:
		A.append(b)

print(A)
tiempo1 = time.time()
print(RandomizeSelect(A,0,len(A)-1,9))
tiempo2 = time.time() - tiempo1
print(tiempo2)

"""
Podemos observar que ambos algoritmos se ejecutan para el mismo arreglo y buscando el mismo número. 
Después de varias corridas se puede concluir que: 
el select no randomizado se ejecuta en un tiempo que varía en el intervalo (2,4) *10^-5, mientras que el randomizado corre en un tiempo de (2,5) * 10^-4. Podemos concluir que el randomizado tarda más tiempo que el no randomizado.

Esto se debe a que el select naturalmente escoge siempre el último elemento del arreglo para poder realizar la busqueda, mientras que el randomizado en cada una de sus llamadas recursivas escoje uno en una posición cualquiera, esto hace que tenga que hacer más iteraciones que el select no randomizado. Lo cual implica que tarde maś tiempo el randomizado que el no randomizado.
"""

