import csv
import os
import pandas as pd
from matplotlib import pyplot as plt

archivo=os.path.join(os.getcwd(),'sample_data/datos_estadisticos.csv')
archivo_csv=open(archivo,"r")

data_set= pd.read_csv(archivo_csv,encoding='utf-8')

print(data_set)

por_tiempo = data_set.sort_values('Tiempo',ascending=False)
usuario_tiempo=por_tiempo[['Usuarie - nick','Tiempo']].head(n=3)

print(usuario_tiempo)

usuario_tiempo.plot(kind='bar')
