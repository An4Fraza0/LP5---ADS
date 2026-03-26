# Crie um algoritmo que peça ao usuário uma palavra e verifique se a palavra é "Python".

palavra = input("digite uma palavra: ").strip()
print("a palavra é python" if palavra.lower() == "python" else "a palavra não é python")