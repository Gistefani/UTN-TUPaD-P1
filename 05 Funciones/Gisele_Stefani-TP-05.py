## TP NUMERO CINCO: LISTAS##

##EJERCICIO 1
## Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
##range.

##lista_numeros = list(range(4,101,4))
##print(lista_numeros)


##EJERCICIO 2
##Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
##penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
##indexing con números negativos!

##lista_elementos = ["silla" , "mesa" , "sillon" ,"planta" , "mate"]
##ultimo_lista_elementos =  lista_elementos[-1]
##print(ultimo_lista_elementos)

##EJERCICIO 3
## Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
##pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior.
##

##lista_vacia = []
##lista_vacia.append("yerba")
##lista_vacia.append("mate")
#3lista_vacia.append("bombilla")
##print(lista_vacia)

##EJERCICIO 4
##Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
##respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
##en los videos o bien investigar cómo funciona el indexing con números negativos!

##animales = ["perro", "gato", "conejo", "pez"]

##animales[1] = "loro"
##animales[3] = "oso"
##print(animales)





##EJERCICIO 5
##Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

##numeros = [8, 15,  3, 22, 7]
##numeros.remove(max(numeros))
##print(numeros)

##Este programa elimina de la lista "numeros" el maximo, en este caso elimina el numero 22.

##6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
##pantalla los dos primeros.


##lista_ejercicio_seis = list(range(10,31,5))
##primeros_2 = lista_ejercicio_seis[:2]
##print(primeros_2) 



##7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
##cualesquiera.

##autos = ["sedan", "polo", "suran", "gol"]

##autos[1] = "parlante"
##autos[2] = "auriculares"

##print(autos)

##8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
##directamente. Imprimir la lista resultante por pantalla.

##dobles = []
##dobles.append(5*2)
##dobles.append(10*2)
##dobles.append(15*2)
##print(dobles)
##Si quisiera agregar todo juntos deberia usar la funcion extend.(5*2,10*2,15*2)




##9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
##diferentes clientes:
##compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
##a) Agregar "jugo" a la lista del tercer cliente usando append.
##b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
##c) Eliminar "pan" de la lista del primer cliente.
##d) Imprimir la lista resultante por pantalla

##compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
##agrego entre corchetes la posicion donde quiero agregar el valor
##compras[2].append("jugo") 
##luego de la lista coloco entre parentesis cual es el elemento donde quiero reemplazar y luego ocn otro corchete la posicion
##compras[1][1]="tallarines"
##Eliminar "pan" de la lista del primer cliente.
##compras[0].remove("pan")

##print(compras)



##10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
##● Posición lista_anidada[0]: 15
##● Posición lista_anidada[1]: True
##● Posición lista_anidada[2][0]: 25.5
##● Posición lista_anidada[2][1]: 57.9
##● Posición lista_anidada[2][2]: 30.6
##● Posición lista_anidada[3]: False
##Imprimir la lista resultante por pantalla.

##lista_anidada = [15,True,[25.5,57.9,30.6],False]

##print(lista_anidada)

