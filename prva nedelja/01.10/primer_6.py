import pandas as pd
import requests
from matplotlib import pyplot as plt# ili import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])



url = "https://people.vts.su.ac.rs/~papzoli/SAP/Podaci/turisti-podaci.csv"

s = requests.get(url)
with open('turisti.csv','wb') as file:
    file.write(s.content)


df = pd.read_csv('turisti.csv')
print(df)

# plt.figure(figsize=(10,15))
# df.plot.bar(y='Broj turista', legend=False, figsize=(10,15))
# plt.xticks(rotation=90)
#
# plt.show()

# fig,ax = plt.subplots(figsize=(12,9))#omogucava da na jednu figuru stavim vise
# df.plot.bar(y='Broj turista',legend=False,ax=ax)
# plt.xticks(rotation=45)
# ax.set_xlabel('Država')
# ax.set_ylabel('Broj turista')
# fig=ax.get_figure()
# fig.savefig('turisti.png')
# plt.show()

ax = df.plot.hist(y='Broj turista', legend=False, figsize=(10,15), title="Broj turista")#autopct='%1.1f%%'
ax.set_ylabel("")
plt.show()#da probamo aps frek ili %

