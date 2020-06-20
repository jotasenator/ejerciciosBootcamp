
#20. Para una string de caracteres n,s,e,o, donde cada letra indica un movimiento en el
#plano X-Y. n indica ir hacia el norte, s sud, e este y o oeste. Indicad el resultado
#final.
#Ej: nnnnseeo da como resultado (-1,3) (4 norte menos 1 sud, 1 oeste menos 2
#este). n seria (0,1),s seria (0,-1), e seria (-1,0) y o seria (1,0).


import numpy as np

def recorrido(direcciones):

	n = np.array([0,1])
	s = np.array([0,-1])
	w = np.array([1,0])
	e = np.array([-1,0])

	diccionario ={'n':n,'s':s,'e':e,'w':w}

	lista = []

	lista.extend(direcciones)

	contador = 0

	for i in lista:

		contador += diccionario[i]

	return tuple(contador)


if __name__ == '__main__':

	print(recorrido(list(input('Teclee las direcciones:'))))