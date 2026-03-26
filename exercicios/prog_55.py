# Desenvolva um programa que peça ao usuário para inserir um número maior que 100. Se o número for menor ou igual a 100, continue pedindo até que um número maior que 100 seja inserido.

while True:
    num = int(input("digite um número maior que 100: "))
    if num > 100:
        print("número válido!")
        break