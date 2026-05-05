def fatorial(n):
    if n < 0:
        return None
    
    fatorial = 1

    for i in range (1,n+1):
        fatorial *= i

    return fatorial

def binomio(n,p):
    coeficiente = fatorial(n) / (fatorial(p) * fatorial(n - p))
    print(f"Coeficiente binomial: {coeficiente}")

binomio(5,2)