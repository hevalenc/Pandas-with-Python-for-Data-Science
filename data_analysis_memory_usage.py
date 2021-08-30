import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/drinks.csv')

print(data.head())

print('\nInformação da tabela')
print(data.info()) #não é considerado o tamanho real da memória utilizada por objetos

print('\nInformação da tabela: espaço em uso (real)')
print(data.info(memory_usage='deep')) #apresenta a memória em uso de todos os tipos de dados

print('\nEspaço em uso por cada coluna de dados em bytes')
print(data.memory_usage(deep=True))

print('\nRegistros únicos na coluna continent')
print(data.continent.unique())

'''Otimizando o espaço utilizado na memória, convertendo o tipo do dado na coluna'''
data['continent'] = data.continent.astype('category')

print('\nTipo dos dados')
print(data.dtypes)

print('\nCódigo da categoria usado na coluna continent')
print(data.continent.cat.codes.head())

print('\nEspaço em uso por cada coluna de dados em bytes')
print(data.memory_usage(deep=True))

print('\nColuna continent')
print(data.continent.head(20))

data['country'] = data.country.astype('category')

print('\nEspaço em uso por cada coluna de dados em bytes')
print(data.memory_usage(deep=True))

print('\nColuna country')
print(data.country.head(20))
