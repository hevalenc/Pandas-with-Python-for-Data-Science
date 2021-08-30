import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/imdb_1000.csv')

print(data.head())
print('\nNome das colunas')
print(data.columns)

print('\nDuração média de tempo de cada gênero de filme')
print(data.groupby('genre').duration.mean())

print('\nMenor duração de tempo de cada gênero de filme')
print(data.groupby('genre').duration.min())

print('\nMaior duração de tempo de cada gênero de filme')
print(data.groupby('genre').duration.max())

print('\nDetalhes sobre duração de tempo de cada gênero de filme')
print(data.groupby('genre').duration.agg(['min', 'median', 'max', 'mean', 'count'])) #agg significa agregação (aggregation)

