# Desenvolva um algoritmo que peça ao usuário para digitar um número e verifique se ele é múltiplo de 2 ou de 5.

num = int(input("digite um número: "))
if num % 2 == 0 or num % 5 == 0:
    print("o número é múltiplo de 2 ou de 5")
else:
    print("o número não é múltiplo nem de 2 nem de 5")