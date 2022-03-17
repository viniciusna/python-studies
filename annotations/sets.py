"""Sets são feitos com chaves ou com a função set().
Para se fazer um set vazio, faz "set()", pois "{}" é considerado um dicionário.
Alguns métodos para sets:
Seja A e B sets, então
A - B -> subtração de B do conjunto A
A | B -> união
A & B -> interseção
A ^ B -> vai resultar num conjunto de elementos que, ou estão em A ou estão em B
x in A -> retorna True se x estiver em A, false se contrário
"""

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

print('orange' in basket)       #True
print('crabgrass' in basket)        #False

a = set('abracadabra')
b = set('alacazam')

print(a)        #{'d', 'a', 'c', 'r', 'b'}
print(b)        #{'z', 'm', 'l', 'a', 'c'}
print(a - b)        #{'d', 'b', 'r'}
print(a | b)        #{'z', 'm', 'l', 'a', 'c', 'd', 'b', 'r'}
print(a & b)        #{'c', 'a'}
print(a ^ b)        #{'z', 'm', 'd', 'b', 'l', 'r'}
