# Desenvolva um algoritmo que peça ao usuário para digitar dois números e verifique se a multiplicação deles é igual a 20.

a = float(input("insira o primeiro número: "))
b = float(input("insira o segundo número: "))
prod = a * b
print("o resultado é igual a 20" if prod == 20 else "o resultado não é igual a 20")
