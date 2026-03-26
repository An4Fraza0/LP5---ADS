# Desenvolva um programa que pergunte ao usuário uma operação matemática (+, -, *, /) e dois números, e realize a operação escolhida.

operacao = input("digite a operação desejada (+, -, *, /): ").strip()
try:
    op1 = float(input("digite o primeiro número: ").strip())
    op2 = float(input("digite o segundo número: ").strip())
except ValueError:
    print("inválido... use números.")
else:
    if operacao == "+":
        print(op1 + op2)
    elif operacao == "-":
        print(op1 - op2)
    elif operacao == "*":
        print(op1 * op2)
    elif operacao == "/":
        if op2 == 0:
            print("erro: divisão por zero.")
        else:
            print(op1 / op2)
    else:
        print("operacao inválida.")