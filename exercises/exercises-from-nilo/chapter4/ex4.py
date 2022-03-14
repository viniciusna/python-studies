"""Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento.
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.

Resposta:"""

wage = float(input("Qual o salário? "))

if wage <= 1250:
    print(f"O seu aumento foi de R${ wage*0.15:7.2f}")
else:
    print(f"O seu aumento foi de R${ wage*0.1:7.2f}")
