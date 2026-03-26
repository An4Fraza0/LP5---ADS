# Escreva um programa que peça ao usuário para inserir três números e verifique se todos são iguais.

a = float(input("insira o primeiro número: "))
b = float(input("insira o segundo número: "))
c = float(input("insira o terceiro número: "))
print("todos os números são iguais" if a == b == c else "os números não são todos iguais")
