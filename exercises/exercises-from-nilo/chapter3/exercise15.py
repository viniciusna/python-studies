"""Escreva um programa para calcular a redução do tempo de vida de um fumante.
Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
Considere que um fumante perde 10 minutos de vida a cada cigarro,
e calcule quantos dias de vida um fumante perderá. Exiba o total em dias.

Resposta:"""

cigarettesPerDay = int(input("Cigarros fumados por dia: "))
yearsSmoking = float(input("Quantos anos já fumou:  "))

minutesLost = 10*cigarettesPerDay*365*yearsSmoking

print(f"Perdeu {int(minutesLost/(60*24))} dias de vida")