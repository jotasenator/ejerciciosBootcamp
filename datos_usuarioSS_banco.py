

contador = 1
diccionario_datos_usuarios_banco = {}


while True:
	
	lista_datos = []

	nombre = input('Nombre del usuario: ')
	apellidos = input('Apellidos del usuario: ')
	CI = input('Numero de Carnet de Identidad: ')
	direccion = input('Direccion de residencia: ')
	estado_civil = input('Estado Civil: ')
	hijos = input('Numero de hijos: ')
	tarjeta_banco = input('Numero de cuenta: ')
	saldo_tarjeta = input('Saldo actual: ')


	lista_variables = [nombre, apellidos, CI, direccion, estado_civil, hijos, tarjeta_banco, saldo_tarjeta]
	lista_variables_key = ['Nombre', 'Apellidos', 'Carnet', 'Direccion', 'Estado_civil', 'Hijos', 'Tarjeta_banco', 'Saldo_tarjeta']


	for i in range(8):

	    lista_datos.append(((lista_variables_key[i]),lista_variables[i]))


	diccionario_datos_usuarios_banco['usuario'+str(contador)] = dict(lista_datos)

	contador += 1

	print(diccionario_datos_usuarios_banco)

	desea_continuar = input('\nDesea añadir otro usuario: y/n? \n')

	if desea_continuar.upper() == 'Y':

		pass

	else :

		print('gg well played')

		break





    

