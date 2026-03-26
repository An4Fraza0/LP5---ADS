# Crie um programa que peça ao usuário um número e exiba todos os divisores desse número.

num = int(input("digite um número: "))
print("divisores:")
for i in range(1, num+1):
    if num % i == 0:
        print(i)