
#ejercicio 3 a,b

def diccionario_improvisado(numero,palabra):

	dicci = {}

	lista_keyes = []

	for i in range(numero):

		i = str(i)

		lista_keyes.append(palabra+i)


	for j,k in enumerate(lista_keyes):

		dicci[k] = j

	return dicci

def diccionario_diccionario():

	diccio = {'d':3,'su':2,'alabao':4} #diccionario a modificar

	dicciON = {}

	for k,v in diccio.items():

		dicciON[k] = diccionario_improvisado(v,k)

	return dicciON


print(diccionario_diccionario())




