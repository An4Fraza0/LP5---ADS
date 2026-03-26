# Escreva um programa que pergunte ao usuário quantas vezes ele quer que uma mensagem seja exibida, e utilize um laço while para exibir a mensagem a quantidade de vezes desejada.

vezes = int(input("quantas vezes gostaria que a mensagem fosse exibida? "))
mensagem = input("digite sua mensagem: ")
i = 1
while i <= vezes:
    print(mensagem)
    i += 1