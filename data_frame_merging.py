import pandas as pd

df1 = pd.DataFrame([['TN', 'Chennai'], ['Telangana', 'Hyderabad'], ['Karnataka', 'Bengalara'], ['Delhi', 'Delhi']], columns=['State', 'Capital'])

print('Data Frame 1')
print(df1)


df2 = pd.DataFrame([['TN', 'Tamil'], ['Telangana', 'Telugu'], ['Karnataka', 'Kannada'], ['MP', 'Hindi']], columns=['State', 'Language'])

print('\nData Frame 2')
print(df2)

print('\nMesclando os dois DFs - inner')
print(pd.merge(df1, df2, how='inner', on='State')) #mesclar as tabelas com os dados comuns de acordo com a coluna State

print('\nMesclando os dois DFs - outer')
print(pd.merge(df1, df2, how='outer', on='State')) #mesclar as tabela com os dados das duas de acordo com a coluna State

print('\nMesclando os dois DFs - left')
print(pd.merge(df1, df2, how='left', on='State')) #mesclando a tabela direita com a esquerda (dados em comum com a esquerda)

print('\nMesclando os dois DFs - right')
print(pd.merge(df1, df2, how='right', on='State')) #mesclando a tabela direita com a esquerda (dados em comum com a direita)

print('\nMesclando os dois DFs - right e indicator')
print(pd.merge(df1, df2, how='right', on='State', indicator=True)) #indicator serve para indicar de qual tabela vem o dado

df3 = pd.DataFrame({'days':['Mon','Tue','Wed','Thu','Fri','Sat','Sun'], 'temperature':[30,32,31,34,32,34,35], 'humidity':[30,32,31,34,32,34,35]})

print('\nData Frame 3')
print(df3)

print('\nTransformando o formato da tabela com pivotamento')
print(pd.melt(df3, id_vars='days')) #melt é utilizado para mesclar as variáveis de uma tabela em uma coluna

print('\nTransformando o formato da tabela com pivotamento')
print(pd.melt(df3, id_vars='days', var_name='Metric', value_name='temperature / humidity'))
