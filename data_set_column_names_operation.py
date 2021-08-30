import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/imdb_1000.csv')

print(data.head())
print('\nNome das colunas')
print(data.columns)

'''Renomeando a coluna'''
data.rename(columns={'star_rating':'starRating'}, inplace=True) #ou data = data.rename(columns={'star_rating':'StarRating'})

print('\nNome das colunas com a coluna renomeada')
print(data.columns)

'''Outra maneira para renomear as colunas'''
data_cols = ['StarRating', 'Title', 'ContentRating', 'Genre', 'Duration', 'ActorsList']
data.columns = data_cols

print('\nNome das colunas renomeadas')
print(data.columns)

print('\n******************\n')
data1 = pd.read_table('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/imdb_1000.csv', sep=',', names=data_cols)

print(data1.head())

print('\n******************\n')
data2 = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/imdb_1000.csv')

print(data2.columns)

print('\nSubstituindo caracteres nas colunas')
print(data2.columns.str.replace('_', ' '))

data2.columns = data2.columns.str.replace('_', ' ')

print('\nSubstituindo caracteres nas colunas (definitivo)')
print(data2.columns)
