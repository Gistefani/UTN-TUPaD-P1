
##ACTIVIDADES TP DATOS COMPLEJOS
 

###EJERCICIO 1


##1)	Dado el diccionario precios_frutas
##precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
##1450}
##Añadir las siguientes frutas con sus respectivos precios:
##●	Naranja = 1200
###●	Manzana = 1500
##●	Pera = 2300

##precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}

##precios_frutas ["Naranja"] = 1200
##precios_frutas ["Manzana"] = 1500
##precios_frutas ["Pera"] = 2300

##print(precios_frutas)

###EJERCICIO 2

##Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
##●	Banana = 1330
##●	Manzana = 1700
##●	Melón = 2800

##precios_frutas ["Banana"] = 1330
##precios_frutas ["Manzana"] = 1700
##precios_frutas ["Melón"] = 2800

##print (precios_frutas)


###EJERCICIO 3

##Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.

##print(precios_frutas.keys())




###EJERCICIO 4
##	Escribí un programa que permita almacenar y consultar números telefónicos.
##•	Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
##•	Luego, pedí un nombre y mostrale el número asociado, si existe. Ejemplo:


##contactos = {}
##print("carga 5 contactos: ")
##for i in range(5):
## nombre = input("ingrese su nombre : ")
## telefono = input("ingrese su telefono : ")
## contactos[nombre]=telefono

##print(contactos) 

##consulta = input("\nIngresá el nombre del contacto que querés buscar: ")
##if consulta in contactos:
##    print(f"El número de {consulta} es: {contactos[consulta]}")
##else:
##    print("Ese contacto no está en la agenda.")





###EJERCICIO 5

##	Solicita al usuario una frase e imprime:
##•	Las palabras únicas (usando un set).
##•	Un diccionario con la cantidad de veces que aparece cada palabra. Ejemplo:




##frase = input("ingrese su frase : ")
##entrada = frase.split()
##palabras_unicas = set(entrada)
##print (palabras_unicas)

##contador={}
##for entrada in entrada:
##  if entrada in contador:
##     contador[entrada] +=1
##  else:
##     contador[entrada] = 1

##print("\n Cantidad de veces que aparece cada palabra:")     
##for entrada, cantidad in contador.items():
##   print(f"{entrada}:{cantidad}")
     


###EJERCICIO 6

##Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno.

##alumno ={}

##for i in range(3):
##    nombre=input(f"ingrese el nombre del alumno {i+1}:")
##    notas_input = input(f"ingrese 3 notas separadas por espacios para {nombre}")
##    ##map me convierte los numeros en decimales
##    notas = tuple(map( float,notas_input.split()))
##
##    if len(notas)==3:
##        alumno[nombre]=notas
##    else:
##        print("deben ser tres notas")
##        break 
##print("promedios:")
##for nombre, notas in alumno.items():
##    promedio=sum(notas)/3
##    print(f"{nombre}:{promedio:.f2}")


##7)	Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
##•	Mostrá los que aprobaron ambos parciales.
##•	Mostrá los que aprobaron solo uno de los dos.
##•	Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).




##8)	Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
##•	Consultar el stock de un producto ingresado.
##•	Agregar unidades al stock si el producto ya existe.
##•	Agregar un nuevo producto si no existe.




##9)	Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. Ejemplo:
##Permití consultar qué actividad hay en cierto día y hora.



##10)	Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
##•	Las capitales sean las claves.
##•	Los países sean los valores. Ejemplo:
