import pandas as pd
from numpy import nan

df = pd.read_csv("data_a_filtrar.csv")

## LIMPIEZA DE DATOS

# Títulos
for i in range(len(df['Título'])):
    df['Título'][i] = df['Título'][i].split('(')[0]

#Precios
for i in range(len(df['Precio'])):
            df['Precio'][i] = df['Precio'][i].split('S/')[1]
            df['Precio'][i] = df['Precio'][i].replace('.','')
            df['Precio'][i] = df['Precio'][i].replace(',','.')
            df['Precio'][i] = float(df['Precio'][i])

#Stock
for i in range(len(df['Stock'])):
            lst = []
            for j in df['Stock'][i]:
                lst.append(j)
            if len(lst) == 12:
                df['Stock'][i]= lst[6]
            elif len(lst) >= 13:
                df['Stock'][i] = 10
            else:
                df['Stock'][i] = 0
            df['Stock'][i] = int(df['Stock'][i])

#Detalle procesador
df['Categoría'] = df.Categoría.replace({'Procesador':'CPU'}) # Cambiando los valores de Procesador a CPU en la columna Categoría
df = df.drop(df.index[(df['Categoría']=='CPU') & (df['Generación']=='4')]) #Eliminando el dato filtrado

#Por stock, elimnando menores a 5
a_eliminar = df[df['Stock']<=4].index
df = df.drop(a_eliminar)

#Estableciendo el orden de las columnas
df = df[['Tienda','Categoría','Socket','Generación','Capacidad','Título','Stock','Precio','URL']]

#Índice
df = df.set_index('Tienda')

#Guardando los cambios en un archivo csv llamado "data_cc"
df.to_csv('data_cc.csv')

#