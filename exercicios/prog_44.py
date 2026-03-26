# Crie um programa que peça ao usuário 10 números e exiba apenas os números pares.

for i in range(1, 11):
    num = int(input(f"digite o {i}º número: "))
    if num % 2 == 0:
        print(f"{num} é par")