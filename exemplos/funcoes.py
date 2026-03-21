def soma(num1, num2):
    """Função que recebe dois números e retorna a soma deles."""
    soma = num1 + num2
    print(f'A soma de {num1} e {num2} é {soma}')
    return soma

def sub(num1, num2):
    """Função que recebe dois números e retorna a subtração deles."""
    sub = num1 - num2
    print(f'A subtração de {num1} e {num2} é {sub}')
    return sub

def menu ():
    print('1 - Soma')
    print('2 - Subtração')
    print('o que deseja fazer?')
    return input()
