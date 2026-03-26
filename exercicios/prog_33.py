# Crie um programa que solicite ao usuário o valor de um produto e calcule o desconto de 10%.

valor = float(input("insira o valor do produto: R$ "))
desconto = valor * 0.10
final = valor - desconto
print(f"o desconto é de: R$ {desconto:.2f}")
print(f"o valor final é de: R$ {final:.2f}")
