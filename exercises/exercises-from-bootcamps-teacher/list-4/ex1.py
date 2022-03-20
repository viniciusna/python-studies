"""Escreva um programa que diga se um número dado pelo usuário é par ou ímpar"""

number = int(input("Insira um número inteiro: "))

if number%2 == 0:
    print(f"O número {number} é par")
else:
    print(f"O número {number} é ímpar")