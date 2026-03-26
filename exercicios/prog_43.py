# Desenvolva um programa que pergunte ao usuário quantas vezes ele quer que uma mensagem seja exibida, e depois use um for para imprimir essa mensagem repetidas vezes.

n_vezes = int(input("quantas vezes deseja repetir a mensagem? "))
msg = input("digite sua mensagem: ")
for _ in range(n_vezes):
    print(msg)