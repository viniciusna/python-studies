"""Faça um programa que calcule o aumento de um salário.
Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.

Resposta:"""

wage = float(input("Insira o salário: "))
increaseRate = float(input("Aumento em porcetagem (insira só o número, sem o símbolo %): "))

print(f"O reajuste salarial foi de {increaseRate}% e o salário agora é de R${ wage*(1 + increaseRate/100) : .2f}")