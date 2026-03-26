# Escreva um algoritmo que peça ao usuário para digitar um número e verifique se ele é maior, menor ou igual a 10.

num = float(input("digite um número: "))
if num > 10:
    print("o número é maior que 10")
elif num < 10:
    print("o número é menor que 10")
else:
    print("o número é igual a 10")