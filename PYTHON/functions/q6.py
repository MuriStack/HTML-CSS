def fatorial(n):
    fatorial = 1
    if n < 0:
        print("Número negativo")
    if n == 0:
        print(f"Fatorial de {n} é: 1")
    
    for i in range (1,n+1):
        fatorial *= i

    print(f"Fatorial de {n} é: {fatorial}")

fatorial(5)