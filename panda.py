import pandas as pd

# working with data tabulation and file

data = {
    "Age":[10, 12, 24, 23, 23, 10, 10],
    "Names" : ["Yolo","Pack", "Bob", "Lesly","Amou", "Lola", "Timi"],
    "Profession":["Homeless", "Jobless", "Doctor", "Scientist", "Web Developper", "Graphiste", "Homeless" ]
}

df = pd.DataFrame(data)

# print(df)
# print(df["Names"])
print(df.iloc[1:4]) # un peu contreintuitif 0:1 premiere ligne la ligne des headers n'est pas considéré comme une ligne :(
# 1:4 montre moi les ligne de index 1 a index 4 exclus

df["Characteristics"] = ["Ugly", "Awesome", "Red", "Angry", "", "", ""] # a ligne has to much other ligne length

print(df[df["Characteristics"] == "Red"])

print(df["Age"].mean())
print(df["Age"].median())

df.drop("Age",axis=1,inplace=True)

print(df)

print(df.describe())

df.to_csv("myexcel.csv", index=False)

