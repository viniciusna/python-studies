"""Escreva uma expressão para determinar se uma pessoa deve ou não pagar imposto. Considere que pagam imposto pessoas cujo salário é maior que R$ 1.200,00.

Resposta:"""

print("Exercício 4")

print("")
wage = 1200

if wage > 1200:
    print("Paga imposto")
else:
    print("Não paga imposto")

"""Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado. Para ser aprovado, todas as médias do aluno devem ser maiores que 7. Considere que o aluno cursa apenas três matérias, e que a nota de cada uma está armazenada nas seguintes variáveis: matéria1, matéria2 e matéria3.

Resposta:"""

print("Exercício 6")

materia1 = 7.1
materia2 = 8
materia3 = 9

if materia1 > 7 and materia2 > 7 and materia3 > 7:
    print("Aluno aprovado")
else:
    print("Aluno não aprovado")