import math
import matplotlib.pyplot as plt
import numpy as np

#Punto 1: para un y arbitrario el cual puede ser reemplazado por cualquier funcion

def fun(x):
    y=x
    return y

def rbisec(fun,I,err,mit):
    a,b=I[0],I[1]
    fa, fb=fun(a), fun(b)
    if fa*fb>0:
        print("NO es posible aplicar el método")
        return None
    hx=[]
    hf=[]


    for i in range (mit):
        e=(b-a)/2
        c=a+e
        fc=fun(c)


        hx.append(c)
        hf.append(fc)
        if abs(fc)<err:
            print("La raiz es {c}, o por lo menos satisface el error aceptado, con valor {fc}")
            break
        if fa*fc<0:
            b=c
            fb=fc
        else:
            a=c
            fa=fc
    return hx,hf

#Punto 2
#a) 2x=tg(x) error menor a 10⁻5
def funcion_2a(x):
    print(math.tan(x))
    y=(x*2)-(math.tan(x))
    return y

#b) aproximacion a raiz de 3

def funcion_2b(x):
    return ((x**2)-3)

#Punto 3
#Metodo de Newton
def funcion_3b(x,a):
    f=(x**3)-a
    df=3*(x**2)
    return f,df
def rnewton(fun,x0,err,mit):
    hx=[]
    hf=[]
    f,df=fun(x0,a)
    if df==0:
        print("la derivada es nula en ese punto, no se puede continuar con el metodo de newton")
    for i in range(mit):
        hx.append(x0)
        xn=x0-(f/df)
        hf.append(f)
        f,df=fun(xn,a)

        if (abs(xn-x0)/abs(xn))<err or abs(f)<err:
           print("Se encontraron las condiciones menores al error solicitado")
           print(f"La raiz es {xn} y tiene un valor de {f}")
           break
        x0=xn
    return hx,hf
    
v=1
while v!=0:


    print("Ejecute el punto que desea resolver:")
    print("puntos del 1 al 9 o presione 0 para salir:")
    v=int(input("Seleccione un punto:"))

    if v==1:
        print("Es apreciable en el código el desarrollo de 1")

    elif v==2:
        w=1
        while w!=0:
            print("Ejecute el punto que desea resolver:")
            print("Inciso a al c, con a=1,b=2 y c dentro de ellos o 0 para salir:")
            w=int(input("Seleccione un punto:"))
            if w==1:
                err=10**(-5)
                hx,hy=rbisec(funcion_2a,[0.8,1.4],err,100)
                print(hx)
                print(hy)
                fig, ax = plt.subplots()
                ax.scatter(hx,hy)
                plt.show()


            elif w==2:
                err=10**-5
                hx,hy=rbisec(funcion_2b,[1,2.],err,100)
                print(hx)
                print(hy)
                fig, ax = plt.subplots()
                ax.scatter(hx,hy)
                plt.show()
            else:
                w=0
    elif v==3:
        print("Se aprecia en el código")
    elif v==4:
        print("Se solicita un a mayor a 0")
        a=-1
        while a<0:
            a=float(input("Ingrese el valor de a:"))
        err=10**(-6)

        hx,hf=rnewton(funcion_3b,2.,err,100)
    elif v==5:
        print("Se aprecia en el código")
    elif v==0:
        print("chauuuuuu")
