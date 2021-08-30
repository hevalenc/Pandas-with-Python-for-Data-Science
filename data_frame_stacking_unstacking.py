import pandas as pd

data = pd.read_excel('E:\\EngSoft\\Cursos\\Udemy\\Pandas with Python for Data Science\\Products.xlsx', header=[0,1])

print(data)

data1 = data.stack()

print('\nStacking data table')
print(data1)

data2 = data1.stack()

print('\nStacking data1 table')
print(data2)

data3 = data2.unstack()

print('\nUnstacking data2 table')
print(data3)

data4 = data3.unstack(level=0)

print('\nUnstacking data3 table')
print(data4)

data4 = data3.unstack(level=[0,1])

print('\nUnstacking data3 table')
print(data4)
