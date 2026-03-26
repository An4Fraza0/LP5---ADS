# Escreva um algoritmo que forneça um menu para o usuário: 1-Cadastrar nome, 2- atualizar o nome, 3, excluir, 4-listar todos os cadastrados, ao final da operação deve dar uma mensagem indicando o resultado da operação e perguntando se deseja realizar
# outra operação, o seu aplicativo apenas deve encerrar quando a opção não for inserida.

nomes = []
while True:
    print("\n----- MENU ------")
    print("1 - cadastrar nome")
    print("2 - atualizar nome")
    print("3 - excluir nome")
    print("4 - listar nomes")
    opcao = input("escolha uma opção: ").strip()

    if opcao == "1":
        nome = input("nome: ").strip()
        if nome:
            nomes.append(nome)
            print("nome cadastrado com sucesso!")
        else:
            print("nome inválido.")
    elif opcao == "2":
        if not nomes:
            print("nenhum nome cadastrado.")
        else:
            print("lista de nomes:")
            for i, n in enumerate(nomes, 1):
                print(f"{i} - {n}")
            try:
                pos = int(input("posição para atualizar: ")) - 1
                if 0 <= pos < len(nomes):
                    novo = input("novo nome: ").strip()
                    if novo:
                        nomes[pos] = novo
                        print("nome atualizado!")
                    else:
                        print("nome inválido.")
                else:
                    print("posição inválida.")
            except ValueError:
                print("entrada inválida.")
    elif opcao == "3":
        if not nomes:
            print("nenhum nome cadastrado.")
        else:
            print("lista de nomes:")
            for i, n in enumerate(nomes, 1):
                print(f"{i} - {n}")
            try:
                pos = int(input("posição para excluir: ")) - 1
                if 0 <= pos < len(nomes):
                    removido = nomes.pop(pos)
                    print(f"'{removido}' excluído.")
                else:
                    print("posição inválida.")
            except ValueError:
                print("entrada inválida.")
    elif opcao == "4":
        if not nomes:
            print("nenhum nome cadastrado.")
        else:
            print("lista de nomes:")
            for i, n in enumerate(nomes, 1):
                print(f"{i} - {n}")
    else:
        print("opção inválida.")

    continuar = input("gostaria de realizar outra operação? (S/N): ").strip().upper()
    if continuar != "S":
        print("programa encerrado.")
        break