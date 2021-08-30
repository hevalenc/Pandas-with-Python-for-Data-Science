import pandas as pd

'''Tabela com as colunas separadas por tabulação'''

data = pd.read_table('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/chipotle.tsv')

print(data)
print('\nPrimeiras linhas')
print(data.head())
print('\nÚltimas linhas')
print(data.tail())
print('\nModelagem da tabela (linhas x coluna)')
print(data.shape)
print('\nNome das colunas')
print(data.columns)

print('\n******************\n')
'''Tabela com as colunas separadas pelo símbolo pipe (|) e sem nome nas colunas'''

'''Nomeando as colunas'''
col_names = ['ID', 'Age', 'Gender', 'Occupation', 'Revenue']

data1 = pd.read_table('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/u.user', sep='|', header=None, names=col_names)

print(data1)

'''Criando uma nova coluna com concatenação de dados'''
data1['new_column'] = data1.Occupation + data1.Gender

print('\n*************\n')
print(data1.head())
