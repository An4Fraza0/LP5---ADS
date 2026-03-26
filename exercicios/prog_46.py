# Desenvolva um programa que pergunte ao usuário para inserir 10 números e, ao final, exiba a média dos números inseridos.

soma = 0
for i in range(1, 11):
    num = int(input(f"digite o {i}º número: "))
    soma += num
media = soma / 10
print(f"média: {media}")
