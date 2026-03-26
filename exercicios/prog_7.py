# Escreva um programa que peça ao usuário uma nota de 0 a 10 e classifique a nota como "Baixa", "Média" ou "Alta" usando estrutura condicional if.

nota = float(input("digite uma nota de 0 a 10: "))

if nota < 0 or nota > 10:
    print("nota inválida! Digite um valor entre 0 e 10.")
elif nota < 6:
    print("classificação: baixa")
elif nota < 7:
    print("classificação: média")
else:
    print("classificação: alta")