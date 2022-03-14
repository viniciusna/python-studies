"""Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências,
I para indústrias e C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir.

+---------------------------------------+
|   Preço por tipo e faixa de consumo   |
+---------------------------------------+
| Tipo        | Faixa (kWh)   | Preço   |
+=======================================+
| Residencial | Até 500       | R$ 0,40 |
|             | Acima de 500  | R$ 0,65 |
+---------------------------------------+
| Comercial   | Até 1000      | R$ 0,55 |
|             | Acima de 1000 | R$ 0,60 |
+---------------------------------------+
| Industrial  | Até 5000      | R$ 0,55 |
|             | Acima de 5000 | R$ 0,60 |
+---------------------------------------+
Resposta:"""

energyQuantity = float(input("Quantidade de energia consumida (em kWh): "))
plant = input(f"Qual o tipo de instalação? \n R-residência \n I-indústria \n C-comércio \n")

if plant.lower() == "r":
    if energyQuantity <= 500:
        print(f"O valor a pagar é R${ energyQuantity*0.4 :.2f}")
    else:
        print(f"O valor a pagar é R${ energyQuantity*0.65 :.2f}")

elif plant.lower() == "i":
    if energyQuantity <= 5000:
        print(f"O valor a pagar é R${ energyQuantity*0.55 :.2f}")
    else:
        print(f"O valor a pagar é R${ energyQuantity*0.6 :.2f}")

else:
    if energyQuantity <= 1000:
        print(f"O valor a pagar é R${ energyQuantity*0.55 :.2f}")
    else:
        print(f"O valor a pagar é R${ energyQuantity*0.6 :.2f}")
