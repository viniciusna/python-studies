"""Faça um programa que receba dois números inteiros do usuário, A e B e imprima na tela as seguintes operações:
•	A soma de A e B;
•	A diferença quando se subtrai B de A;
•	O produto (multiplicação) entre A e B;
•	O quociente (parte inteira da divisão) quando se divide A por B;
•	O resto da divisão entre A e B;
•	O resultado de log10 de A;
•	O resultado de A elevado a B;
"""
import math

A = int(input("Primeiro número: "))
B = int(input("Segundo número: "))

print(f"{A} + {B} = {A + B}")
print(f"{B} - {A} = {B - A}")
print(f"{A} * {B} = {A*B}")
print(f"A parte inteira da divisão {A}/{B} é {A//B} e seu resto é {A%B}")
print(f"log10(A) = {math.log10(A)}")
print(f"A^B = {A**B}")