"""Escreva um programa para encontrar o tamanho do comprimento das strings nos valores de dicionário. Exemplo: dada o dicionário
>> {1: "vermelho", 2: "azul", 3: "marrom"}
A saída deverá ser
>> {1: 8, 2: 4, 3: 6}
"""

dictionary = {1: "vermelho", 2: "azul", 3: "marrom"}
response = {}

for key in dictionary:
    elementLength = len(dictionary[key])
    response[key] = elementLength

print(response)