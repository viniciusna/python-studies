"""Faça um programa que lê uma sigla de um estado do usuário e imprime na tela o nome completo do estado. Exemplo:

>> Digite um estado: SP
>> O nome completo do estado é São Paulo.
"""

acronymsOfStates = {
    "RR": "Roraima",
    "AP": "Amapá",
    "AM": "Amazonas",
    "PA": "Pará",
    "AC": "Acre",
    "RO": "Rondônia",
    "TO": "Tocantins",
    "MA": "Maranhão",
    "PI": "Piauí",
    "CE": "Ceará",
    "RN": "Rio Grande do Norte",
    "PB": "Paraíba",
    "PE": "Pernambuco",
    "AL": "Alagoas",
    "SE": "Sergipe",
    "BA": "Bahia",
    "MT": "Mato Grosso",
    "DF": "Distrito Federal",
    "GO": "Goiás",
    "MS": "Mato Grosso do Sul",
    "MG": "Minas Gerais",
    "ES": "Espírito Santo",
    "RJ": "Rio de Janeiro",
    "SP": "São Paulo",
    "PR": "Paraná",
    "SC": "Santa Catarina",
    "RS": "Rio Grande do sul"
}

acronymsInput = input("Digite a sigla de um estado: ").upper()

if acronymsInput in acronymsOfStates:
    print(f"O nome completo do estado é {acronymsOfStates[acronymsInput]}")
else:
    print("Sigla inválida")