"""Escreva um programa que converta uma temperatura digitada em °C em °F. A fórmula para essa conversão é:

     9 × C
 F = ----- + 32
       5

Resposta:"""

celsiusTemperature = float(input("Insira a temperatura em Celsius: "))

print(f"A temperatura em Fahrenheit é { 9*celsiusTemperature/5 + 32 }°F")