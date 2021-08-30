import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/imdb_1000.csv')

print(data.head())
print('\nNome das colunas')
print(data.columns)

data.drop('title', axis=1, inplace=True) #axis=1 significa coluna

print('\nRemovido a coluna title')
print(data.columns)

data.drop(['genre', 'duration'], axis=1, inplace=True) #remoção de duas colunas ou mais

print('\nRemovido as colunas genre e duration')
print(data.columns)

print('\n******************\n')
print(data.head())

data.drop([0,1,2], axis=0, inplace=True) #axis=0 significa linha

print('\nRemovido as linhas 0, 1 e 2')
print(data.head())
