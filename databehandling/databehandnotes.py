#1 Dimensionella "Listor"
import pandas as pd
from docs.conf import language

data = dict(Ai = 25, NET = 30, APP = 30, JAVA = 27)

series_programs = pd.Series(data)
print(series_programs)

#extract values

print(f"series_program[0] -> {series_programs[0]}")
print(f"series_program[-1] -> {series_programs[-1]}")

#get the keys
#kan behandlas som en lista
print(f"series_programs.keys() -> {series_programs.keys()}")
print(f"series_programs.keys() -> {series_programs.keys()[2]}")

##

import random as rnd

#inte använda seed, läraren gör det i info-syfte.
rnd.seed(42) #

# create series using list

dice_series = pd.Series([rnd.randint(1, 6) for _ in range(5)])
print(dice_series)

#
print(f"Min value: {dice_series.min()}")
print(f"Mean value: {dice_series.mean()}")
print(f"Median value: {dice_series.median()}")

#2D, dataframes
#annan sorts dict, där varje kolumn är mappar till en serie, en dataframe är en antal serier ihopsatta.


df_programs = pd.DataFrame(series_programs, columns = ("Num students",))
print(df_programs)

#
language = pd.Series(dict(AI="Python", NET="C#", APP="Koitlin", Java="Java"))

df_programs = pd.DataFrame({"Students": series_programs, "Language":language})
print(df_programs)

#för att få fram index
df_programs.index

#data selection, dictionary och attribute indexing

print(df_programs["Students"])

# välja ut vilka kolumner man vill ha och även bygga "ny" data utav de.
#använder man jupyter så behöver man inte skriva PRINT INNAN.
#EX: df_programs["Language", "Students"]
print(df_programs[["Language", "Students"]])

#plocka ut vissa
df_programs["Language"]["NET"]
print(df_programs["Language"]["NET"])

#Indexering, slicing interface

print(df_programs.loc["Java"])

print(df_programs.loc[["Java", "APP"]])

#"riktig slicing" iloc, slicar direkt på index, plockar ut olika delar.

print(df_programs.iloc[1:3])

#viktig grej för att välja saker, masking
#Masking- False eller True

print(df_programs["Students"] > 25)

#går att använda som en mask

df_over_25 = df_programs[df_programs["Students"] > 25]
print(df_over_25)

#Read excel data: pandas för att läsa olika/kända filformat
#kaggle för fler ex.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("../Data/calories.xlsx")
df.head() # visar dom 5 översta i en dataframe, man kan lägga
          # till ett värde i: () för att få fler rader.
#

df.info() # vi får fram mycket/all info angående om datan.
#data frames tar upp mycket minne när dom är stora

#kan få fram information om vissa delar

df["FoodCategory"].unique() # går igenom en lista bara en gång,
                           # array

# fast eller flytande

df["per100grams"].unique()

#Data cleaning, alla datatyper är objekt, måste konverteras
#till int för att kunna använda siffror

df = df.rename(dict(Cals_per100grams="Calories", per100grams="percent", KJ_per100grams="kJ"), axis="columns")
df.head()

#astype = pandas
df ["Calories"] = df["Calories"].str[:-3].astype(int)
df.head()   #omvandlat calories till int istället

#check number of values in solids and liquids

df["per100"].value_counts()

#separer dom i solids och liquids

liquids = df[df["per100"] == "100ml"]
liquids.head()

# solids
solids = df[df["per100"] == "100g"]
solids.head()

#Fint out top 5 categoires of highest calories

solids_sorted = solids.sort_values(by="Calories", ascending=False)
solids_top5 = solids.sorted.iloc[:5] #eller head(5)
print(solids_top5)

# top 5 liquids in calories
liquids_top5 = liquids.sort_values(by="Calories", ascending=False)
print(liquids_top5)

# topp 5 av median värdena, df.groupby:sorterar inom/först inom FoodCategory

top5_median = df.groupby("FoodCategory").median(numeric_only=True).sort_values(by="Calories", ascending=False).head().reset_index()
print(top5_median)

#visualisera datan

fig, axes = plt.subplots(1,3, dpi=120, figsize=(16,4))

titles = ["Solid top 5", "Liquids top 5", "Top 5 per group median"]
data_frames = [solids_top5, liquids_top5, top5_median]
x_column = ["FoodItem", "FoodItem", "FoodCategory"]

for i, (data, title) in enumerate(zip(data_frames, titles)):
    sns.barplot(data=data, x=x_column, y="Calories", ax=axes[i])
    axes[i].set_title(title)
    axes[i].set_xticklabels(axes[i].get_xticklabels(), rotation=90) # rotation 90: på höjd istället för bredden.
# 3 olika plottar med "bars" för varje kategori

#läraren testar sig fram
plt.savefig("calories.png", facecolor="white", bbox_inches="tight")




