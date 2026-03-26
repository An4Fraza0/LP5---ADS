# Crie um algoritmo que solicite ao usuário uma cor (vermelho, verde, azul) e exiba uma mensagem correspondente à cor escolhida.

cor = input("escolha uma cor (vermelho, verde, azul): ").lower()

if cor == "vermelho":
    print("voce escolheu o vermelho... voce é a florzinha!")
elif cor == "verde":
    print("voce escolheu o verde... voce é a docinho!")
elif cor == "azul":
    print("voce escolheu o azul... voce é a lindinha!")
else:
    print("cor inválida. por gentileza, escolha entre vermelho, verde ou azul.")