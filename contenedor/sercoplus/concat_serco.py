import pandas as pd

s_mb_10_11 = pd.read_csv('1_data/s_mb_10_11.csv')
s_mb_12 = pd.read_csv('1_data/s_mb_12.csv')
s_mb_am4 = pd.read_csv('1_data/s_mb_am4.csv')
s_cpu_10 = pd.read_csv('1_data/s_cpu_10.csv')
s_cpu_11 = pd.read_csv('1_data/s_cpu_11.csv')
s_cpu_12 = pd.read_csv('1_data/s_cpu_12.csv')
s_cpu_am4 = pd.read_csv('1_data/s_cpu_am4.csv')
s_alm = pd.read_csv('1_data/s_almacenamiento.csv')
s_case = pd.read_csv('1_data/s_case.csv')
s_pc = pd.read_csv('1_data/s_pc.csv')
s_gpu = pd.read_csv('1_data/s_gpu.csv')
s_laptop = pd.read_csv('1_data/s_laptop.csv')
s_psu = pd.read_csv('1_data/s_psu.csv')
s_ram = pd.read_csv('1_data/s_ram.csv')

df = pd.concat([
    s_mb_10_11,
    s_mb_12,
    s_mb_am4,
    s_cpu_10,
    s_cpu_11,
    s_cpu_12,
    s_cpu_am4,
    s_ram,
    s_alm,
    s_gpu,
    s_psu,
    s_case,
    s_pc,
    s_laptop
    ])
#df = df.set_index('Tienda')
df.to_csv("data_a_filtrar_s.csv")
print("--- DATOS CONCATENADOS ---")

#