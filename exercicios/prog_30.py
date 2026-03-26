# Faça um programa que pergunte ao usuário a idade e verifique se ele pode votar (idade maior ou igual a 16).

idade = int(input("insira a idade: "))
print("pode votar" if idade >= 16 else "não pode votar")
