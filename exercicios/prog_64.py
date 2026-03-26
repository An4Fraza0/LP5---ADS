# Crie uma lista com 10 números aleatórios e exiba apenas os números que são múltiplos de 3.

import random
lista = [random.randint(1, 100) for _ in range(10)]
print("números múltiplos de 3:")
for num in lista:
    if num % 3 == 0:
        print(num)
