def tablaMult(n):
    try: resultado = int(n)
    except:
        resultado = None
    return resultado

numero = None
while numero == None:
    strNumero = input("Introduzca valor: ")
    numero = tablaMult(strNumero)
    
for i in range(1, 11):
    print("{} x {}".format(numero, i, numero * i))