import pandas as pd

data = pd.DataFrame({'Id':[1,2,3,4,1,2,3,4,], 'Name':['Tom', 'Harry', 'Peter', 'Thomas', 'Tom', 'Harry', 'Peter', 'Thomas']})

print(data)

print('\nIdentificando dados duplicados')
print(data.Name.duplicated()) #keep='first' é o padrão, manter o primeiro registro como não duplicado
print()
print(data.Name.duplicated(keep='last')) #keep='last' vai manter o último registro como não duplicado

print('\nTotal de dados duplicados')
print(print(data.duplicated().sum()))

print('\nLocalizando os dados duplicados')
print(data.loc[data.duplicated()])

print('\nRemovendo dados duplicados, preservando os primeiros')
print(data.drop_duplicates())

print('\nRemovendo dados duplicados, preservando os últimos')
print(data.drop_duplicates(keep='last'))
