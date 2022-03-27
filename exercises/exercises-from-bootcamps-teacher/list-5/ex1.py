"""Neste exercício, você criará um programa que calcula a média de uma coleção de valores inseridos
pelo usuário e imprime-a na tela. O usuário digitará 0 como um valor para indicar que nenhum outro
valor será fornecido. Seu programa deve exibir uma mensagem de erro se o primeiro valor inserido pelo usuário for 0. """

number = int(input("Insira um número: "))
numbers = []

if number == 0:
    print("Não pode começar pelo 0!")
else:
    while number != 0:
        numbers.append(number)
        number = int(input("Insira um número: "))

    print(f"A média é { sum(numbers)/len(numbers) }")
    print(numbers)