# import libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def getPc(lista, valor):
    total = 0
    for x in lista:
        total += x
    pc = (valor*100)/total
    return pc

#lista
casos = np.array([474, 1019, 1482, 10220, 1741, 701, 2177, 992, 3055])
cidades = np.array(['Central', 'Ibipeba', 'Ibititá', 'Irecê', 'João Dourado', 'Jussara', 'Lapão', 'Uibaí', 'Xique-Xique'])

city = list()


print(city)

#dados em series
Series = pd.Series(casos,index=cidades, name="Casos covid região de Irecê (Cidades)")
#plotagem em formato de pizza
Series.plot.pie(figsize=(4,4))
#exibe o gráfico
plt.show()
