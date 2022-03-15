"""Faça um programa que receba do usuário seu peso em kg e altura em metros e imprima o
Índice de Massa Corporal (IMC) do usuário."""

weight = float(input("Qual o seu peso (em Kg)? "))
height = float(input("Qual a sua altura (em metros)? "))

print(f"Seu IMC é {weight/height**2}")