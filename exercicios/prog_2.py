# Escreva um programa que peça ao usuário para inserir um número e verifique se o número é maior que 10.

numero = float(input("digite um número: "))

if numero > 10:
    print(f"o número inserido: {numero} é maior que 10")
else:
    print(f"o número inserido: {numero} é menor ou igual a 10")