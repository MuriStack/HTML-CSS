def eh_primo(n):
    if n <= 1:
        print("Não é primo")
        return True
    
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            print("Não é primo")
            return True
    
    print("É primo")
    return False

eh_primo(5)
eh_primo(10)
