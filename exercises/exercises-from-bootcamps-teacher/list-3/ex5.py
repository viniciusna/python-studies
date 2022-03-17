"""Faça um programa que encontre as notas mínimas e máximas de um dicionário, e imprima-os na tela com as suas respectivas chaves.
Exemplo: dado o dicionário
>> {"Theodoro": 20, "Márcia": 50, "Júnior": 80}
A saída deve ser
>> Nota máxima -> Júnior : 80
>> Nota mínima -> Theodoro : 20
"""

grades = {"Theodoro": 20, "Márcia": 50, "Júnior": 80}

gradesOrdered = sorted(grades.items(), key = lambda tuple: tuple[1])

print(f"Nota máxima -> {gradesOrdered[-1][0]} : {gradesOrdered[-1][1]}")
print(f"Nota mínima -> {gradesOrdered[0][0]} : {gradesOrdered[0][1]}")