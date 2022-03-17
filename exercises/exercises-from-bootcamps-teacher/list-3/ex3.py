"""Faça um programa que ordene um dicionário por seus valores. Exemplo: dado o dicionário
>> {" matemática" : 81, " física" : 83, " química" : 87} 
a saída deve ser 
>> {" química" : 87, " física" : 83, matemática" : 81}
"""

grades = {" matemática" : 81, " física" : 83, " química" : 87}

gradesSorted = sorted(grades.items(), key = lambda tuple: tuple[1], reverse = True)
gradesSorted = dict(gradesSorted)

print(gradesSorted)