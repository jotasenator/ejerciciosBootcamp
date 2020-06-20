
# 9. Dado un número natural n, calcular la suma desde 1 hasta n (sin utilizar whiles ni fors)
# cuando se habla de si for o while hablamos de recursividad?
# cuando se entra el valor a partir de 998
# RecursionError: maximum recursion depth exceeded in comparison
# ampliando el limite desetrecursion puedo asimilar mayores valores en mi recursividad

import sys

sys.setrecursionlimit(10**6)

def suma(n):

	if n-1 == 0: return 1

	else:

		return suma(n-1) + n

if __name__ == '__main__':

	print(suma(int(input())))