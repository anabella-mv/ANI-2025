#Cito librerias necesarias

import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.interpolate import interp1d
from scipy import linalg

#punto 1: aproximación: Cuadrados minimos

def intenumcomp(fun, i, a, b, N, regla):
    h = (b - a)/N
    vector_x = np.linspace(a, b, N+1)
    
    if regla == "simpson":
        if N % 2 != 0:
            raise ValueError("Para la regla de Simpson, N debe ser par")
        suma = fun(a)[i] + fun(b)[i]
        for k in range(1, N):
            if k % 2 == 0:
                suma += 2 * fun(vector_x[k])[i]
            else:
                suma += 4 * fun(vector_x[k])[i]
        return (h/3) * suma

    else:
        raise ValueError(f"{regla} usar 'simpson'")


#implemento una funcion para conseguir minimizar el error hasta la cota dada

def interr(fun,i,a,b,tol,real):
    N = 2
    while abs(intenumcomp(fun,i,a,b,N,'simpson')-real) >= tol:
        N += 2

        if N ==1000:
            print('no se llego al minimo de la tolerancia')
            break

    return N, intenumcomp(fun,i,a,b,N,'simpson')

#defino las funciones a integrar para el ajuste cuadratico por cuadrados minimos

def funciones(x):
    f=[]
    for a in range(3):
        fx=np.sin(x)*(x**a)
        f.append(fx)
    return f


def polinomios(x):
    p=[]
    for a in range(5):
        px=x**a
        p.append(px)
    return p

def punto1():

    #defino los valores de las integrales
    inte=[]
    for i in range (2):

        inti = interr(funciones,i,0,np.pi/2,10e-5,1)[1]
        inte.append(inti)
        print(inti)

    int2 = interr(funciones,2,0,np.pi/2,10e-5,np.pi-2)[1]
    inte.append(int2)
    print(int2)

    # integrales de los polinomios

    integrales=[]

    for j in range(4):

        intpol= intenumcomp(polinomios,j,0,np.pi/2,2,'simpson')
        integrales.append(intpol)

    intpol4 = interr(polinomios,4,0,np.pi/2,10e-5,np.pi**5/(5*2**5))[1]
    integrales.append(intpol4)

    print(integrales)
    return integrales, inte

#Para el punto 2 necesito linalg para realizar la descompcision y resolver las ecuaciones del sistema

def solLU(A,B):
    P,L,U = linalg.lu(A)
    pb = P @ B
    y_sol = linalg.solve_triangular(L,pb,lower=True)
    coeficientes = linalg.solve_triangular(U,y_sol)
    return coeficientes

#defino el polinomio cuadratico con los coeficientes
def aprox_cuadmin(x,coeficientes):

    cuadmin = coeficientes[0] + coeficientes[1]*x + coeficientes[2]*(x**2)

    return cuadmin

def punto2():
    integrales,inte=punto1()
    #Matriz A del sist. a resolver
    A = np.zeros([3,3])
    for i in range(3):
        for j in range(3):
            a=j+i
            A[i,j]=integrales[a]
    print(A)

    #Matriz B del sist. a resolver
    
    B=[]
    for b in range(3):
        B.append(inte[b])
    print(B)
    coeficientes=solLU(A,B)
    return coeficientes

def punto3():
    

    #defino los puntos equiespaciados y les atribuyo un valor en la funcion
    nodos = np.linspace(0,np.pi/2,5)
    print(nodos)
    fnodos = funciones(nodos)
    y=fnodos[0]
    print(y)

    #defino el spline cubico
    spline_3 = interp1d(nodos,y,'cubic')
    x = np.linspace(0,np.pi/2,50)
    pol = spline_3(x)

    return pol


#Menú principal para la ejecución del programa
def main():
    punto=1
    while punto!=0:
        print("Elija el ejercicio a desarrollar:")
        print("Los puntos a ejecutar son 1, 2 , 3 y 4, el 0 es para terminar el programa")
        punto=int(input("Seleccione el punto a desarrollar: "))

        if punto==1:

            integralesp1,defe=punto1()
            print(integralesp1)

        if punto==2:

            coeficientes=punto2()
            print("Estos son los coeficientes:")
            print(coeficientes)

            #En las funciones defino el polinomio cuadratico con estos coeficientes obtenidos

        if punto==3:

            pol=punto3()
            print(pol)

        if punto==4:

            x = np.linspace(0,np.pi/2,50)
            pol=punto3()
            coef=punto2()

            plt.style.use('seaborn-v0_8')
            plt.title('Comparacion de las aproximaciones con la funcion original', fontsize=14, pad=20)
            plt.xlabel('x', fontsize=12)
            plt.ylabel('y', fontsize=12)

            #llamo a los puntos anteriores para el desarrollo del grafico
            
            plt.plot(x,pol,'.r')
            plt.plot(x,funciones(x)[0],'-g')
            plt.plot(x,aprox_cuadmin(x,coef),'.y')
            plt.show()

        if punto==0:
            break
main()




