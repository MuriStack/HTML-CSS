def calculadora(n1,n2,operation):
    if operation == "+":
        print(f"Soma dos números: {n1+n2}")
    elif operation == "-":
        print(f"Subtração dos números: {n1-n2}")
    elif operation == "*":
        print(f"Multiplicação dos números: {n1*n2}")
    elif operation == "/":
        print(f"Divisão dos números: {n1/n2}")
    else:
        print("Operação inválida")

calculadora(2,3,"+")
calculadora(2,3,"-")
calculadora(2,3,"*")
calculadora(2,3,"/")
