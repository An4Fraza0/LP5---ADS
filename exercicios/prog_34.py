# Escreva um programa que peça ao usuário um número e verifique se ele é positivo, negativo ou zero.

num = float(input("insira um número: "))
if num > 0:
    print("o número é positivo")
elif num < 0:
    print("o número é negativo")
else:
    print("o número é zero")