import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/imdb_1000.csv')

print(data.head())
print('\nNome das colunas')
print(data.columns)

print('\nDescrição detalhada da coluna genre')
print(data.genre.describe())

print('\nQuantidadede filmes em cada gênero')
print(data.genre.value_counts())

print('\nNomes únicos da coluna gênero')
print(data.genre.unique())

print('\nQuantidade de nomes únicos da coluna gênero')
print(data.genre.nunique())

print('\nComparação cruzada entre duas colunas')
print(pd.crosstab(data.genre, data.content_rating))

print('\nDetalhamento estatístico da coluna duration')
print(data.duration.describe())

import matplotlib.pyplot as plt

data.duration.plot(kind='hist')
plt.show()

data.genre.value_counts().plot(kind='bar')
plt.show()
