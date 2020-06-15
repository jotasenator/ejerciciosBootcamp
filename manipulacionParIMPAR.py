

# ejercicio Tócate!!
#dado n pertenezca Naturales, si n es par lo divido entre 2, si n es impar lo multiplico *3 y le sumo 1
#hasta que todo este proceso de como resultado 1, añadirlo a una lista de resultados

n = int(input('Teclee un numero natural: '))

lista_resultados = []

while n!=1:

	lista_resultados.append(n)

	if n%2 == 0:

		n = int(n/2)

	else:

		n = int(n*3+1)

lista_resultados.append(1)

print(lista_resultados)



