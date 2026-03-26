# Crie um algoritmo que solicite ao usuário um número e continue pedindo outro número até que um número negativo seja inserido.

while True:
    num = int(input("digite um número (negativo para parar): "))
    if num < 0:
        print("fim.")
        break
