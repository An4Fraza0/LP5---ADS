# Escreva um programa que peça ao usuário para escolher um modo de transporte (carro, bicicleta, a pé) e exiba uma mensagem com a velocidade média correspondente.

transporte = input("escolha um modo de transporte (carro, bicicleta, a pé): ").strip().lower()

match transporte:
    case "carro":
        print("velocidade média do carro: 60 km/h")
    case "bicicleta":
        print("velocidade média da bicicleta: 15 km/h")
    case "a pé" | "apé" | "pe":
        print("velocidade média a pé: 5 km/h")
    case _:
        print("opção inválida... por gentileza, escolha entre carro, bicicleta ou a pé.")
