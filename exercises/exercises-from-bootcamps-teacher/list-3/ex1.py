"""Digamos que existam 2 cursos de idiomas em uma escola, inglês e francês, e que existam alunos matriculados conforme abaixo:
•    Alunos matriculados em inglês:
o    João Alves dos Santos
o    Maria Magalhães
o    Antônio da Silva Ferreira
o    José Júnior Jarbas
o    Henrique da Silva Sauro
o    Joaquina Ferreira da Silva
o    Fabiana Aparecida Bianco
o    Marrone Gutierres
o    Carlos Magno Farad
o    Antônio da Silva Júnior Amaral

•    Alunos matriculados em francês:
o    João Alves dos Santos
o    Antônio da Silva Ferreira
o    Fernanda Abdala Mohamed
o    Abner Mignon Alib
o    Alisson Figueiredo
o    Henrique da Silva Sauro
o    Maria Magalhães
o    Marrone Gutierres
o    Joaquina Ferreira da Silva

Faça um programa que responda as seguintes perguntas:

1.    Quantos alunos estão matriculados na escola, no total?
2.    Quantos e quais estão matriculados APENAS em INGLES?
3.    Quantos e quais estão matriculados APENAS em FRANCES?
4.    Quantos e quais estão matriculados EM AMBOS os cursos?
5.    Quantos alunos estão matriculados somente em francês ou somente em inglês, mas não em ambos os cursos?
"""

englishClass = {"João Alves dos Santos", "Maria Magalhães", "Antônio da Silva Ferreira", "José Júnior Jarbas",
"Henrique da Silva Sauro", "Joaquina Ferreira da Silva", "Fabiana Aparecida Bianco", "Marrone Gutierres",
"Carlos Magno Farad", "Antônio da Silva", "Júnior Amaral"}

frenchClass = {"João Alves dos Santos", "Antônio da Silva Ferreira", "Fernanda Abdala Mohamed",
"Abner Mignon Alib", "Alisson Figueiredo", "Henrique da Silva Sauro", "Maria Magalhães", "Marrone Gutierres", "Joaquina Ferreira da Silva"}

print("Quantos alunos estão matriculados na escola, no total?")
print(f"{ len(englishClass | frenchClass) } \n")

print("Quantos e quais estão matriculados APENAS em INGLES?")

print(f"{len(englishClass)} alunos")
for student in englishClass:
    print(student)
print()


print("Quantos e quais estão matriculados APENAS em FRANCES?")

print(f"{len(frenchClass)} alunos")
for student in frenchClass:
    print(student)
print()


print("Quantos e quais estão matriculados EM AMBOS os cursos?")

intersection = englishClass & frenchClass

print(f"{len(intersection)} alunos")
for student in intersection:
    print(student)
print()


print("Quantos alunos estão matriculados somente em francês ou somente em inglês, mas não em ambos os cursos?")

studentsInJustOneCourse = englishClass ^ frenchClass

print(f"{len(studentsInJustOneCourse)} alunos")
for student in studentsInJustOneCourse:
    print(student)
print()