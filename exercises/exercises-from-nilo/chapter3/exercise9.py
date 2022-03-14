"""Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.

Resposta:"""

days = int(input("Quantidade de dias: "))
hours = int(input("Quantidade de horas: "))
minutes = int(input("Quantidade de minutos: "))
seconds = int(input("Quantidade de segundos: "))

timeInSeconds = seconds + minutes*60 + hours*3600 + days*86400

print(f"Esse tempo em segundos é: {timeInSeconds}")