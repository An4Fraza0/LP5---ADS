# Crie um programa que solicite ao usuário um número de 1 a 12 e exiba o mês correspondente.

meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho",
         "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

num = int(input("digite um número de 1 a 12: "))
if 1 <= num <= 12:
    print(meses[num-1])
else:
    print("número inválido... por gentileza, insira um número de 1 a 12.")