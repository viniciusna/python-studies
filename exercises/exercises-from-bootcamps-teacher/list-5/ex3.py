"""Um determinado zoológico cobra a entrada com base na idade do visitante.
Os visitantes com 2 anos de idade ou menos não pagam para entrar. Crianças entre 3 e 12 anos custa R$14,00.
Idosos com 65 anos ou mais custam R$18,00. A entrada para todos os outros visitantes é de R$23,00.
Crie um programa que comece lendo do usuário as idades de todos os visitantes de um determinado grupo,
com uma idade inserida em cada linha. O usuário digitará uma linha em branco para indicar que não há
mais visitantes no grupo. Em seguida, seu programa deve exibir o custo de admissão para o grupo com uma mensagem apropriada.
O custo deve ser exibido usando duas casas decimais. """

age = input("insira a idade: ")
value = 0

while True:
    if age == "":
        break

    age = int(age)

    if 2 < age < 13:
        value += 14
    elif 13 <= age < 65:
        value += 23
    elif 65 <= age:
        value += 18

    age = input("insira a idade: ")

print(f"O total a pagar pelo grupo é R$ {value:.2f}")
