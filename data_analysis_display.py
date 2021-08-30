import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/drinks.csv')

print(data.head())

print('\nConfiguração de linhas a ser exibido: ', pd.get_option('display.max_rows')) #verificar a configuração de saída na tela

pd.set_option('display.max_rows', 200) #configurar a quantidade de linhas que serão exibidas na tela

print('\nConfiguração de linhas a ser exibido: ', pd.get_option('display.max_rows'))
print(data)

pd.reset_option('display.max_rows')
