## EJERCIO 1##

##Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
##(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

##for i in range (1,101):
##    print(i)


## EJERCIO 2##

##Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
##dígitos que contiene. 


## EJERCIO 3##
##3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
##dados por el usuario, excluyendo esos dos valores. 

##numero_inicial=int(input("ingrese el primer numero: "))
##numero_final= int(input("ingrese el siguiente numero: "))
##debo inicializar la sumatoria en cero
##sumatoria=0

##uso el ciclo for con el rango que quiero sumar. debo poner el mas uno en inicial para que no lo incluya
##si no aclaro nada excluye siempre el ultimo numero.
##for i in range(numero_inicial +1,numero_final):
##    sumatoria+=i
##print("la sumatorio de estos numeros es :",sumatoria)


## EJERCIO 4##

## Elabora un programa que permita al usuario ingresar números enteros y los sume en 
##secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
##un 0.
##detencion=0
##sumatoria=0
##numero=int(input("ingrese un numero entero: "))
##while numero != detencion :
##    sumatoria+=numero
##    numero=int(input("ingrese otro numero entero: "))
##print(" la sumatoria de la secuencia es: ",sumatoria)    


## EJERCIO 5##

## Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
##programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 

##import random
##numero= random.randint(0, 9)
##cont=0
##adivinador= int(input("Adivina un numero del 0 al 9: "))
##while numero != adivinador:
##   cont+= 1
##   adivinador= int(input("Incorrecto,ingresa otro numero del 0 al 9: ")) 
##cont +=1   
##print("Correcto!,es el numero:",numero,", tu numero de intentos fue: ", cont)    



## EJERCIO 6##

## Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
##entre 0 y 100, en orden decreciente. 

## tomo como valor inicial el numero 100 y como final el -1 porque quiero llegar al cero
## y voy bajando de a dos, obteniendo asi solo los numeros pares
##for i in range(100,-1,-2):
##  print((i))

## EJERCIO 7##

## Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
##número entero positivo indicado por el usuario.

##inicializo la suamatoria y solicito al usuario q ingrese el numero con el que debo 
##finalizar el rango

##sumatoria=0
##numero=int(input("ingrese un numero entero: "))
##defino el rango desde o al numero que ingresa el usuario 
##for i in range(0,numero):
##    sumatoria+=i
##print("la sumatorio de estos numeros es :",sumatoria)


## EJERCIO 8##
##Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
##programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
##negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
##menor, pero debe estar preparado para procesar 100 números con un solo cambio). 

##inicializo todos los contadores
##cont=0
##cont_impares=0
##cont_pares=0
##cont_negativo=0
##cont_positivo=0
##con un ciclo for determino la cantidad de numeros que necesito ingresar
##for i in range(100):
##    numero=int(input("ingrese un numero entero: "))
    ##indico el contador para que pare en 100
##    cont+=1
    ##con if determino si son par , impar negativo o positivo
##    if numero > 0:
##        cont_positivo+=1
##    elif numero < 0:
##        cont_negativo+=1           
##    if numero % 2 == 0:
##        cont_pares+=1
##    else :
##        cont_impares+=1
##devolvemos las cantidades por tipo de dato y la cantidad de numeros para corroborar
##print("los numeros pares fueron: ", cont_pares)
##print("los numeros impares fueron: ", cont_impares)
##print("los numeros negativos fueron: ", cont_negativo)
##print("los numeros positivos fueron: ", cont_positivo)
##print("la cantidad de numeros son: ", cont)


## EJERCIO 9##

## Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
##media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
##poder procesar 100 números cambiando solo un valor).


##from statistics import mean
##cont=0
##numeros=[]##lista para guardar los numeros
##con un ciclo for determino la cantidad de numeros que necesito ingresar
##for i in range(100):
##    numero=int(input("ingrese un numero entero: "))
    ##indico el contador para que pare en 100
##    cont+=1
    ##con esto guardo los numeros en mi lista ver:https://docs.python.org/es/3.13/tutorial/datastructures.html 
##    numeros.append(numero)
##    media= mean(numeros)
##print("la media es: ", media)    



## EJERCIO 10##

##Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
##usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. 


##pido el numero al usuario
##numero = int(input("Ingrese un número: "))
##inicializo la variable revertir
##revertir = 0
##el valor 
##revierto el numero matematicamente,mientras el numero que ingresa al ciclo sea mayor a cero va a segir ingresando
##while numero > 0:
    ##al numero le saco la unidad q me queda como residuo
##    residuo = numero % 10
    ##al numero le agrego la columna de la unidad multiplicandolo por diez y le agrego el valor que me quedo de residuo
##    revertir = (revertir * 10) + residuo
    ##ahora elimino el ultimo numero dividiendo el numero el 10 quedandome solo con la parte entera
##    numero //= 10
    ##este proceso se repite hasta que el valor es cero guardando el numero en la variable revertir
##print('El inverso del número ingresado es: ', revertir)
