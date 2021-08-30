import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv')

print(data.head())
print('\nNome das colunas')
print(data.columns)

print('\nOcorrência de dados nulos')
print(data.isnull())
print('\nSem ocorrência de dados nulos')
print(data.notnull())

print('\nQuantidade total de ocorrência de dados nulos')
print(data.isnull().sum())

print('\nTodos os registros onde City é nulo')
print(data[data.City.isnull()])
