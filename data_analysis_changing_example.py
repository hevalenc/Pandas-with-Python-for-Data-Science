import pandas as pd

data = pd.read_table('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/chipotle.tsv')

print(data.head())
print('\nNome das colunas')
print(data.columns)
print('\nTipo dos dados')
print(data.dtypes)

print('\nValor médio dos preços')
print(data.item_price.str.replace('$', '').astype(float).mean())

print('\nVerificar se na coluna item_name possui a palavra and')
print(data.item_name.str.contains('and').head())
