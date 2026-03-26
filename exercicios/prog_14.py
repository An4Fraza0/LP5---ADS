# Desenvolva um algoritmo que peça ao usuário para digitar dois números e verifique se a soma deles é maior que 100.

num1 = float(input("digite o primeiro número: "))
num2 = float(input("digite o segundo número: "))
soma = num1 + num2

if soma > 100:
    print(f"a soma ({soma}) é maior que 100.")
else:
    print(f"a soma ({soma}) não é maior que 100.")