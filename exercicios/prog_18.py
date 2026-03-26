# Faça um programa que peça ao usuário três números e verifique se todos são positivos.

num1 = float(input("digite o primeiro número: "))
num2 = float(input("digite o segundo número: "))
num3 = float(input("digite o terceiro número: "))

if num1 > 0 and num2 > 0 and num3 > 0:
    print("todos os números são positivos.")
else:
    print("nem todos os números são positivos.")