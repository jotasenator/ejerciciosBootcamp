
#1. Haz un programa que dados 2 vectores calcule el producto escalar de los dos vectores.

import numpy as np

def producto_escalar(v1,v2):

	print(f'v1 = {v1}')
	print(f'v2 = {v2}')

	v1,v2 = np.array(v1),np.array(v2)
		
	resultado = np.dot(v1,v2)

	

	return f'El resultado del producto escalar es {resultado}'

if __name__ == '__main__':
	
	print(producto_escalar(list(map(int,input().strip().split())),list(map(int,input().strip().split()))))