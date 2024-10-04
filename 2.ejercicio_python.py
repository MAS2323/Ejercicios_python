# Ejercicios de Cadenas
# Ejercicio 1
# Escribir un programa que pregunte el nombre del usuario en la consola
# y un número entero e imprima por pantalla en líneas distintas el nombre
# del usuario tantas veces como el número introducido.

"""nombreUsuario = input("Cual es su nombre de usuario? ")
numEnterImpar = int(input("Introduzca un numero entero e impar: "))

for numEnterImpar in nombreUsuario:
    print(nombreUsuario)"""
nombre = input("¿Cómo te llamas? ")
n = input("Introduce un número entero: ")
print((nombre + "\n") * int(n))

# Ejercicio 2
# Escribir un programa que pregunte el nombre completo del usuario en la
# consola y después muestre por pantalla el nombre completo del usuario
# tres veces, una con todas las letras minúsculas, otra con todas las letras
# mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula.
# El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

nombre = input("Introduzca su nombre completo: ")
print(nombre.lower())  # minusculas
print(nombre.upper())  # Mayuscula
# usamos la funcion titile() para hacer que las primeras letras esten en mayuscula
print(nombre.title())

# Ejercicio 3
# Escribir un programa que pregunte el nombre del usuario en la consola y después de
# que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras,
# donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras
# que tienen el nombre.

miNombre = input("Introduzca su nombre: ")
print(f"{miNombre.upper()} tiene {len(miNombre)} letras")

# Ejercicio 4
# Los teléfonos de una empresa tienen el siguiente formato
# prefijo-número-extension donde el prefijo es el código del
# país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56).
# Escribir un programa que pregunte por un número de teléfono con este
# formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
numTel = input(
    "Introduce un numero de telefono con el siguiente formato +xx-xxxxxxxxx-xx: ")
print("El numero de telefono es: ", numTel[4: -3])

# Ejercicio 5
# Escribir un programa que pida al usuario que introduzca una frase en la consola y
# muestre por pantalla la frase invertida.

frase = input("Introduzca una frace: ")
print(frase[:: -1])

# Ejercicio 6
# Escribir un programa que pida al usuario que introduzca una frase en la consola y
# una vocal, y después muestre por pantalla  la misma frase pero con la vocal introducida en mayúscula.

"""frace = input('Introduce una frace por consola y una vocal: ')
voacl = input('Introduce una vocal: ')

print(f'{frase} {voacl.upper()}')
"""

frase = input("Introduce una frase: ")
vocal = input("Introduce una vocal en minúscula:  ")
print(frase.replace(vocal, vocal.upper()))

# Ejercicio 7
# Escribir un programa que pregunte el correo electrónico del usuario en
# la consola y muestre por pantalla otro correo electrónico con el mismo nombre
# (la parte delante de la arroba @) pero con dominio ceu.es.

email = input("Introduce tu correo electrónico: ")
print(email[:email.find('@')] + '@ceu.es')

correo = input('Introduzca su correo electronico: ')
resul = correo.replace("@", '@ceu.es')

print(resul)

# Ejercicio 8
# Escribir un programa que pregunte por consola el precio de un producto en euros
# con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.

precio = input("Introduce el precio del producto con dos decimales:  ")
print(precio[:precio.find('.')], 'euros y',
      precio[precio.find('.')+1:], 'céntimos.')
