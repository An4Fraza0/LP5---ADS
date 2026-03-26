# Escreva um algoritmo que peça ao usuário para inserir 5 números e, ao final, exiba o maior número inserido.

maior_num = int(input("digite o primeiro número: "))
for i in range(2, 6):
    num = int(input(f"digite o {i}º número: "))
    if num > maior_num:
        maior_num = num
print(f"maior número: {maior_num}")
