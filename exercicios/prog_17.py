# Crie um programa que solicite ao usuário dois números e exiba a soma, subtração, multiplicação e divisão entre eles.

num1 = float(input("digite o primeiro número: "))
num2 = float(input("digite o segundo número: "))

print(f"- soma: {num1 + num2}")
print(f"- subtração: {num1 - num2}")
print(f"- multiplicação: {num1 * num2}")

if num2 != 0:
    print(f"- divisão: {num1 / num2}")
else:
    print("não é possível dividir (divisão por zero).")