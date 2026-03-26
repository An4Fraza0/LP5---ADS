#  Desenvolva um programa que peça ao usuário um tipo de combustível (gasolina, etanol, diesel) e exiba o preço correspondente por litro.

combustivel = input("digite o tipo de combustível (gasolina, etanol, diesel): ").strip().lower()

precos = {
    "gasolina": 6.65,
    "etanol": 5.49,
    "diesel": 6.20
}

if combustivel in precos:
    print(f"preço: R$ {precos[combustivel]:.2f} por litro")
else:
    print("inválido... por gentileza, escolha entre gasolina, etanol ou diesel.")