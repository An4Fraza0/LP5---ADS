# Escreva um programa que pergunte ao usuário uma idade e verifique se a pessoa é adolescente (entre 13 e 17 anos).

idade = int(input("digite a idade: "))

if 13 <= idade <= 17:
    print("a pessoa é adolescente.")
else:
    print("a pessoa não é adolescente.")
