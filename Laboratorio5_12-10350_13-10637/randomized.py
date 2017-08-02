import random


def RandomizeSelect(A,p,i,r):
    if p == r:
        return A[p]

    q = RandomizePartition(A,p,r)
    k = (q - p + 1)
    if i == k :
        return A[q]

    elif i < k:
        return RandomizeSelect(A,p,q-1,i)
    else:
        return RandomizeSelect(A,q+1,r,i-k)

def RandomizePartition(A,p,r):
    i = random.randrange(p,r)
    A[r], A[i] =A[i], A[r] 

    return Partition(A,p,r)

def Partition(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j] <= x:
        
            i = i+1
            
            A[i],A[j]= A[j],A[i]
    A[i+1],A[r] =A[r],A[i+1]
    return i+1



A= [1,6,4,8,9,45,36,7,8,3,6]

print(RandomizeSelect(A,0,10,10))