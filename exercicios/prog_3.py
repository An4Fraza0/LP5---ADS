# Desenvolva um programa que pergunte ao usuário o dia da semana (número de 1 a 7) e exiba o nome do dia correspondente.

dias_da_semana = {
    1: "segunda-feira",
    2: "terça-feira",
    3: "quarta-feira",
    4: "quinta-feira",
    5: "sexta-feira",
    6: "sábado",
    7: "domingo"
}

numero = int(input("digite o número do dia da semana (1-7): "))

if numero in dias_da_semana:
    print(f"o dia é: {dias_da_semana[numero]}")
else:
    print("número inválido... por gentileza, digite um número entre 1 e 7.")