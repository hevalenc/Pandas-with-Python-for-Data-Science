import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/imdb_1000.csv')

print(data.head())
print('\nNome das colunas')
print(data.columns)

print('\nMédia dos valores na tabela')
print(data.mean())

print('\nMédia dos valores na tabela, média por coluna')
print(data.mean(axis=0))

print('\nMédia dos valores na tabela, média por linha')
print(data.mean(axis=1))
