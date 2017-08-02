def Merge(A,p,q,r):
	print("Q es igaul a :",q)
	print("r es igaul a :",r)
	n = q - p + 1
	m = r - q - 1
	print("El tama;o de L es:", n)
	print("El tama;o e R es:",m)

	L = [] #arreglo que contiene la primera mitad del  los que estan por ordenarse
	R = []# segunda mitad
	for i in range (0,n):
		L.append(A[p+i])

	for j in range(0,m):
		R.append(A[q+j + 1])

	print("L):",L)
	print("R):", R)
	

	i, j = 0,0

	for k in range(0,6):

		if i < n and j < m:
			if L[i] <= R[j]:
				A[k] = L[i]
				i = i + 1
			else:
				A[k] = R[j]
				j = j + 1
			print("1:",A)

		else:
			if i >= n:
				for g in range(j,m):
					A[k] = R[g]
					k = k + 1
					print("algo1")
			elif j >= m:
				for g in range(i,n):
					A[k] = L[g]
					k = k + 1
					print(L[g])
					print("algo2")
			break

		
		print("\n")
	return(A)
		
		

A = [3,27,38,43,80,90,100]
l = len(A) 
h = (len(A)//2) 
print(Merge(A,0,h,l))
		