# Desenvolva um programa que peça ao usuário para inserir 7 números e, ao final, exiba quantos desses números são maiores que 10.

cont = 0
for i in range(1, 8):
    num = int(input(f"digite o {i}º número: "))
    if num > 10:
        cont += 1
print(f"quantidade de números maiores que 10: {cont}")