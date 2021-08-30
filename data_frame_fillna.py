import pandas as pd

ufo = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv')

print(ufo)

ufo_new = ufo.fillna('blank')

print('\nNova tabela com dados NaN substituídos por blank')
print(ufo_new)

print('\nSubstituindo os valores NaN por outro')
print(ufo.fillna({'Colors Reported':'No Color', 'Shape Reported':'No Shape'}))

temperature = pd.read_csv('E:\\EngSoft\\Cursos\\Udemy\\Pandas with Python for Data Science\\temp.csv')

print('\nNova tabela com dados nulos')
print(temperature)

print('\nSubstituindo os dados nulos pelo dado anterior')
print(temperature.fillna(method='ffill'))

print('\nSubstituindo os dados nulos pelo dado posterior')
print(temperature.fillna(method='bfill'))
