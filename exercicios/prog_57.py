# Crie um programa que peça ao usuário para adivinhar um número secreto entre 1 e 10. Continue pedindo até que ele adivinhe o número corretamente.

import random
secreto = random.randint(1, 10)
print("tente adivinhar o número secreto (1-10): ")
while True:
    palpite = int(input("seu palpite: "))
    if palpite == secreto:
        print("parabéns! acertou!")
        break
    print("errooou! tente de novo.")