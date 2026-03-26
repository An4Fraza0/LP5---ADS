# Crie um programa que solicite ao usuário a temperatura em graus Celsius e converta para Fahrenheit.

celsius = float(input("digite a temperatura em graus celsius(°C): "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C equivalem a {fahrenheit}°F.")