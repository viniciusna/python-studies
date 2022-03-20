"""Escreva um programa que receba dois números e imprima na tela se o primeiro é divisível pelo segundo."""

number1 = int(input("Insira um número inteiro: "))
number2 = int(input("Insira outro número inteiro: "))

if number1 % number2 == 0:
    print(f"{number1} é divisível por {number2} e dá {number1/number2}")
else:
    print(f"{number1} não é divisível por {number2}")