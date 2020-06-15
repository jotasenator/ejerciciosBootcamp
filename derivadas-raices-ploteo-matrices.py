

# *********************************************** limites
'''from sympy import Symbol,limit,oo,sin,cos

x = Symbol('x')  # Creando el simbolo x

# La funcion limit nos da directamente el resultado

funcion = ((x**2+2*x)**0.5)/(2*x-5*x**2)
funcion1= (x**3-2)/(x**2+12*x)
funcion2= (3*x**2+5*x)/((x**3+5*x-3)**0.5)
funcion3= ((x**2-5*x+1)**0.5)/((4*x**2+3*x)**0.5)
funcion4= (cos(x))
funcion5= (sin(x)/x)


limite_buscado = limit(funcion5, x, 0)

print('El resultado del limite es: ',limite_buscado)'''

# *********************************************** derivadas ploteo ,raices de polinomios

'''from sympy import Symbol,diff, simplify,exp,oo,tan,pi,sin,cos

from sympy.solvers import solve

from sympy.plotting import plot


x = Symbol('x')  # Creando el simbolo x


fx1 = tan(x)
fx2 = sin(x)
fx3 = cos(x)

derivada1 = simplify(diff(fx1, x))
raices_derivada1 = solve(derivada1,x)


derivada2 = simplify(diff(derivada1, x))
raices_derivada2 = solve(derivada2,x)

print(derivada1)
print('Las soluciones de la primera derivada de la funcion: ',raices_derivada1)
print(derivada2)
print('Las soluciones de la segunda derivada de la funcion: ',raices_derivada2)

plot(fx1,fx2,fx3, (x, -pi,pi))'''

# *********************************************** integrales

'''from sympy import integrate,Symbol,sin,simplify

x = Symbol('x')

fx1 = sin(x)
fx2 = (3*x**3-x**2+2*x-4)
fx3 = (x)*sin(x)

print(integrate(fx1, x))
print(integrate(fx2, x))
print(integrate(fx2, (x,0,1)))
print(integrate(fx3, x))'''



# *********************************************** matrices
'''
from sympy import Matrix

M = Matrix([[1,2],
			[1,0]])

P,D = M.diagonalize()
#print(P)
#print(D)

#print(M.det())
#print(M.transpose())
#print(M.adjugate())
#print(M.adjugate().transpose())
#print(M.inv())
#print(M.eigenvects())
#print(M*M.inv())'''

'''B = Matrix([[3,5,2],
			[1,1,3],
			[2,2,1]])


print(B.det())
print(B.inv())
print(B.trace())'''

'''C = Matrix([[2,1,0,0],
			[0,0,-1,0],
			[0,0,3,1],
			[0,0,0,1]])

#print(C.eigenvects())

try:
	print(C.inv())
	

except :

	print('joder que no se  puede calcular la inversa que el determinante dio cero' )

P,D = C.diagonalize()
print(P)
print(D)

print(P.inv()*C*P)'''

# *********************************************** matrices diagonalizables
'''from sympy import Matrix,Symbol

M = Matrix([[1,2],
			[1,0]])

P,D = M.diagonalize()

print(M.eigenvects())

P1 = Matrix([[-1,2],
			 [1,1]])

print(P1.det())
print(P1.inv())

print(P1.inv()*M*P1)

print(P)
print(D)

print(P1.inv()*M*P1 == D)
print(M==P1.inv()*D*P1)

n = Symbol('n')

print(P1.inv()*(D**n)*P1)

n=2

print(M**n)

print(P1.inv()*(D**n)*P1)'''

# *********************************************** resolucion ecuaciones matrices

'''from sympy import Matrix,symbols,solve_linear_system,simplify,solve

x,y,z = symbols('x,y,z')

# calcular valores de x,y,x tal que Matrix([[1,1,1],[2,2,-1],[1/2,-2,3]]) * Matrix([[x],[y],[z]]) equal to Matrix([[10],[-2],[21]])
M = Matrix([[1,1,1,10],
			[2,2,-1,5],
			[1/2,-2,3,10]])



resultado1 = simplify(solve_linear_system(M,x, y, z))

print(resultado1)

N = Matrix([[1,1,1,10],
			[3,1,1,-2],
			[1,2,3,21]])



resultado1 = simplify(solve_linear_system(N,x, y, z))

print(resultado1)


# veamos rudimentariamente

from sympy.solvers.solveset import linsolve

M1 = Matrix([[1,1,1],[2,2,-1],[1/2,-2,3]])
M2 = Matrix([[x],[y],[z]])
M3 = Matrix([[10],[5],[10]])

Mtotal = M1*M2-M3

resultado = linsolve([Mtotal[0],Mtotal[1],Mtotal[2]],(x,y,z))

print(resultado)


M1 = Matrix([[1,1,1],[3,1,1],[1,2,3]])
M2 = Matrix([[x],[y],[z]])
M3 = Matrix([[10],[-2],[21]])

Mtotal = M1*M2-M3

resultado = linsolve([Mtotal[0],Mtotal[1],Mtotal[2]],(x,y,z))

print(resultado)'''
