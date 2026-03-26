# Escreva um programa que peça ao usuário um número de 0 a 20 e verifique se ele está entre 10 e 15.

num = int(input("escolha um número (0-20): "))
print("o número está entre 10 e 15" if 10 <= num <= 15 else "o número não está entre 10 e 15")