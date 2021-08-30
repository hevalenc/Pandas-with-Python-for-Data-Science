import pandas as pd

data = pd.read_csv('E:\\EngSoft\\Cursos\\Udemy\\Pandas with Python for Data Science\\Temperature1.csv', sep=';')

print(data)

data = data.replace('Chennai', 'Madras', inplace=True)

print('\nSubstituindo uma cidade')
print(data)

data.to_csv('E:\\EngSoft\\Cursos\\Udemy\\Pandas with Python for Data Science\\Temperature_updated.csv')
