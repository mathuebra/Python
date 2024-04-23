import pandas as pd

cidades = ['Maringá', 'Itabira', 'Uberlândia', 'Salvador', 'Fortaleza']
populacao = [403.063, 120.904, 699.097, 2.886698, 2.686612]

populacao_cidades = dict(zip(cidades, populacao))

# Verifica se o tipo de populacao_cidades realmente é 'dict'
print(type(populacao_cidades))

print(populacao_cidades['Uberlândia'])

# Verifica se as cidades estão no dicionário
print('São Carlos' in populacao_cidades)
print('Maringá' in populacao_cidades)

# Adiciona um novo registro
populacao_cidades['Vitória'] = 365.855

print('Vitória' in populacao_cidades)

del populacao_cidades['Fortaleza']

print('Fortaleza' in populacao_cidades)