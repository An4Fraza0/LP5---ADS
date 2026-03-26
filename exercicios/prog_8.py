# Desenvolva um algoritmo que pergunte ao usuário o estado civil (solteiro, casado, divorciado, viúvo) e exiba uma mensagem correspondente.

estado_civil = input("qual é o seu estado civil? (solteiro, casado, divorciado, viúvo): ").lower()

if estado_civil == "solteiro":
    print("você está solto(a) na pixta (ou não).")
elif estado_civil == "casado":
    print("você é comprometido(a), uiui.")
elif estado_civil == "divorciado":
    print("você tem ex agora.")
elif estado_civil == "viúvo":
    print("você é viúvo(a), meus pesares.")
else:
    print("estado civil inválido... por gentileza, insira uma opção válida.")