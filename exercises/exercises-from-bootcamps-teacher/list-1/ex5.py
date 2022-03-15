"""Escreva um programa que leia do usuário um número de 4 dígitos e imprima a soma destes dígitos.
Exemplo, se o usuário digitar 3141 seu programa deverá imprimir na tela 
3+1+4+1=9
3+1+4+1=9"""

number = input("Insira um número de 4 dígitos: ")

if len(number) == 4:
    print(f"{int(number[0])} + {int(number[1])} + {int(number[2])} + {int(number[3])} = {int(number[0]) + int(number[1]) + int(number[2]) + int(number[3])}")
else:
    print("Tem que digitar um número com 4 dígitos :(")