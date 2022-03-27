"""Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas.
A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as
notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição
acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes).
As notas não são informadas ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo: 

Atleta: Aparecido Parente 

Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final: 

Atleta: Aparecido Parente 

Melhor nota: 9.9 

Pior nota: 7.5 """

name = input("Nome do atleta: ")
grades = []

for i in range(7):
    grade = float(input(f"Digite a {i + 1}º nota: "))
    grades.append(grade)

highestGrade = max(grades)
lowestGrade = min(grades)

average = ( sum(grades) - highestGrade - lowestGrade ) / ( len(grades) - 2 )

print(f"Atleta: {name} \n")

for grade in grades:
    print(f"Nota: {grade : .2f}")

print(f"\nResultado final: {average}")
print(f"Melhor nota: {highestGrade}")
print(f"Pior nota: {lowestGrade}")
