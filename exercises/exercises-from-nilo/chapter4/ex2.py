"""Escreva um programa que pergunte a velocidade do carro de um usuário.
Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado.
Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.

Resposta:"""

velocity = float(input("Qual a velocidade? "))

if 80 < velocity:
    print(f"Multado em R${ 5*int((velocity - 80)) :.2f}")
else:
    print("Dentro do limite")