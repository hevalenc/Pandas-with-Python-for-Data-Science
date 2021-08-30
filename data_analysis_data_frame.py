import pandas as pd

data = pd.DataFrame({'Id':[1,2,3,4], 'customerName':['Tom', 'Harry', 'Peter', 'Thomas'], 'age':[20,25,34,45]})

print('Data Frame feito de forma manual')
print(data)

ufo = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv')

print('\nData Frame feito através de um arquivo CSV')
print(ufo.head())
print()
print(ufo.shape)

print('\nDados nulos no DF UFO')
print(pd.isnull(ufo).head())

print('\nAmostra da tabela UFO')
print(ufo.sample(n=5)) #a amostra será aleatória toda vez que rodar o programa, o 'n' é a quantidade

print('\nAmostra da tabela UFO')
print(ufo.sample(n=10, random_state=2)) #o random_state preserva a amostra toda vez que rodar o programa

print('\nAmostra da tabela UFO')
print(ufo.sample(frac=0.2, random_state=2)) #frac é a quantidade fracionária da amostra
