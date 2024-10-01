import pandas as pd
import requests
from matplotlib import pyplot as plt# ili import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv('nivo-secera.csv')

fig,ax = plt.subplots(figsize=(12,9))#omogucava da na jednu figuru stavim vise
df.hist(y='Broj turista',legend=False,ax=ax)
plt.xticks(rotation=45)
ax.set_xlabel('Država')
ax.set_ylabel('Broj turista')
fig=ax.get_figure()
fig.savefig('turisti.png')
plt.show()
