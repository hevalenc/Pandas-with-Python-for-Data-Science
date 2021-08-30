import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/imdb_1000.csv')

print(data.head())
print('\nNome das colunas')
print(data.columns)

print('\nTipo dos dados')
print(data.dtypes)

print('\nAlterando o tipo da coluna duration de int para float')
data.duration = data.duration.astype(float)
print(data.dtypes)

print('\n*****************\n')

'''Carregar uma tabela alterando o tipo de uma coluna'''
data = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/imdb_1000.csv', dtype={'duration':float})

print(data.dtypes)
