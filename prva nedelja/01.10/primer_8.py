import pandas as pd
import requests
from matplotlib import pyplot as plt
import seaborn as sns

url = "https://people.vts.su.ac.rs/~papzoli/SAP/Podaci/nivo-secera.csv"

s = requests.get(url)
with open('secer.csv','wb') as file:
    file.write(s.content)


df = pd.read_csv('secer.csv')
# print(df)

# plt.figure(figsize=(10,15))
# df.plot.bar(y='Broj turista',legend=False)
# plt.xticks(rotation=45)
# plt.show()

# 1. metoda: Pandas
fig,ax = plt.subplots(figsize=(12,9))
df.plot.hist(bins=4, ax=ax, legend=False)
# plt.xticks(rotation=45)
ax.set_xlabel('Nivo šećera u ')
ax.set_ylabel('Broj pacijenata')
# fig=ax.get_figure()
# fig.savefig('turisti.png')
plt.show()

# 2. metoda: Seaborn

# plt.figure(figsize=(12,8))
# sns.histplot(df,bins=4,legend=False)
# plt.title('Histogram pomoću paketa Seaborn')
# plt.xlabel('Nivo šećera u krvi')
# plt.ylabel('Broj pacijenata')
# plt.show()