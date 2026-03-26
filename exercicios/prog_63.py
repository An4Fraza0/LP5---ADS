# Desenvolva um algoritmo que peça ao usuário para inserir 5 números, adicione-os a uma lista e, depois, exiba a soma de todos os números na lista.

numeros = []
for i in range(5):
    num = int(input(f"número {i+1}: "))
    numeros.append(num)
soma = sum(numeros)
print(f"soma: {soma}")
