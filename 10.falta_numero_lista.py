
def falta_lista(lista):


	resultado = [i for i in range(lista[0],1+lista[-1]) if i not in lista]

	return resultado

if __name__ == '__main__':
	print(falta_lista(list(map(int,input().strip().split()))))