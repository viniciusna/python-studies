"""Escreva um programa que receba uma string e diga se ela tem o formato de uma placa veicular brasileira
(no formato antigo) com três letras, um traço e quatro números. Exemplos: 
•    Dada a entrada ABT-1234 o programa deveria exibir True
•    Dada a entrada JKL9999 o programa deveria exibir False
•    Qualquer outra entrada que fuja do padrão de 3 letras, um traço e quatro números, o programa deverá exibir False 
"""

userInput = input(f"Digite uma sequência de letras e números no formato de uma placa veicular brasileira:\n")

isAPlate = True

if len(userInput) != 8:
    print("Não tem formato de placa de carro")
elif userInput[0:3].isupper() and userInput[3] == '-' and userInput[4:8].isnumeric():
    print("Possui o formato de placa de carro")
else:
    print("Não tem formato de placa de carro")
