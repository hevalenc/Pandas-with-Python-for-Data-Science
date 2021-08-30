import pandas as pd

'''Extraindo uma tabela de um arquivo CSV e selecionando as colunas que serão utilizados'''
data = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/imdb_1000.csv', usecols=['title', 'genre'])

print(data.head())
print('\nNome das colunas')
print(data.columns)

print('\n*****************\n')

'''Extraindo uma tabela de um arquivo CSV e selecionando quantas linhas serão utilizados'''
data = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/imdb_1000.csv', nrows=5)

print(data.head())
print('\nNome das colunas')
print(data.columns)
print()

for i in data.title:
    print(i)

print()

for index, row in data.iterrows():
    print(row.title, row.genre)
