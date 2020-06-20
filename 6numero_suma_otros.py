
#6. Haz un programa que dado una lista de números, devuelva “SI” si hay un número que
#sea la suma de todos los otros números y “NO” si no lo hay

def numero_suma_otros(lista):

	resultado = [ i for i in lista if i == sum(lista)- i]

	if resultado != []:

		return f'SI existe numero que sea la suma de los demas en la lista y es este:{resultado[0]}'

	else:

		return 'De eso nada monada jeje'

if __name__ == '__main__':
	
	print(numero_suma_otros(list(map(int,input().strip().split()))))





