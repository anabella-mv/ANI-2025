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

#Funciones necesarias y la derivada
def fun(x):
    fx=x
    return fx
def dfun(x):
    dfun=x
    return dfun

#Metodo de newton y secante:

def rsecante(fun,x0,x1,err,mit):
    hx=[]
    hy=[]
    hx.append(x0)
    hx.append(x1)
    fx0=fun(x0)
    fx1=fun(x1)
    hy.append(fx0)
    hy.append(fx1)
    #Que se repita hasta las iteraciones pedidas
    for i in range(mit):
       #guardo los valores
       
       #hx.append(x1)
       fx0=fun(x0)
       fx1=fun(x1)
       if (fx1-fx0)==0:
           print("no puedo realizar el metodo por problemas en el denominador")
           break
       
       xn=x1-((fx1*(x1-x0))/(fx1-fx0))
       x0=x1
       x1=xn
       fxn=fun(xn)
       hx.append(x1)
       hy.append(fx1)

       if abs(fxn)<err:
           print("Se encontraron las condiciones menores al error solicitado")
           break
    return hx,hy

def rnewton(fun,x0,err,mit):
    hx=[]
    hf=[]
  
    for i in range(mit):
       f=fun(x0)
       df=dfun(x0)
       if df==0:
           print("la derivada es nula en ese punto, no se puede continuar con el metodo de newton")
           break
       xn=x0-(f/df)
       x0=xn
       hx.append(x0)
       hf.append(f)


       if abs(x0-xn)/abs(x0)<err or abs(f)<err:
           print("Se encontraron las condiciones menores al error solicitado")
           break
    return hx,hf


def busqueda_ceros(fun,x0,x1,err,mit):
    #Debo realizar en simultaneo ambos metodos
    hxn,hyn=rnewton(fun,x0,err,mit)
    hxs,hys=rsecante(fun,x0,x1,err,mit)
    
    it_secante=(len(hys))-1 #Pues los primeros dos valores corresponden a una sola iteracion
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
    print("Seleccione el punto a ejecutar")
    print("Hay puntos del 1 al 5, presione 0 para terminar el programa")
    v=int(input("Seleccione un punto:"))

    while v!=0:
        if v==1:
            #Pide un valor al usuario para poder ingresar a la funcion que ejecute la serie seno
            a=float(input("Ingrese el valor de x para obtener el polinomio: "))
            print(serie_seno(a))
        if v==2:
            #Creo dos listas que van a hacer de puntos en el eje x,y, ademas de un contador para que recorra
            graficar_seno
        if v==3:
            print("Es un punto apreciable en el codigo")
            print("Al no tener valores ni funcion especifica, el punto no se ve desarrollado al ejecutarlo")
            #x0=1
            #x1=2
            #err=10**-5
            #mit=100
            #hx,hy=rsecante(fun,x0,x1,err,mit)
        if v==4:
            print("Es un punto apreciable en el codigo")
            print("Al no tener valores ni funcion especifica, el punto no se ve desarrollado al ejecutarlo")
            # los valores deben ser ingresados con anterioridad
            x0=1
            x1=2
            err=10**-4
            mit=100
            print("La raiz que encuentra el mejor 0 es: ", busqueda_ceros(fun,x0,x1,err,mit))
        if v==5:
            print("Es un punto apreciable en el codigo")


main()