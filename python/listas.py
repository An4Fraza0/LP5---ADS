# nome = 'nome qualquer'
# print(f'meu nome é {nome}')

# nome = 'nome qualquer v2'
# print(f'meu nome é {nome}')


# nomes = ['PUTALAKACHANGA', 'SALAMALEICO', 'BOMBACLAT']
# print(nomes[0])
# print(nomes[1])
# print(nomes[2])

# apostolos = ['PAULO', 'PEDRO', 'JOAO', 'TIAGO', 'MATHEUS']
# # percorrendo a lista posição por posição
# for apostolo in apostolos:
#     print(apostolo)

# apostolos.append('ANDRE') # adiciona um elemento no final da lista
# print(apostolos)

# apostolos.insert(2, 'FILIPE') # adiciona um elemento na posição desejada
# print(apostolos)

# expandindo a lista com novos elementos
notas = ['DO', 'RE']
print(notas)

notas.extend(['MI', 'FA', 'SOL', 'LA', 'SI']) # adiciona uma lista de elementos no final da lista
print(notas)

# excluindo itens de uma lista
notas.remove('DO') # remove o elemento desejado da lista (também é possível remover por nome do elemento)
print(notas)

notas.pop(2) # remove o elemento da posição desejada da lista
print(notas)

claves = ['DO', 'FA', 'FA', 'SOL']
print(claves)

# claves.remove('FA') # remove a primeira ocorrência do elemento desejado da lista
# print(claves)

for clave in claves:
    if clave == 'FA':
        claves.remove(clave)
print(claves)


# linha_pauta = [1, 2, 3, 4, 5,]
# linha_vazia = [4]
# for numero in linha_pauta:
#     if numero in linha_vazia:
#         linha_vazia.remove(numero)
# print(linha_vazia)


# numeros = [1, 2, 3, 4, 5]   
# impares = []
# pares = []


# for numero in numeros:
#     if numero % 2 != 0:
#         impares.append(numero)
#     elif numero % 2 == 0:
#         pares.append(numero)
# print(impares)
# print(pares)

# print(claves)
# claves.sort() # ordena a lista em ordem alfabética
# print(claves)

# claves.reverse() # inverte a ordem da lista
# print(claves)

# print(claves)
# claves.clear() # limpa a lista, deixando vazia
# print(claves)

# print(claves)
# del claves # deleta a lista completamente
# # print(claves) # isso vai gerar um erro, pois a lista foi deletada