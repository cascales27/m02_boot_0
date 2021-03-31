p1='amor'
p2='roma'

listaComparacionLetras = []

for caracter1 in p1:
    noAñadasFalse = False
    for caracter2 in p2:
        if caracter1 == caracter2:
            noAñadasFalse = True
            listaComparacionLetras.append(True)
            
    if not noAñadasFalse:
        listaComparacionLetras.append(False)
        
if False in listaComparacionLetras:
    print('No es un anagrama')
else:
    print('Es un anagrama')