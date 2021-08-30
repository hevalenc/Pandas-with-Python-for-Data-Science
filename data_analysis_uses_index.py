import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv')

print(data.head())
print('\nNome das colunas')
print(data.columns)

print('\nÍndice: início e fim')
print(data.index)

print('\nMostrar os registros do estado de NY')
print(data[data.State == 'NY'])

print('\nFormatação da tabela (linhas x colunas)')
print(data.shape)

print('\nLocalizando um registro')
print(data.loc[0, 'State']) #registro no índice 0, coluna State

print('\nUsando a coluna City como índice')
data.set_index('City', inplace=True)
print(data.head())

print('\nFormatação da tabela (linhas x colunas), uma coluna a menos')
print(data.shape)

print('\nLocalizando um registro, cujo índice é Abilene')
print(data.loc['Abilene', 'Colors Reported'])

print('\nRemovendo o nome do índice')
data.index.name = None
print(data.head())

print('\nReiniciando a coluna de índice (números)')
data.reset_index(inplace=True)
print(data.head())

print('\nRenomeando a coluna index para City')
data.rename(columns={'index': 'City'}, inplace=True)
print(data.head())

print('\nAnálise estatística da tabela')
print(data.describe())
print()
print(data.describe().index)
