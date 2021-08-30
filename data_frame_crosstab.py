import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/titanic_train.csv')

print(data)

print('\nComparação cruzada entre as colunas Pclass e Survived')
print(pd.crosstab(data.Pclass, data.Survived))

print('\nComparação cruzada entre as colunas Ticket e Survived')
print(pd.crosstab(data.Ticket, data.Survived))

print('\nComparação cruzada entre as colunas Embarked e Survived')
print(pd.crosstab(data.Embarked, data.Survived))

print('\nComparação cruzada entre as colunas Sex e Survived')
print(pd.crosstab(data.Sex, data.Survived))

print('\nComparação cruzada entre as colunas Age e Survived')
print(pd.crosstab(data.Age, data.Survived))

print('\nComparação cruzada entre as colunas Embarked e Survived, com a coluna All')
print(pd.crosstab(data.Embarked, data.Survived, margins=True))

print('\nComparação cruzada entre as colunas Embarked com Pclass e Survived')
print(pd.crosstab([data.Embarked, data.Pclass], data.Survived))

print('\nComparação cruzada entre as colunas Embarked e Survived com Pclass')
print(pd.crosstab(data.Embarked, [data.Survived, data.Pclass]))

print('\nComparação cruzada entre as colunas Embarked e Survived, dados percentuais do total')
print(pd.crosstab(data.Embarked, data.Survived, normalize=True))

print('\nComparação cruzada entre as colunas Embarked e Survived, dados percentuais por linha')
print(pd.crosstab(data.Embarked, data.Survived, normalize='index'))

print('\nComparação cruzada entre as colunas Embarked e Survived, dados percentuais por coluna')
print(pd.crosstab(data.Embarked, data.Survived, normalize='columns'))

print('\nComparação cruzada entre as colunas Embarked e Survived, osvalores são a idade')
print(pd.crosstab(data.Embarked, data.Survived, values=data.Age, aggfunc=max))
print()
print(pd.crosstab(data.Embarked, data.Survived, values=data.Age, aggfunc=min))
