"""Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário,
assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.

Resposta:"""

rentDays = int(input("Quantidade de dias que o carro foi alugado: "))
kmTraveled = int(input("Quantidade de km percorridos: "))

print(f"Preço a pagar: R${ 60*rentDays + 0.15*kmTraveled:.2f}")