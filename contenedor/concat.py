import pandas as pd

df_cc = pd.read_csv('cyc/data_cc.csv')
df_s = pd.read_csv('sercoplus/data_s.csv')

#Concatenando la data extraída y filtrada de las tiendas "C&C" y "Sercoplus"
df = pd.concat([
    df_cc,
    df_s
    ])

#Estableciendo las columnas que tomaré en cuenta
df = df[['Tienda','Categoría','Socket','Generación','Capacidad','Título','Stock','Precio','URL']]
#Estableciendo la columna "Ciudad" como índice
df = df.set_index('Ciudad')

#Reemplazando los valores de la columna "Generación" para el caso de los procesadores
#como tienen valores únicos no causará conflicto alguno con otros valores
df['Generación'] = df.Generación.replace({
    'i3':'Core I3',
    'I3':'Core I3',
    'i5':'Core I5',
    'I5':'Core I5',
    'i7':'Core I7',
    'I7':'Core I7',
    'i9':'Core I9',
    'I9':'Core I9',
    3:'Ryzen 3',
    5:'Ryzen 5',
    7:'Ryzen 7',
    9:'Ryzen 9',
    })

print(df.columns)
#Enviando al destino donde se utilizará
df.to_csv("../digitalia/data/data.csv")
#
print('\n-------- DATA LISTA --------\n')