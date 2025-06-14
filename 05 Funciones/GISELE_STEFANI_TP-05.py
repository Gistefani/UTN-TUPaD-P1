##Funciones en Python

##EJERCICIO 1##

##Crear una función llamada imprimir_hola_mundo que imprima por
##pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
##programa principal


##FUNCIONES 
##def imprimir_hola_mundo():
##   print("hola mundo")

##PROGRAMA PRINCIPAL
##saludo = imprimir_hola_mundo()


##EJERCICIO 2##
##Crear una función llamada saludar_usuario(nombre) que reciba
##como parámetro un nombre y devuelva un saludo personalizado.
##Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
##principal solicitando el nombre al usuario.

##FUNCIONES 

##def saludar_usuario(nombre):
       
##        return print(f" hola {nombre}")


##PROGRAMA PRINCIPAL
##nombre = input("ingrese su nombre : ")
##saludo = saludar_usuario(nombre)

##EJERCICIO 3##
##Crear una función llamada informacion_personal(nombre, apellido,
##edad, residencia) que reciba cuatro parámetros e imprima: “Soy
##[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados

##FUNCIONES
##def datos_personales (x, y, z , w):

## return print(f" Soy {x} {y}, tengo {z} años y vivo en {w}")

##PROGRAMA PRINCIPAL
##nombre =input("ingrese su nombre : ")
##apellido =input("ingrese su apellido : ")
##edad =input("ingrese su edad : ")
##residencia =input("ingrese su lugar de residencia : ")
##informacion= datos_personales(nombre,apellido,edad,residencia)



##EJERCICIO 4##
##Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para ##mostrar los resultados.

import math
##FUNCIONES
def calcular_area_circulo(radio) :
         area = math.pi * radio ** 2
         return area

def calcular_perimetro_circulo(radio) :
        perimetro = 2* math.pi * radio
        return perimetro

##PROGRAMA PRINCIPAL
radio = float(input("ingresar el radio: "))
area = calcular_area_circulo (radio)
perimetro = calcular_perimetro_circulo (radio)
print(f"el area del circulo es : {area:.2f} y el perimetro:  { perimetro:.2f}")



##EJERCICIO 5##
##Crear una función llamada segundos_a_horas(segundos) que reciba
##una cantidad de segundos como parámetro y devuelva la cantidad
##de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.



##FUNCIONES
##def segundos_a_horas(segundos):
##     horas = round (segundos / 3600, 2)
##     return horas

##PROGRAMA PRINCIPAL

##segundos = float(input("ingrese la cantidad de segundos : "))
##horas = segundos_a_horas(segundos)
##print (f"la cantidad de horas son : {horas}")



##EJERCICIO 6##

##Crear una función llamada tabla_multiplicar(numero) que reciba un
##número como parámetro y imprima la tabla de multiplicar de ese
##número del 1 al 10. Pedir al usuario el número y llamar a la función.

##FUNCIONES

##def tabla_multiplicar(numero):
## for i in range(0, 11):
##        print(str(numero) + " * " + str(i) + " = " + str(numero * i))


##PROGRAMA PRINCIPAL
##numero = int(input("Por favor, ingrese un número entero: "))
##tabla_multiplicar(numero)


##EJERCICIO 7##

##Crear una función llamada operaciones_basicas(a, b) que reciba
##dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de ##forma clara.

##FUNCIONES
##def operaciones_basicas(n1,n2):
## sum = n1 + n2
## res = n1 - n2
## mul = n1 * n2
## div = n1 / n2
## print(f"el resultado de las operaciones son: suma {sum}, resta {res}, multiplicacion {mul} y division {div}")

##PROGRAMA PRINCIPAL
##n1 = int(input ("ingresar el primer numero: "))
##n2 = int(input ("ingresar el segundo numero: "))
##operaciones_basicas(n1,n2)


##EJERCICIO 8##

##Crear una función llamada calcular_imc(peso, altura) que reciba el
##peso en kilogramos y la altura en metros, y devuelva el índice de
##masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

##FUNCIONES
##def calcular_imc(altura,peso):
##  imc=peso/(altura*altura)
##  print(f"su indice de masa corporal es {imc:.2f}")

##PROGRAMA PRINCIPAL
##altura = float(input ("ingresar su altura en metros: "))
##peso = float(input ("ingresar su peso en kg: "))
##calcular_imc(altura,peso)

##EJERCICIO 9##
##Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
##una temperatura en grados Celsius y devuelva su equivalente en
##Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
##resultado usando la función.


##FUNCIONES
##def celsius_a_fahrenheit(celsius):
##  tempf=(1.8*celsius)+32
##  print(f"su temperatura en grados Fahrenheit es: {tempf}")

##PROGRAMA PRINCIPAL
##celsius= float(input ("ingresar su temperatura en grados Celsius: "))
##celsius_a_fahrenheit

##EJERCICIO 10##
##.Crear una función llamada calcular_promedio(a, b, c) que reciba
##tres números como parámetros y devuelva el promedio de ellos.
##Solicitar los números al usuario y mostrar el resultado usando esta
##función.
##FUNCIONES
##def calcular_promedio(a, b, c): 
##     prom = (a + b +c)/3
##     print(f"su promedio es: {prom}")
##PROGRAMA PRINCIPAL
##a = float(input ("ingresar su primera nota: "))
##b = float(input ("ingresar su segunda nota: "))
##c = float(input ("ingresar su tercera nota: "))
##calcular_promedio