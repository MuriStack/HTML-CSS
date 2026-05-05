def conversor_moeda(BRL,taxa):
    USD = BRL * taxa
    print(f"Valor de reais em dolar: ${USD:.1f}")

conversor_moeda(5,0.20)