from random import randint as r

def jogo_adivinhacao():
    contador = 0
    numero_aleatorio = r(0, 100)
    tentativa = int(input("tente acertar um número entre 0 e 100"))

    while True:
        if tentativa > numero_aleatorio:
            print("Alto")
            contador += 1

        elif tentativa < numero_aleatorio:
            print("Baixo")
            contador += 1
        
        else:
            print("Parabéns você acertou")
            contador += 1
            break
        
        tentativa = int(input("tente acertar um número entre 0 e 100"))
    
    print(f"Você acertou em {contador} tentativas")
