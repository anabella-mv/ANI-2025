#Creo menu para la ejecucuion del parcial: basta con elegir el punto a desarrollar

#Llamo las librerias que creo necesarias
import matplotlib.pyplot as plt
import math
import numpy as np

#Punto 1:
def serie_seno(x):
    b=0
    #creo un condicional recursivo que calcule y sume los tèrminos
    for i in range(5):
        y=(((-1)**i)*(x**((2*i)+1)))/(math.factorial((2*i)+1))
        b=b+y
    return b

#Punto 2:
def graficar_seno():
    hx=[]
    hy=[]
    m=0
    while m<=6.4:
        hx.append(m)
        hy.append(serie_seno(m))
        m=m+0.01
    fig, ax = plt.subplots()
    ax.scatter(hx,hy)
    plt.show()

#Punto 3:

#Funcion necesaria de la derivada
def dfun(x):
    b=0
    #creo un condicional recursivo que calcule y sume los tèrminos
    for i in range(5):
        y=(((-1)**i)*(x**(2*i)))/(math.factorial(2*i))
        b=b+y
    return b

#Metodo de newton y secante:

def rsecante(fun,x0,x1,err,mit):
    hx=[]
    hy=[]
    
    #Obtengo los primeros f necesarios para la ejecucion
    
    fx0=fun(x0)
    fx1=fun(x1)
    
    #Que se repita hasta las iteraciones pedidas
    for i in range(mit):
       
       if (fx1-fx0)==0:
           print("no puedo realizar el metodo por problemas en el denominador")
           break
       
       #Hago la iteracion
       
       xn=x1-((fx1*(x1-x0))/(fx1-fx0))
       
       x0=x1
       x1=xn
       
       #Evaluo y guardo los valores obtenidos en la it.
       fxn=fun(x1)
       hx.append(x1)
       hy.append(fx1)

       if abs(fxn)<err:
           print("Se encontraron las condiciones menores al error solicitado")
           break
       
       fx0=fun(x0)
       fx1=fun(x1)
       
    return hx,hy

def rnewton(fun,x0,err,mit):
    hx=[]
    hf=[]
    
    f=fun(x0)
    df=dfun(x0)
    for i in range(mit):
       
       if df==0:
           print("la derivada es nula en ese punto, no se puede continuar con el metodo de newton")
           break
       
       #Iteracion
       xn=x0-(f/df)
       
       f=fun(xn)
       df=dfun(xn)
       
       hx.append(xn)
       hf.append(f)


       if abs(x0-xn)/abs(x0)<err or abs(f)<err:
           print("Se encontraron las condiciones menores al error solicitado")
           break
       
       x0=xn
    return hx,hf


def busqueda_ceros(fun,x0,x1,err,mit):
    #Debo realizar en simultaneo ambos metodos
    hxn,hyn=rnewton(fun,x0,err,mit)
    hxs,hys=rsecante(fun,x0,x1,err,mit)
    
    it_secante=(len(hys)) #Trabajo con el tamaño de la lista
    raiz_secante=hxs[-1] #EL ultimo valor guardado es mi raiz

    print("iteraciones de la secante: ",it_secante," raiz dada por la secante: ", raiz_secante)

    it_newton=(len(hyn))
    raiz_newton=hxn[-1]

    print("iteraciones de newton: ",it_newton," raiz dada por newton: ", raiz_newton)


    fn=fun(raiz_newton)
    fs=fun(raiz_secante)
    print("el cero de secante es: ", fs, " el cero de newton es: ",fn)
    if abs(fn)<abs(fs):
        return raiz_newton
    else:
        return raiz_secante

def main():

    v=1
    #Los puntos 3 y 4 se ven apreciados en la ejecución del punto 5
    print("Seleccione el punto a ejecutar")
    print("Hay puntos 1,2 y 5, presione 0 para terminar el programa")
    v=int(input("Seleccione un punto:"))

    while v!=0:
        if v==1:
            #Pide un valor al usuario para poder ingresar a la funcion que ejecute la serie seno
            a=float(input("Ingrese el valor de x para obtener el polinomio: "))
            print(serie_seno(a))
        if v==2:
            #Creo dos listas que van a hacer de puntos en el eje x,y, ademas de un contador para que recorra
            graficar_seno
        if v==5:
            print("En este punto se aprecia la ejecución de los puntos 3 y 4 del parcial")
            x0=3
            x1=6
            err=10**-5
            mit=100
            busqueda_ceros(serie_seno,x0,x1,err,mit)
        else:
            print("Elija otra opcion")


main()
