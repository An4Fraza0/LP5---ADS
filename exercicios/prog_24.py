# Desenvolva um algoritmo que pergunte ao usuário o nome de uma cidade e verifique se é a capital do Brasil.

cidade = input("nome da cidade: ").strip().lower()
print("a cidade é a capital do Brasil" if cidade in ["brasília", "brasilia"] else "a cidade não é a capital do Brasil")