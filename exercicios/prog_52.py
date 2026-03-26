# Desenvolva um algoritmo que solicite ao usuário uma senha e continue pedindo até que a senha correta "1234" seja digitada.

while True:
    senha = input("digite a senha: ")
    if senha == "1234":
        print("acesso concedido!")
        break
