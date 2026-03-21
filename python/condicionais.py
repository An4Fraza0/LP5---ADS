# condicionais if, elif e else
#acompanhada = False
#idade = 18

# if idade >= 18:
#     print('você pode entrar para assistir o filme')

# elif idade <= 17 and not acompanhada:
#     print('você não pode entrar para assistir o filme, somente com acompanhante')

# elif idade <= 17 and acompanhada:
#     print('você pode entrar para assistir o filme')

# ctrl + K + C para comentar o código (método KACETE)
# ctrl + K + U para descomentar o código (método KU)

# if idade < 0:
#     print('idade invalida')
# elif idade <= 17: 
#     print('você é menor de idade')
# elif idade <= 65:
#     print('você é adulto')
# else:
#     print('você é idoso')

# match case 

print('qual sua opção desejada? 0 cadastrar, 1 editar, 2 excluir, 3 consultar ou 4 sair')
opcao = int(input('Digite sua opção: '))

match opcao:
    case 0:
        print('0 - cadastrar')
    case 1:
        print('1 - editar')
    case 2:
        print('2 - excluir')
    case 3:
        print('3 - consultar')
    case 4:
        print('4 - sair')