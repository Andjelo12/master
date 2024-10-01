import pandas as pd
import sidetable as stb
import matplotlib.pyplot as plt
import requests
import io
# import seaborn as sns

## Ucitavanje podataka
url = "https://people.vts.su.ac.rs/~papzoli/SAP/Podaci/titanic.csv"
s=requests.get(url).content
titanic = pd.read_csv(io.StringIO(s.decode('utf-8')))

## Pregled i informacije o podacima

print(titanic.head())
#
# print(titanic.info())

## Preciscavanje podataka

titanic_new = titanic.drop(['Cabin','PassengerId','Name','Ticket'],axis=1)
print(titanic_new.head())

## Vizuelizacija podataka

# Umesto skracenica luka, uvodimo pune nazive luka

titanic_new.loc[:,'Embarked'].replace(['S','C','Q'],['Southampton','Cherbourg','Queenstown'],inplace=True)
print(titanic_new.head())

# Umesto 0, 1 u koloni Survived, uvodimo, No, Yes
#
titanic_new.loc[:,'Survived'].replace([0,1],['No','Yes'],inplace=True)
# print(titanic_new.head())

## Graficki prikaz podataka

# Proporcija putnika ukrcanih na lukama
#
embarked_freq = titanic_new.stb.freq(['Embarked'])
print(embarked_freq)
#
fig1, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 5))
#
#
a=embarked_freq.plot.pie(y='count',autopct='%1.1f%%',legend=False,ax=ax2)
# #
a.set(ylabel=None)
b=embarked_freq.plot.bar(y='count',rot=0,legend=False,ax=ax1)
b.set(xlabel=None)
#
plt.suptitle('Odnos ukrcanih putnika po lukama')
#
plt.show()
fig1.savefig('putnici-luka.png')
plt.close(fig1)

# korelacija izmedju mesta ukrcavanja i prezivelih
#
c=100.*titanic_new.groupby(['Embarked'])['Survived'].value_counts(normalize=True)
print(c)