"""Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar.
O valor da prestação mensal não pode ser superior a 30% do salário.
Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

Resposta:"""

homeValue = float(input("Valor da casa: R$"))
wage = float(input("Salário: R$"))
yearsToPay = int(input("Quantos anos para pagar? "))

installment = homeValue/(12*yearsToPay)

if installment <= 0.3*wage:
    print(f"Empréstimo aprovado, parcelas de R${installment:.2f}")
else:
    print("Empréstimo não foi aprovado")