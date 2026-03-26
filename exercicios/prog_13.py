# Crie um algoritmo que solicite ao usuário um mês do ano (1 a 12) e exiba a estação do ano correspondente.

mes = int(input("digite o número do mês (1 a 12): "))

if mes in [12, 1, 2]:
    print("verão")
elif mes in [3, 4, 5]:
    print("outono")
elif mes in [6, 7, 8]:
    print("inverno")
elif mes in [9, 10, 11]:
    print("primavera")
else:
    print("mês inválido.")