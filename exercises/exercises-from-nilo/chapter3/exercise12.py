"""Escreva um programa que calcule o tempo de uma viagem de carro.
Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

Resposta:"""

distance = float(input("Distância a percorrer (em km): "))
averageVelocity = float(input("Velocidade média (em km/h): "))

totalTimeInHours = distance/averageVelocity
hoursTravel = int(totalTimeInHours)

print(f"O tempo de viagem esperado é de {hoursTravel} horas e { (totalTimeInHours - hoursTravel)*60 :.2f} minutos")
