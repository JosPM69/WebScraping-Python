import pandas as pd

cc_mb_10 = pd.read_csv('1_data/cc_mb_10.csv')
cc_mb_11 = pd.read_csv('1_data/cc_mb_11.csv')
cc_mb_12 = pd.read_csv('1_data/cc_mb_12.csv')
cc_mb_am4 = pd.read_csv('1_data/cc_mb_am4.csv')
cc_cpu_10 = pd.read_csv('1_data/cc_proce_10.csv')
cc_cpu_11 = pd.read_csv('1_data/cc_proce_11.csv')
cc_cpu_12 = pd.read_csv('1_data/cc_proce_12.csv')
cc_cpu_am4 = pd.read_csv('1_data/cc_proce_am4.csv')
cc_alm = pd.read_csv('1_data/cc_almacenamiento.csv')
cc_case = pd.read_csv('1_data/cc_case.csv')
cc_pc = pd.read_csv('1_data/cc_computadora.csv')
cc_gpu = pd.read_csv('1_data/cc_gpu.csv')
cc_laptop = pd.read_csv('1_data/cc_laptop.csv')
cc_psu = pd.read_csv('1_data/cc_psu.csv')
cc_ram = pd.read_csv('1_data/cc_ram.csv')

df = pd.concat([
    cc_mb_10,
    cc_mb_11,
    cc_mb_12,
    cc_mb_am4,
    cc_cpu_10,
    cc_cpu_11,
    cc_cpu_12,
    cc_cpu_am4,
    cc_ram,
    cc_alm,
    cc_gpu,
    cc_psu,
    cc_case,
    cc_pc,
    cc_laptop
    ])
#df = df.set_index('Tienda')
df.to_csv("data_a_filtrar.csv")
print("--- DATOS CONCATENADOS ---")
