import pandas as pd

ufo = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv')

print(ufo.head())

print('\nTipo dos dados')
print(ufo.dtypes)

ufo['Time'] = pd.to_datetime(ufo.Time)
print('\nConvertendo object to datetime')
print(ufo.dtypes)
print()
print(ufo.head())

print('\nVerificando os minutos da coluna Time')
print(ufo.Time.dt.minute.head(10))

print('\nData mais recente')
print(ufo.Time.max())

date = pd.to_datetime('1.1.1998')
print('\nNova data: ', date)

print('\nMostrar todos os registros com data superior a nova data')
print(ufo.loc[ufo.Time >= date])
