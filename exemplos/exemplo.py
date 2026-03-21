import os
from funcoes import soma, sub, menu

continuar = 's'
while continuar != 'n':
    os.system('cls') 
    opcao = menu() # Limpa a tela (use 'cls' no Windows e 'clear' no Linux/Mac)

    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))

    if opcao == '1':
        soma(num1, num2)

    elif opcao == '2':
        sub(num1, num2)

    else:
        print('Opção inválida. Por favor, escolha 1 ou 2.')

    continuar = input('Deseja continuar? (s/n) ')
