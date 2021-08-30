import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv')

print(data.head())
print('\nNome das colunas')
print(data.columns)

print('\nTodos os registros do índice 0')
print(data.loc[0, :]) #loc[row, column], ':' significa tudo

print('\nTodos os registros dos índices 0, 1, 2 e 3')
print(data.loc[[0,1,2,3], :])

print('\nTodos os registros dos índices 0, 1, 2 e 3')
print(data.loc[0:3, :])

print('\nTodos os registros das colunas City, State e Time')
print(data.loc[:,['City', 'State', 'Time']])

print('\nTodos os registros das colunas City, Colors Reported, Shape Reported e State')
print(data.loc[:,'City' : 'State'])
