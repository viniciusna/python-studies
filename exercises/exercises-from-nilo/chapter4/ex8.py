"""Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar.
Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/).
Exiba o resultado da operação solicitada.

Resposta:"""

n1 = float(input("Primeiro número: "))
n2 = float(input("Segundo número: "))
operation = input(f"Qual operação? \n 1-soma \n 2-subtração \n 3-multiplicação \n 4-divisão \n")

if operation == '1':
    print(f" {n1} + {n2} = {n1 + n2} ")
elif operation == '2':
    print(f" {n1} - {n2} = {n1 - n2} ")
elif operation == '3':
    print(f" {n1} * {n2} = {n1 * n2} ")
else:
    print(f" {n1} / {n2} = {n1 / n2} ")