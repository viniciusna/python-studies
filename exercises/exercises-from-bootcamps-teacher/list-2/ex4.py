"""Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
Em seguida, calcule a média anual das temperaturas e mostre a média calculada juntamente com todas
as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: Exemplo de saída:
>> Meses com temperatura acima da média anual de 35,5°:
>> 1 – janeiro
>> 3 – março
>> 6 – junho
"""

months = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
averages = []

for month in months:
    averageTemperature = float(input(f"Temperatura média do mês de {month} (em °C): "))
    averages.append(averageTemperature)

averageAnnual = round(sum(averages) / len(averages), 2)

print(f"Meses com temperatura acima da média anual de {averageAnnual:.2f}°C")

for index, average in enumerate(averages):
    if averageAnnual < average:
        print(f"{index + 1} - {months[index]} com temperatura de {average}°C")
