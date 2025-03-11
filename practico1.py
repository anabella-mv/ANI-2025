import math

v=1
while v!=0:


    print("Ejecute el punto que desea resolver:")
    print("puntos del 1 al 12 o presione 0 para salir:")
    v=int(input("Seleccione un punto:"))

        if v==1:
        

        print("1-Dadas 3 variables: x, y, z, notar las diferencias entre:")

        print("a) x/y+z y x/(y+z)")

        print("En términos de resoluciòn al excluir los paréntesis la operaciòn serìa la suma de x/y y z, en el otro caso serìa la divisiòn de x entre la suma de y más z")

        print("b) x/y*z y x/(y*z)") 

        print("Igual al caso anterior, los paréntesis definen la prioridad operacional, por la tanto en un caso z se encontrarìa multiplicando a x y en el otro, x multiplica el denominador")

    elif v==2:
        print("2- Comprobar que el epsilon-maquina es 2^−52 = 2.2204 × 10^−16, escribiendo y comparando las siguientes dos lıneas de comando:")

        a = 1 + 2**-53; b = a-1

        print(a,b)

        c = 1 + 2**-52; d = c-1

        print(c,d)

        print("Se puede observar que en potencia 52 la máquina aún devuelve valores decimales mientras que para a y b directamente el número es tan pequeño que lo redondea a 0")

    elif v==3:
        print("3- Obtener el mayor y menor numero positivo en punto flotante (overflow y underflow ). Para obtener el mayor numero de overflow escribir un ciclo que vaya calculando las sucesivas  potencias de 2 y que finalice cuando se produce overflow. Se recomienda utilizar el comando isinf (importar la librerıa math) para detectar cuando se produce el overflow (escribir help(math.isinf) para obtener informacion sobre este comando). Otra instruccion que puede resultar util es break para interrumpir el ciclo cuando se produce el overflow, o utilizar un while. El numero de underflow se puede obtener dividiendo por 2 repetidamente hasta obtener un numero indistinguible del cero en punto flotante")

        print("Para Overflow:")

        o=0
        p=2.
        band=False
        while band==False:

            o=o+1
            p=p*2
            band=math.isinf(p)

        print("se potencia ",o," veces 2 para obtener overflow")

        print("Para Underflow:")

        i=1
        t=2
        x=0

        while i!=0:
            i=1/t
            t=t*2
            x=x+1

        print("se divide por dos a la",x ,"para obtener underflow")
    
    elif v==4:
        print("Ejecutar lineas de comando tal que cree un bucle que sume hasta 10 desde 0 sumando 0.1 y otra 0.5")

        print("En 0.1 tiene problemas porque la recursiòn causa errores haciendo una suma sin fin, mientras que en 0.5 llega a una declaracion formal")

        x=0
        while x!=10:
            x=x+0.5

    elif v==5:
        print("a) Escribir un programa que calcule el factorial de 6")
        
        n=1
        t=1
        while n<=6:
            t=t*n
            n=n+1
        print(t," es el resultado de 6 !")

        print("c) Escribir una funci´on que calcule el factorial de un n´umero n dado")

        fact=int(input("Ingrese el numero a factorizar:"))
        print("EL factorial de ",n, "es ", factorizar(fact))
    
    elif v==6:

        print("Escribir un programa que pida dos n´umeros reales e imprima en la pantalla el mayor de ellos. El programa debe indicar si los n´umeros son iguales.")
        pri=float(input("Ingrese el primer numero a comparar:"))
        sec=float(input("Ingrese el segundo numero a comparar:"))

        comparar(pri,sec)


    elif v==0:
        print("fin del programa")
        break
