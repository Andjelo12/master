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
embarked_freq = titanic_new.stb.freq(['Embarked']).set_xindex(['Embarked'])
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
# fig1.savefig('putnici-luka.png')
# plt.close(fig1)

# korelacija izmedju mesta ukrcavanja i prezivelih
#
c=100.*titanic_new.groupby(['Embarked'])['Survived'].value_counts(normalize=True)
print(c)
# print(c.unstack())
# ax2 = c.unstack().plot.bar(rot=0)
fig2 = ax2.get_figure()
# plt.show()
# fig2.savefig('luka_vs_preziveli.png')
# plt.close(fig2)

# korelacija izmedju mesta ukrcavanja i klase

#
d = 100.*titanic_new.groupby(['Embarked'])['Pclass'].value_counts(normalize=True,sort=False)
print(d)
# ax3 = d.unstack().plot.bar(rot=0)
# fig3 = ax3.get_figure()

# plt.show()
# fig3.savefig('luka_vs_klasa.png')
# plt.close(fig3)

# odnos prezivelih i umrlih u odnosu a klasu
#
e = 100.*titanic_new.groupby(['Pclass'])['Survived'].value_counts(normalize=True,sort=False)
print(e)
# ax4 = e.unstack().plot.bar(rot=0)
# fig4 = ax4.get_figure()
# plt.show()
# fig4.savefig('preziveli_vs_klasa.png')
# plt.close(fig4)

# Odnos muskog i zenskog pola u zavisnosti od ukrcavanja
#
f = 100.*titanic_new.groupby(['Embarked'])['Sex'].value_counts(normalize=True,sort=False)
print(f)
# ax5 = f.unstack().plot.bar(rot=0,color=['pink','blue'])
# fig5 = ax5.get_figure()
# plt.show()
# fig5.savefig('pol_vs_luka.png')
# plt.close(fig5)

# Ukupni odnos zenskog i muskog pola

sex_freq = titanic_new.stb.freq(['Sex']).set_index(['Sex'])
print(sex_freq)
#
# fig6, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 5))

#
# g=sex_freq.plot.pie(y='count',autopct='%1.1f%%',legend=False,ax=ax2,colors=['blue','pink'])
# #
# g.set(ylabel=None)
# h=sex_freq.plot.bar(y='count',rot=0,legend=False,ax=ax1,color=['blue','pink'])
# h.set(xlabel=None)

# plt.suptitle('Odnos muškog i ženskog pola')
#
# plt.show()
# fig6.savefig('pol.png')
# plt.close(fig6)

# Proporcija muskog i zenskog pola u odnosu na klasu

i = 100.*titanic_new.groupby(['Pclass'])['Sex'].value_counts(normalize=True,sort=False)
print(i)
# ax7 = i.unstack().plot.bar(rot=0,color=['pink','blue'])
# fig7 = ax7.get_figure()
# plt.show()
# fig7.savefig('pol_vs_klasa.png')
# plt.close(fig7)

# Odnos muskog i zenskog pola koji su preziveli

j = 100.*titanic_new.groupby(['Survived'])['Sex'].value_counts(normalize=True,sort=False)
print(j)
# ax8 = j.unstack().plot.bar(rot=0,color=['pink','blue'])
# fig8 = ax8.get_figure()
# plt.show()
# fig8.savefig('preziveli_vs_pol.png')
# plt.close(fig8)

# korelacija prezivelih sa klasom i polom

k = titanic_new.groupby(['Pclass','Sex'])['Survived'].value_counts(normalize=True,sort=False).unstack()['Yes'].unstack()
print(k)

# ax9 = k.plot.bar(stacked=False,rot=0,color=['pink','blue'])
# fig9 = ax9.get_figure()
# plt.show()
# fig9.savefig('preziveli_klasa_pol.png')
# plt.close(fig9)

## Analiza starosti putnika
#
print(titanic.info()) # informacije

# Tabela koja sadrzi samo one putnike kojima je poznata starost

starost = titanic_new[titanic_new['Age'].notnull()]
print(starost.info())

# fig10,ax = plt.figure()
starost.hist(column='Age',bins=11)
# ax = ax10.ravel() # Unpack all of the subplot arrays from axes
# fig = ax[0].get_figure()
plt.show()
# fig = ax.get_figure()
# fig.savefig('starost_histogram.png')

# Deskriptivna statistika

deskriptivna_stat = pd.DataFrame(starost['Age'].describe())
deskriptivna_stat.index=['Velicina populacije','Srednja vrednost','Standardno odstupanje','Minimum','25 kvantil','Medijana','75 kvantil','Maksimum']
print(deskriptivna_stat.round(decimals=3))

# Histogram starosti po prezivelima i umrlima

# ax11=starost.hist(column='Age',by='Survived',sharey=True,density=True)
# ax = ax11.ravel() # Unpack all of the subplot arrays from axes
# fig = ax[0].get_figure()
plt.suptitle('Raspodela starosti grupisana po preživelima')
plt.show()
# fig = ax.get_figure()
# fig.savefig('starost_preziveli_umrli_histogram.png')

# Deskriptivne statistike grupisane po preživelima i umrlima

starost_grupisana = pd.DataFrame()
# starost_grupisana
preziveli = starost['Age'][starost['Survived']=='Yes'].describe()
print(preziveli)
poginuli = starost['Age'][starost['Survived']=='No'].describe()
starost_grupisana['Preziveli'] = preziveli
starost_grupisana['Poginuli'] = poginuli
starost_grupisana.index=['Velicina populacije','Srednja vrednost','Standardno odstupanje','Minimum','25 kvantil','Medijana','75 kvantil','Maksimum']
print(starost_grupisana.round(decimals=3))
