# Escreva um algoritmo que solicite ao usuário 5 números inteiros e calcule a soma desses números.


soma = 0
for i in range(1, 6):
    num = int(input(f"digite o {i}º número: "))
    soma += num
print(f"soma: {soma}")