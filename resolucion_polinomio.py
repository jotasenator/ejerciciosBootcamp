
def raices_polinomio_cuadrado():

	while True:

		print('Vamos a resolver a*X**2 + b*X + c')

		a = input('Teclee valor de a: ')
		b = input('Teclee valor de b: ')
		c = input('Teclee valor de c: ')

		try:

			discriminante = int(b)**2 - 4*int(a)*int(c)

			if discriminante == 0:

				solucion1 = -(int(b))/(2*int(a))

				print(f'\nLa solucion de {a}*X**2 + {b}*X + {c} es: \n{solucion1}\n')

			elif discriminante > 0:

				solucion1 = (-int(b) - (discriminante)**(0.5))/(2*int(a))
				solucion2 =  (int(b)- (discriminante)**(0.5))/(2*int(a))

				print('\nLas soluciones de {}*X**2 + {}*X + {} son: \n{}\n{}\n'.format(a,b,c,solucion1,solucion2))

			else:

				print(f'{a}*X**2 + {b}*X + {c} no tiene solucion..\n')

		except ValueError:

			print('\nTeclee un valor NUMERICO en a b c...\n')

			

raices_polinomio_cuadrado()


	

		
