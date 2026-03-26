# Escreva um programa que solicite ao usuário para digitar dois números e verifique se o primeiro é maior que o segundo. Continue pedindo números até que o primeiro número seja maior que o segundo.

while True:
    a = float(input("digite o primeiro número: "))
    b = float(input("digite o segundo número: "))
    if a > b:
        print("agora o primeiro é maior que o segundo.")
        break
