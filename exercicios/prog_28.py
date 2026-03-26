#  Escreva um programa que peça ao usuário para inserir uma palavra e verifique se ela tem mais de 5 letras.

palavra = input("digite uma palavra: ").strip()
print("a palavra tem mais de 5 letras" if len(palavra) > 5 else "a palavra tem 5 letras ou menos")