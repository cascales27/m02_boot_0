def esDdecimal(numero):
    try:
        float(numero)
        return True
    except:
        return False
    
B = input("Base del triangulo: ")
if esDecimal(B):
    b = float(B)
    
    H = input("Altura del triangulo: ")
    
    if esDecimal(H):
        h = float(H)
        area = b * h / 2
    
        print("superficie del triangulo:", round(area, 2))
    
    else:
        print(H, "debe ser un numero")
else:
    print(B, "debe ser un numero")
    