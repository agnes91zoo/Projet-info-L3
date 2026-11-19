import pandas as pd
df = pd.read_csv("données/Top Movies dataset.csv")
# print(df.shape)
# print(df.columns)
# print(df.head(5))

#nettoyage du csv retirer les colonnes inutiles

df = df.drop(columns=["Title","Overview","Popularity","Vote_Count","Poster_Url","Working URL"])
# print(df.head(5))

#suppressions des colonnes avec des cases vides 

# print(df.isna().sum())
df = df.dropna()
# print(df.isna().sum())

#suppressions des doublons 

# print(df.duplicated().sum())
df = df.drop_duplicates()
# print(df.duplicated().sum())


#Modification de la date de sortie en format date JJ/MM/AAAA puis on ajoute 2 colonnes month et year

df["Release_Date"] = pd.to_datetime(df["Release_Date"], dayfirst=True)
df["Year"] = df["Release_Date"].dt.year
df["Month"] = df["Release_Date"].dt.month
df = df.drop(columns=["Release_Date"])
# print(df.head(5))

#Il y a plusieurs genre listé dans la catégorie genre donc chaque genre attribué devient une colonne de notre tableau

print(df["Genre"].head(10).tolist())
dummies = df["Genre"].str.replace(", ", ",", regex=False).str.get_dummies(sep=",") #str.replace c'est parce que des fois les virgules 
#sont pas aux memes endroits et ça crée des colonnes en double pour le meme genre
df = pd.concat([df, dummies], axis=1)
df = df.drop(columns=["Genre"])
print(df.head(5))
print(df.columns)
