A = [31, 41, 59, 26, 41, 58]

def Insertion_sort(X, p, r):
	for j  in range (len(X)):
		key = X[j]
		print (key)
		i = j-1
		while i >= p and X[i] > key:
			X[i+1] = X[i]
			i = i - 1
			print(key, X)
		X[i+1] = key

		#print (X)
	return(X)

Insertion_sort(A, 0, 5)