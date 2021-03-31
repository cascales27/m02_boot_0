nombre = input("¿Cómo te llamas? ")
print("Hola, ", nombre)

strEdad = input("¿Cuantos años tienes? ")
strYear = input("¿En que año estamos? ")
strCumplidos = input("¿Cumpliste años ya este año? ")

edad = int(strEdad)
year = int(strYear)

if strCumplidos == "S":
    nacimiento = year - edad
else:
    nacimiento = year - edad -1
    
print(nombre, "naciste en", nacimiento)