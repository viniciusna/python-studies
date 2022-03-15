"""Crie uma lista com 6 números inteiros. Imprima o maior, o menor e suas respectivas posições.
Exemplo: para a lista [5,4,6,8,3,4] a saída deve ser
>> O maior elemento é 8 e está na posição 3
>> O menor elemento é 3 e está na posição 4

Obs: caso o maior ou o menor número sejam repetidos, trazer a menor posição.
"""

array = [1, 6, 3, 4, 5, 6]

print(f" O maior número é {max(array)} e está na posição {array.index(max(array))}")
print(f" O maior número é {min(array)} e está na posição {array.index(min(array))}")