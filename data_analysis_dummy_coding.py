import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/titanic_train.csv')

print(data.head())
print('\nNome das colunas')
print(data.columns)

print('\nMapeando uma coluna')
print(data.Sex.map({'male':1, 'female':0}))

data['isMale'] = data.Sex.map({'male':1, 'female':0}) #criando uma nova coluna

print('\nTabela com a nova coluna')
print(data.head())

print('\nDados únicos na coluna Embarked')
print(data.Embarked.unique())

print('\nMapear dados únicos de uma coluna - dummies')
print(pd.get_dummies(data.Embarked))

print('\n', pd.get_dummies(data.Embarked, prefix='dummy').head()) #prefix é o prefixo adicionado ao nome da coluna

embark = pd.get_dummies(data.Embarked, prefix='dummy').head() #criando uma tabela com dados de outra

print('\nConcatenando duas tabelas')
print(pd.concat([data, embark], axis=1).head()) #axis=0 para linha, axis=1 para coluna

print('\nSubstituindo colunas da tabela por dummies')
print(pd.get_dummies(data, columns=['Sex', 'Embarked']).head())
print(pd.get_dummies(data, columns=['Sex', 'Embarked']).columns)

