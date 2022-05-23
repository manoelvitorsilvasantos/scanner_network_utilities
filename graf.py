import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados.csv")
df.plot(x="Rank", y=["INFO", "TES", "FSADS"])
plt.show()
