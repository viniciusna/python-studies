"""Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto.
Exiba o valor do desconto e o preço a pagar.

Resposta:"""

price = float(input("Insira o valor do produto: R$"))
discount = float(input("Insira a porcetagem do desconto (apenas números, sem o símbolo %): "))

print(f"O desconto foi de {discount}% e o preço a pagar é R${ price*(1 - discount/100) if discount < 100 else 0.00 : .2f}")