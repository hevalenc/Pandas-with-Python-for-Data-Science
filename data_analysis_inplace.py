import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/drinks.csv')

print(data.head())
print('\nNome das colunas')
print(data.columns)

print('\nFromatação da tabela: linhas x colunas')
print(data.shape)

print('\nRemovendo a coluna continent temporariamente')
print(data.drop('continent', axis=1).head()) #inplace=False é padrão para proteção dos dados na tabela

print('\nColunas')
print(data.columns)

print('\nRemovendo a coluna continent definitivamente')
data.drop('continent', axis=1, inplace=True) #inplace=True autoriza a ação na tabela
print(data.head())

print('\nRemovendo a coluna total_litres_of_pure_alcohol definitivamente')
data.drop('total_litres_of_pure_alcohol', axis=1, inplace=True)
print(data.head())

print('\nOutro método de remoção que não requer implace=True')
data = data.drop('wine_servings', axis=1)
print(data.head())
