# Crie um programa que peça ao usuário para inserir um número e, em seguida, exiba os números de 1 até esse número, mas de forma decrescente.


num = int(input("digite um número: "))
for i in range(num, 0, -1):
    print(i)