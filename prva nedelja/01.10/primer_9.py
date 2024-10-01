import pandas as pd
import requests
from matplotlib import pyplot as plt
import seaborn as sns

url = "https://people.vts.su.ac.rs/%7Epapzoli/SAP/Podaci/titanic.csv"

s = requests.get(url)
with open('titanic.csv','wb') as file:
    file.write(s.content)

titanic = pd.read_csv('titanic.csv')

# print('Deo tabele:')
#
print(titanic.head())
#
# print('Informacija o podacima')
#
print(titanic.info())

# Srednja vrednost starosti

age_mean = titanic["Age"].mean()
#
print(f'Prosek starosti je {age_mean:.2f} godina.')
#
# # Medijana gstarosti i cene karte
#
medijana = titanic[["Age", "Fare"]].median().round(2)
print(medijana)

#
# # Sve deskriptivne statistike za starost i cenu karte
#
deskriptivne_statistike = titanic[["Age", "Fare"]].describe()
#
print(deskriptivne_statistike.round(2))
#
# # Deskriptivne statistike grupisane po kategoriji
#
# # Prosecna starost muskaraca vs zena
#
prosecna_starost = titanic[["Sex", "Age"]].groupby("Sex").mean()
#
print(prosecna_starost)
#
# # Prosecna cena karte grupisana po polu i klasi
#
prosecna_cena = titanic.groupby(["Sex", "Pclass"])["Fare"].mean()
#
print(prosecna_cena.round(2))