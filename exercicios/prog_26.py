# Desenvolva um algoritmo que peça ao usuário para inserir dois números e verifique se ambos são múltiplos de 5.

num1 = int(input("primeiro: "))
num2 = int(input("segundo: "))
print("ambos os números são múltiplos de 5" if num1 % 5 == 0 and num2 % 5 == 0 else "nenhum dos dois números são múltiplos de 5")