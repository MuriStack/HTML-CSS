def contar_digitos(n):
    n = abs(n)
    
    if n == 0:
        return 1
    
    contador = 0
    
    while n > 0:
        n //= 10
        contador += 1
    
    return contador

n = int(input("digite um número: "))
digitos = contar_digitos(n)
print(f"{n} tem {digitos} digitos")