import pandas as pd

data = pd.read_csv('E:\\EngSoft\\Cursos\\Udemy\\Pandas with Python for Data Science\\Temperature.csv', sep=';')

print(data)

print('\nPivotando uma tabela')
print(data.pivot(index='Day', columns='City'))

print('\nPivotando uma tabela, onde os valore serão a precipitação')
print(data.pivot(index='Day', columns='City', values='Preciptation'))

data1 = pd.read_csv('E:\\EngSoft\\Cursos\\Udemy\\Pandas with Python for Data Science\\Temperature1.csv', sep=';')

print('\nNova tabela')
print(data1)

print('\nPivotando uma nova tabela')
print(data1.pivot_table(index='Day', columns='City', aggfunc='max'))
print(data1.pivot_table(index='Day', columns='City', aggfunc='max', margins=True))

data2 = pd.read_csv('E:\\EngSoft\\Cursos\\Udemy\\Pandas with Python for Data Science\\Temperature2.csv', sep=';')

print('\nNova tabela')
print(data2)

print('\nPivotando a nova tabela')
print(data2.pivot(index='Day', columns='City'))

print('\nTipo do dado da coluna Day')
print(type(data2.Day[0]))

data2.Day = pd.to_datetime(data2.Day)
print(type(data2.Day[0]))

print('\nPivotando uma nova tabela com o Grouper')
print(data2.pivot_table(index=pd.Grouper(key='Day', freq='W'), columns='City', aggfunc='max'))
