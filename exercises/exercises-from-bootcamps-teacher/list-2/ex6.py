"""Faça um programa que remova strings vazias de uma lista de strings. Exemplo:
dada a lista ["Olá", "", "meu", "nome", "", "é", "facilitador", ""] a saída deve ser
>> ["Olá", "meu", "nome", "é", "facilitador"]
"""

array = ["Olá", "", "meu", "nome", "", "é", "facilitador", ""]

for element in array:
    if element == "":
        array.remove("")

print(array)

#Outra forma de fazer que pensei
"""try:
    for element in array:
        array.remove("")
        print(array)
except:
    print(array)"""