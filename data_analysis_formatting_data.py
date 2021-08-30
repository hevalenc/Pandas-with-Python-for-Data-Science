import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/drinks.csv')

print(data.head())

data['wine'] = data.wine_servings * 1000
data['alcohol'] = data.total_litres_of_pure_alcohol * 1000

print('\nTabela com novas colunas')
print(data.head())

print('\nTipos dos dados')
print(data.dtypes)

pd.set_option('display.float_format', '{:,}'.format)

print('\nTabela com nova configuração')
print(data.head())

print('\nTipos dos dados')
print(data.dtypes)
