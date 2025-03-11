import math


print("Ejecute el punto que desea resolver:")
print("puntos del 1 al 12 o presione 0 para salir:")
v=int(input("Seleccione un punto:"))

while v==0:
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
        p=2

        while isinf(p)==false:
            o=o+1
            p=p*2

        print("se potencia ",o," veces 2" )