import pandas as pd
import requests
import sidetable as stb

url="https://people.vts.su.ac.rs/~papzoli/SAP/Podaci/nivo-secera.csv"

s=requests.get(url)
with open('secer.csv','wb') as file:
    file.write(s.content)

df=pd.read_csv('secer.csv')
print(df)
print(df.info())
