import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/imdb_1000.csv')

print(data.head())
print('\nNome das colunas')
print(data.columns)

print('\n*************\n')
print('\nFiltrando os dados por content_rating = "R"')
print(data[data.content_rating == 'R'])

print('\nFiltrando os dados por content_rating = "R" e genre = "Crime"')
print(data[(data.content_rating == 'R') & (data.genre == 'Crime')])

print('\nFiltrando os dados por genre = "Crime" ou genre = "Action" ou genre = "Drama"')
print(data[(data.genre == 'Crime') | (data.genre == 'Action') | (data.genre == 'Drama')])

print('\nOutro método para filtrar os dados acima')
print(data[data.genre.isin(['Crime', 'Drama', 'Action'])])

