# Escreva um algoritmo que peça ao usuário o nome de uma fruta e verifique se a fruta é uma maçã.

fruta = input("digite o nome de uma fruta: ").strip().lower()

if fruta in ["maçã", "maca", "maça"]:
    print("a fruta é uma maçã.")
else:
    print("a fruta não é uma maçã.")