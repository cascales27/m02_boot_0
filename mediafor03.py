notas = (2, 4, 6, 8)

suma = 0
longNotas = len(notas)
for indice in range(0, longNotas):
    suma = suma + notas [indice]
    
media = suma /longNotas

# Presentar la media
print("Numero de items: ", longNotas)
print("Nota total.....: ", suma)
print("Nota Media.....: ", media)
    
    