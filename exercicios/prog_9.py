# Crie um algoritmo que verifique se um número inserido pelo usuário é ímpar ou par.

numero = int(input("digite um número: "))

if numero % 2 == 0:
    print(f"o número {numero} é PAR")
else:
    print(f"o número {numero} é ÍMPAR")