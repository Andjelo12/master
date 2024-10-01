import pandas as pd
import requests
import sidetable as stb
import matplotlib

url="https://people.vts.su.ac.rs/~papzoli/SAP/Podaci/nivo-secera.csv"

s=requests.get(url)
with open('nivo-secera.csv','wb') as file:
    file.write(s.content)

df=pd.read_csv('nivo-secera.csv')
print(df)
print(df.info())

num_bins=4
df['Binned']=pd.qcut(df['Secer'],q=num_bins)
print(df)

# print(df.head(10))

# freq_table1=pd.pivot_table(df, index=['Vodostaj'],aggfunc='size').reset_index(name='Frequency')#ili index=['Vodostaj]
freq_table=df.stb.freq(['Binned'])
print(freq_table)
# freq_table1['Rel. Frequency']=freq_table1['Frequency']/len(df)*100
# print(freq_table1)

#freq_table2=df.stb.freq([
#    'Vodostaj'
#])
#print(freq_table2)
