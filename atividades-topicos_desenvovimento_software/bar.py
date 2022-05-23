# import libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

casos = np.array([474, 1019, 1482, 10220, 1741, 701, 2177, 992, 3055])
cidades = np.array(['Central', 'Ibipeba', 'Ibititá', 'Irecê', 'João Dourado', 'Jussara', 'Lapão', 'Uibaí', 'Xique-Xique'])

speed = [0.1, 17.5, 40, 48, 52, 69, 88]

lifespan = [2, 8, 70, 1.5, 25, 12, 28]

index = ['snail', 'pig', 'elephant',

         'rabbit', 'giraffe', 'coyote', 'horse']

df = pd.DataFrame({'speed': speed,

                   'lifespan': lifespan}, index=index)

ax = df.plot.bar(rot=0)
