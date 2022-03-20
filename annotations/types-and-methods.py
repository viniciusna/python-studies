"""Pra formatar float num string faz:
    f" { n : .xf } "

onde 'n' é o float que será exibido e 'x' é o número de casa decimais que será usado.
EX:
"""
print(f"{round(750*1.15): .2f}")

"""Para selecionar um trecho de uma string usa-se

str[i: n: p]

Assim selcionar o trecho da string que se inicia no índice 'i' até o índice 'n - 1' pulando de 'p' em 'p' caracteres.
EX:
"""

print( "abcdefgh"[1:9:2] )      #bdfh