# Desenvolva um algoritmo que solicite ao usuário uma palavra e continue pedindo outra palavra até que ele digite "sair".

while True:
    palavra = input("digite uma palavra (ou escreva 'sair' para terminar): ").strip().lower()
    if palavra == "sair":
        print("programa encerrado.")
        break