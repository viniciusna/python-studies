"""Dada a lista de strings ["1", "7", "99", "15"] construa um programa que converte todos
os elementos desta lista para inteiro.
Faça também o inverso, dada a mesma lista só que agora de elementos inteiros, converta todos os elementos para int.
"""

lst = ["1", "7", "99", "15"]

lstInt = list(map(int, lst))

lstStr = list(map(str, lstInt))

print("A lista original é a seguinte")
print(lst)
print()
print("A lista com elementos convertidos para 'int':")
print(lstInt)
print()
print("Agora a lista anterior com os elementos convertidos para string:")
print(lstStr)