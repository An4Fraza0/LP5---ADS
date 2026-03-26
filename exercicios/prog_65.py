# Escreva um programa que solicite ao usuário uma lista de 5 números e exiba o maior e o menor número dessa lista.

numeros = []
for i in range(5):
    num = float(input(f"número {i+1}: "))
    numeros.append(num)
print(f"maior: {max(numeros)}")
print(f"menor: {min(numeros)}")