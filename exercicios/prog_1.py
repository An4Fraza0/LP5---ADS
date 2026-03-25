# Crie um programa que pergunte ao usuário um número de 1 a 3 e exiba o nome correspondente ao número (1: "um", 2: "dois", 3: "três")
def obter_nome_por_numero(numero):
    if numero == 1:
        return "um"
    
    elif numero == 2:
        return "dois"
    
    elif numero == 3:
        return "três"
    
    else:
        return "Número inválido. Por gentileza, insira um número de 1 a 3."
    
try:
    numero_usuario = int(input("Digite um número de 1 a 3: "))

    nome_correspondente = obter_nome_por_numero(numero_usuario)
    print(nome_correspondente)
    
except ValueError:
    print("Por gentileza, insira um número válido.")
