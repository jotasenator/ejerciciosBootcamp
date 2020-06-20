
#5. Haz un programa que dados dos números N y M escriba todos los números primos de N hasta M.

def primos_rango(N,M):


	lista1 = [i+1 for i in range(N,M+1) if i%2 == 0 and i+1<=M]
	
	return lista1

if __name__ == '__main__':

	print(primos_rango(int(input()),int(input())))