"""Escreva um programa que leia três números e que imprima o maior e o menor.

Resposta:"""

n1 = float(input("Primeiro número: "))
n2 = float(input("Segundo número: "))
n3 = float(input("Terceiro número: "))

greater = n1
smaller = n2

if greater < n2:
    greater = n2

if greater < n3:
    greater = n3

if n1 < smaller:
    smaller = n1

if n3 < smaller:
    smaller = n3

print(f"O menor número é {smaller} e o maior é {greater}")