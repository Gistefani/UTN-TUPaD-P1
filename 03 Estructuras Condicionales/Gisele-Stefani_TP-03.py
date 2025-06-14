
##ACTIVIDADES TP ESTRUCTURAS CONDICIONALES 
 

###EJERCICIO 1

### Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
###deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

##Defino la variable
mayor_edad=18
##solicito la edad del usuario
edad = int(input("Por favor ingrese su edad "))

##si la edad es mayor muestra el mensaje "es mayor de edad"
if edad>mayor_edad:
    print("es mayor de edad")
    

###EJERCICIO 2

##Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
##mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
##mensaje “Desaprobado”

##Defino la variable
##Aprobado=6
##solicito la nota del usuario
##nota = int(input("Por favor ingrese su nota "))
##si la nota es mayor o igual que 6 muestra el mensaje "Aprobado"
##if nota>=Aprobado:
##    print("Aprobado")
##else:
##    print("Desaprobado")    
##    print("es mayor de edad")


###EJERCICIO 3

##Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
##número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
##contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
##operador de módulo (%) en Python para evaluar si un número es par o impar
##solicito un numero al usuario
##numero = int(input("Por favor ingrese un numero par "))
## si el numero es par imprimir Ha ingresado un número par"
##if numero % 2 == 0:
##    print ( "Ha ingresado un número par")
##si el numero no es par imprime "Por favor, ingrese un número par"    
##else:
##    print("Por favor, ingrese un número par ")


###EJERCICIO 4

## Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
##siguientes categorías pertenece:
##● Niño/a: menor de 12 años.
##● Adolescente: mayor o igual que 12 años y menor que 18 años.
##● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
##● Adulto/a: mayor o igual que 30 años.

##solicito su edad al usuario
##edad = int(input("Por favor ingrese su edad: "))
## ahora enumero los rangos
##if edad < 18:
##    if edad <12:
##      print(" su categoria es niño")
##    else :
##      print(" su categoria es adolescente")
##else:
##    if edad < 30:
##       print("su categoria es adulto joven")
##    else:
##       print("su categoria es adulto")         

###EJERCICIO 5

##Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
##(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
##pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
##pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
##de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
##como una lista o un string

##solicito la contraseña al usuario
##contrasena = input("Por favor ingrese su contraseña: ")

##uso la fincion len para determinar el largo del string
##if 8<=(len(contrasena))<=14:
##    print ("Ha ingresado una contraseña correcta")
##else:
##    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

###EJERCICIO 6

##escribir un programa que tome la lista
##numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
##hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

## from statistics import mode,median, mean
## import random

##defino la lista que voy a usar 
##num_al= [random.randint(1,100)for i in range (50)]
##media = mean(num_al)
##mediana= median(num_al)
##moda= mode(num_al)

##comparo los tres parametros para saber que tipo de sesgo tengo
##if media>mediana:
##    if mediana>moda:
##        print(" El Sesgo es positivo")
##     else:
##         print ("No se puede determinar si es positivo")
## 
## elif media<mediana:
##     if mediana<moda:
##         print("El sesgo es Negativo")
##     else:
##         print ("No se puede determinar si es negativo")    
## 
## elif media==moda==mediana:
##     print("No hay Sesgo")    

## else:
##     print ("No se puede determinar")


## print(f"Media: {media}, Mediana: {mediana}, Moda: {moda}")

###EJERCICIO 7

##Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
##termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
##pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
##pantalla.

##solicito una palabra al usuario y defino las vocales en mayuscula y minuscula
##palabra= input("Por favor ingrese su palabra: ")
##vocales="aeiouAEIOU"
##uso el [-1]paratomar la ultima letra de la palabra ingresada y lo comparo con las vocales 
##if palabra [-1] in vocales:
##    print(f"{palabra} !")
##else:
##    print(palabra)    
   


###EJERCICIO 8

##8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
##dependiendo de la opción que desee:
##1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
##2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
##3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
##El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
##usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
##lower() y title() de Python para convertir entre mayúsculas y minúsculas.

##solicito al usuario su nombre y que seleccione una opcion 
##nombre= input("Por favor ingrese su nombre: ")
##opcion=input(" 1. Si quiere su nombre en mayúsculas.2. Si quiere su nombre en minúsculas.3. Si quiere su nombre con la primera letra mayúscula" \
##"Por favor ingrese una opcion: ")

##if opcion == "1":
##    print(nombre.upper())
##elif opcion== "2":
##     print(nombre.lower())
##elif opcion== "3":
##     print(nombre.title())
##else:
##     print("ingrese una opcion correcta")          
    


###EJERCICIO 9

##Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
##magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
##por pantalla:

#solicito al usuario que ingrese la magnitud del terremoto 
##magnitud= input("Por favor ingrese la magnitud del terremoto 3,4,5,6 o 7: ")

##De acuerdo al valor ingresado se informa la magnitud.
##if magnitud <"7":
##    if  magnitud < "5":
##       if magnitud <"3":
##         print("Magnitud Muy leve")
##       elif magnitud =="3":
##          print("Magnitud leve")            
##       else:
##          print("Magnitud Moderada")
##   
##    elif  magnitud == "5" :   
##       print("Magnitud Fuerte")  
##    else:   
##       print("Magnitud Muy fuerte")
##else:
##   print("Magnitud extrema")               
    

###EJERCICIO 10


## Utilizando la información aportada en la siguiente tabla sobre las estaciones del año  
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
##del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
##si el usuario se encuentra en otoño, invierno, primavera o verano.  

##solicito al usuario que ingrese el hemsiflerio en el que se encuentra 
##h= input("Por favor ingrese el hemisferio en el que se encuentra N o S ?: " )
##m= input("ingrese el mes en numero 1-12:")
##d = input(" ingrese el dia (1-31): ")
##
##if h =="N":
##      if ( m == "3" and d <="20") or (m=="12" and d <="21") or m in [1,2]:
##            print("estas en invierno")
##      elif (m == "3" and d >= "20") or (m == "6" and d <= "20") or m in [4,5]:
##            print("estas en Primavera")
##      elif (m == 6 and d >= 21) or m in [7, 8] or (m == 9 and d <= 20):
##              print("Verano")      
##      else:
##        print("Otoño")        
##if h== "S":
##      
##      if ( m == "3" and d <="20") or (m=="12" and d <="21") or m in [1,2]:
##            print("estas en Verano")
##      elif (m == "3" and d >= "20") or (m == "6" and d <= "20") or m in [4,5]:
##            print("estas en otoño")
##      elif (m == "6" and d >= "21") or m in [7, 8] or (m == "9" and d <= "20"):
##              print("invierno")      
##      else:
##        print("primavera")     