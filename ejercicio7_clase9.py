
'''
Dada una matriz cualquiera nx3, donde n es el numero de filas,hacer un
programa que imprima las filas que cumplan esta condicion:
En la tercera columna el valor que toma es mayor que 2 Y en la segunda
columna el valor que toma es mayor que 1.

'''
import numpy as np 

# aqui se puede modificar la matriz con cualquier valor, siempre manteniendo las 3 columnas
#en el futuro se puede hacer el codigo para cualquier numero de filas y columnas
#solo habra que modificar la condicion para obtener la lista final
a = np.array([[1,2,3],[4,3,2],[8,3,1],[8,4,2],[3,2,9],[1,2,4],[8,4,1],[2,1,3],[4,2,8],[1,3,9],[1,3,5]])

print(a)

#ultima columna

contador_columna = 0
lista_ultima = []

rango_matriz = np.shape(a)[1]

for col3 in a[:,rango_matriz-1]:

	if col3 > 2:
		
		lista_ultima.append(a[contador_columna,:])

	contador_columna += 1

print(f'Esto son los vectores que cumplen la condicion a >2 en la ultima columna: \n{lista_ultima}\n')

#penultima columna

contador_columna = 0
lista_penultima = []

rango_matriz = np.shape(a)[1]

for col2 in a[:,rango_matriz-2]:

	if col2 > 1:
				
		lista_penultima.append(a[contador_columna,:])

	contador_columna += 1

print(f'Esto son los vectores que cumplen la condicion a >1 en la penultima columna: \n{lista_penultima}\n')

#elementos en penultima que si en ultima

lista_final = []

for i in lista_ultima:
		
	for j in lista_penultima:

		if i[0] == j[0] and i[1] == j[1] and i[2] == j[2]:

			lista_final.append(i)



print(f'Estos son los vectores que cumplen con las dos condiciones en ambas columnas:\n{lista_final}')




		

	
