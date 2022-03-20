"""A tabela a seguir lista os níveis sonoros em decibéis para alguns barulhos comuns
Barulho	Nível sonoro (dB)
Britadeira	130
Cortador de grama	106
Despertador	70
Cômodo em silêncio	40


Escreva um programa que leia um valor de nível sonoro do usuário em decibéis. Se o valor for um dos que estão na tabela,
o programa deve retornar aquele barulho. Caso o número esteja entre algum dos valores da tabela, o programa deve dizer
entre quais barulhos o valor digitado está. Seu programa deve informar também quando o valor for menor que o ruído
mínimo da tabela e maior que ruído máximo. 
"""

sonorousLevel = int(input("Insira o nível sonoro em decibéis (db):"))

if sonorousLevel == 40:
    print("Mesmo nível sonoro de um cômodo em silêncio")
elif sonorousLevel == 70:
    print("Mesmo nível sonoro de um despertador")
elif sonorousLevel == 106:
    print("Mesmo nível sonoro de um cortador de grama")
elif sonorousLevel == 130:
    print("Mesmo nível sonoro de um britadeira")
elif sonorousLevel < 40:
    print("Nível sonoro menor que o nível sonoro mínimo da tabela")
elif sonorousLevel < 70:
    print("Nível sonoro entre os níveis sonoros de um cômodo em silêncio e um despertador")
elif sonorousLevel < 106:
    print("Nível sonoro entre os níveis sonoros de um despertador e um cortador de grama")
elif sonorousLevel < 130:
    print("Nível sonoro entre os níveis sonoros de um cortador de grama e uma britadeira")
else:
    print("Nível sonoro maior que o nível sonoro máximo da tabela")