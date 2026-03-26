# Faça um programa que solicite ao usuário dois números e verifique se ambos são pares.

num1 = int(input("digite o primeiro número: "))
num2 = int(input("digite o segundo número: "))

if num1 % 2 == 0 and num2 % 2 == 0:
    print("os dois números são pares.")
else:
    print("um dos números não é par.")