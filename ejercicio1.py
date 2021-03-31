# Entrada de datos
strNumero01 = input("Introduzca un número: ")
strNumero02 = input("Introduzca otro número: ")

# Procesamiento de datos
numero01 = int(strNumero01)
numero02 = int(strNumero02)

numero01 = numero01/10
numero02 = numero02/10

suma = round(numero01 + numero02, 2)
resta = round(numero01 - numero02, 2)
producto = round(numero01 * numero02, 2)
division = round(numero01 / numero02, 2)

# Salida de resultados
print(numero01, "+", numero02, "=", suma)
print(numero01, "-", numero02, "=", resta)
print(numero01, ".", numero02, "=", producto)
print(numero01, "/", numero02, "=", division)

