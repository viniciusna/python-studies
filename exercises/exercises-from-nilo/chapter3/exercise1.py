"""Complete a tabela a seguir, marcando inteiro ou ponto flutuante dependendo do número apresentado.

    Número      Tipo numérico
    5      ○ inteiro ○ ponto flutuante
    5.0    ○ inteiro ○ ponto flutuante
    4.3    ○ inteiro ○ ponto flutuante
    -2     ○ inteiro ○ ponto flutuante
    100    ○ inteiro ○ ponto flutuante
    1.333  ○ inteiro ○ ponto flutuante
Resposta:"""

print("Exercício 1")

numbers = [5, 5.0, 4.3, -2, 100, 1.333]

print(f"Número{6*' '}Tipo numérico")

for x in numbers:
    print(f"{x}       { 'ponto flutuante' if type(x) == float else 'inteiro' }")