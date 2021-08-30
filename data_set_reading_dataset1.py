import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/imdb_1000.csv')

print(data)
print('\nPrimeiras linhas')
print(data.head())
print('\nÚltimas linhas')
print(data.tail())
print('\nModelagem da tabela (linhas x coluna)')
print(data.shape)
print('\nNome das colunas')
print(data.columns)

print('\n******************\n')

'''Outramaneira de abrir um arquivo CSV com pandas'''
data1 = pd.read_table('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/imdb_1000.csv', sep=',')

print(data1.head())

print('\nDescrição estatística da tabela')
print(data.describe())

'''No Pandas, todos os dados no formato string são considerados objetos'''
print('\nDescrição dos objetos da tabela')
print(data.describe(include=['object']))

print('\nTipo dos dados da tabela')
print(data.dtypes)

print('\nOrdenando os dados da coluna duration por ordem crescente')
print(data['duration'].sort_values())

print('\nOrdenando os dados da coluna duration por ordem decrescente')
print(data['duration'].sort_values(ascending=False))

print('\nOrdenando os dados da tabela por ordem crescente da coluna duration')
print(data.sort_values('duration'))

print('\nOrdenando os dados da tabela por ordem crescente das colunas genre e duration')
print(data.sort_values(['genre', 'duration']))
