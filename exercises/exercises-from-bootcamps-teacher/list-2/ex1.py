"""Crie uma variável do tipo lista com 5 elementos (você escolhe quais serão).
Imprima na tela o elemento e sua respectiva posição na lista. Exemplo:
para a lista [1, 3, 6, “H”, [7,7,7]] a saída deve ser:
>> Elemento 1 na posição 0
>> Elemento 3 na posição 1
>> Elemento 6 na posição 2
>> Elemento “H” na posição 3
"""

array = [1, 3, 6, "h", [7,7,7]]

for index, element in enumerate(array):
    print(f"Elemento {element} na posição {index}")
print(list(enumerate(array)))