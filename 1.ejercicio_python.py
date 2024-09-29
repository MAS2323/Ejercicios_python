# Ejercicio 2
# Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.

print("¡Hola Mundo!")

# Ejercicio 2
# Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego
#  muestre por pantalla el contenido de la variable.

saludar = input("Introduce la cadena ¡Hola Mundo! ")
print(saludar)

# Ejercicio 3
# Escribir un programa que pregunte el nombre del usuario en la consola y después
# de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!,
# donde <nombre> es el nombre que el usuario haya introducido.

saluda = input("Cual es su nombre: ")
print(f"¡Hola {saluda}!")

# Ejercicio 4
# Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética
# (3+2/2*5)^2

operacion = ((3 + 2)/(2 * 5))**2
print(operacion)

# Ejercicio 5
# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por
# hora. Después debe mostrar por pantalla la paga que le corresponde.

htrabaja = int(input("Introduce el numero de horas que has trabajado: "))
chora = float(input("Introduce el coste por hora trabajado: "))
paga = htrabaja * chora
print(f"La paga que le corresponde es de: {paga} FCF")

# Ejercicio 6
# Escribir un programa que lea un entero positivo, n
# introducido por el usuario y después muestre en pantalla la suma de todos
# los enteros desde 1 hasta n La suma de los
# primeros enteros positivos puede ser calculada de la siguiente forma:
# suma = n(n + 1)/ 2

numero = int(input(
    "Introduzca un numero entero por pantalla para calcular la suna enesima del mismo: "))

suma = (numero * (numero + 1)) / 2
print("La suma enesima del ", numero, "es: ", suma)


# Ejercicio 7
# Escribir un programa que pida al usuario su peso (en kg) y
# estatura (en metros), calcule el índice de masa corporal y lo
# almacene en una variable, y muestre por pantalla la frase Tu índice de
# masa corporal es <imc> donde <imc> es el índice de masa corporal calculado
# redondeado con dos decimales.
"""
El índice de masa corporal (IMC) es el peso de una persona en 
kilogramos dividido por el cuadrado de la estatura en metros.
"""

print("Programa para calcular el Indice de Masa Coporal de las personas (IMC)")

peso = int(input("Introduzca su peso en kg: "))
altura = float(input("Introduzca su altura en metros: "))

imc = (peso)/(altura**2)

print("Su indice de masa corporal es de ", imc)

# Ejercicio 8
# Escribir un programa que pida al usuario dos números enteros y muestre por pantalla
# la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números
# introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división
# entera respectivamente.

print("Programa para devolver el cociente (c) y resto (r) de dos numeros enteros introducidos por pantalla")

divin = int(input("Introduzca el dividendo: "))
divisorm = int(input("Introduzca el divisor: "))
cociente = int(divin / divisorm)
resto = divin % divisorm

print(f"El cociente es {cociente} y el resto {resto}")


# Ejercicio 9
# Escribir un programa que pregunte al usuario una cantidad a invertir, el
# interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

print("Programa para calcular el dinero invertido")

"""cantidad = float(input("Introduce la cantidad a invertir: "))
interanual = float(input("Introduce el interes anual: "))
numagnos = int(input("Introduce el numero de agnos: "))

capiObtenido = cantidad * interanual * numagnos
print(f"El capital obtenido es: {capiObtenido}")"""

"""
La función round en python redondea el valor decimal 
de un número a su entero más cercano. Por ejemplo: round(65.66) = 66. 
Además, se puede entregar a la función el número de decimales al que 
se debe redondear el número especificado. Por ejemplo, round(65.66, 1) = 65.7.

"""

cantidad = float(input("¿Cantidad a invertir? "))
interes = float(input("¿Interés porcentual anual? "))
años = int(input("¿Años?"))
print("Capital final: " + str(round(cantidad * (interes / 100 + 1) ** años, 2)))

# Ejercicio 10
# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas.
# Suele hacer venta por correo y la empresa de logística les cobra por peso
# de cada paquete así que deben calcular el peso de los payasos y muñecas que
# saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g.
# Escribir un programa que lea el número de payasos y muñecas vendidos en el último
# pedido y calcule el peso total del paquete que será enviado.

print("Programa para calcule el peso total del paquete que será enviado")

numMpayasos = int(input("Introduzca un numero de payasos "))
numMuneca = int(input("Introduzca el numero de muñeca "))

pesoTotal = numMpayasos * 112 + numMuneca * 75
print(f"El peso total del paquete a enviar es {pesoTotal}")

# Ejercicio 11
# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece
# el 4% de interés al año. Estos ahorros debido a intereses, que no se
# cobran hasta finales de año, se te añaden al balance final de tu cuenta
# de ahorros. Escribir un programa que comience leyendo la cantidad de dinero
# depositada en la cuenta de ahorros, introducida por el usuario. Después el
# programa debe calcular y mostrar por pantalla la cantidad de ahorros tras
# el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.
