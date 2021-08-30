import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/imdb_1000.csv')

print(data.head())
print('\nNome das colunas')
print(data.columns)

print('\nColocando o título em maiúsculas')
print(data.title.str.upper())

print('\nSubstituindo caracteres "["')
print(data.actors_list.str.replace('[', ''))

print('\nSubstituindo caracteres "[" e "]"')
print(data.actors_list.str.replace('[', '').str.replace(']', ''))

print('\nQual registro contém a palavra "The"')
print(data.title.str.contains('The'))
