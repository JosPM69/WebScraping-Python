import pandas as pd
from numpy import nan

df = pd.read_csv("data_a_filtrar_s.csv")

## LIMPIEZA DE DATOS

#Precios
for i in range(len(df['Precio'])):
    if ',' in df['Precio'][i]:
        df['Precio'][i] = df['Precio'][i].replace('.','')
        df['Precio'][i] = df['Precio'][i].replace(',','.')

for i in range(len(df['Precio'])):
    if df['Precio'][i].split(' ')[0]=='(S/':
        df['Precio'][i] = str(df['Precio'][i].split(' ')[-1] + '')
        df['Precio'][i] = str(df['Precio'][i].rstrip(df['Precio'][i][-1]))
        df['Precio'][i] = float(df['Precio'][i])
    else:
        df['Precio'][i] = nan

#Stock
for i in range(len(df['Stock'])):
    df['Stock'][i] = df['Stock'][i].split('>')[-1] 
    df['Stock'][i] = int(df['Stock'][i])

#Por stock, elimnando menores a 5
a_eliminar = df[df['Stock']<=4].index
df = df.drop(a_eliminar)

#Estableciendo el orden de las columnas
df = df[['Tienda','Categoría','Socket','Generación','Capacidad','Título','Stock','Precio','URL']]

#Índice
df = df.set_index('Tienda')


df.to_csv('data_s.csv')