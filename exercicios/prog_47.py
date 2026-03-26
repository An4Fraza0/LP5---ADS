# Crie um programa que peça ao usuário um número e exiba a tabuada desse número de 1 a 10.

num = int(input("digite um número: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
