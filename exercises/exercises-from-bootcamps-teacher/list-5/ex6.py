"""Sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, faça um programa que calcule o valor de H com N termos. """

terms = int(input('Quantos termos serão usados? '))

h = 0
n = 1

while n <= terms:
    h += 1/n
    n += 1

print(h)