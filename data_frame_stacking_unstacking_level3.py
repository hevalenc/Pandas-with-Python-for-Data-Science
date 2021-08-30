import pandas as pd

data = pd.read_excel('E:\\EngSoft\\Cursos\\Udemy\\Pandas with Python for Data Science\\Products1.xlsx', header=[0,1,2])

print(data)

data1 = data.stack()

print('\nStacking data table')
print(data1)

data1 = data.stack(level=[0,2])

print('\nStacking data table')
print(data1)

data2 = data1.unstack(level=[0,2])

print('\nUnstacking data1 table')
print(data2)
