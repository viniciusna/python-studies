"""No exercício acima você calculou a área de um triângulo a partir da sua base e altura.
Faça um programa que receba os 3 lados de um triângulo – s1, s2 e s3 – e calcule sua área.
Compare a resposta com o exercício acima, dada das mesmas entradas. Os resultados devem ser idênticos."""

import math

s1 = float(input("Primeiro lado do triângulo: "))
s2 = float(input("Segundo lado do triângulo: "))
s3 = float(input("Terceiro lado do triângulo: "))

if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    s = (s1 + s2 + s3)/2
    area = math.sqrt(s*(s - s1)*(s - s2)*(s - s3))
    print(f"A área desse triângulo é {area}")
else:
    print("Não existe um triângulo com esses comprimentos de lados")