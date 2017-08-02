def mediana(lista):
	# Precondicion
	assert(all(lista[i] <= lista[i+1] for i in range(len(lista)-1)))

	if len(lista) != 1:
		n = len(lista) // 2
		print(lista[n])
		mediana(lista[n:])
		mediana(lista[:n])