# creation d'un dictionnaire

dict = {"paris": 200, "lyon":400, "marseille": 100}

print (dict ["lyon"])

dict["marseille"] = 300

print(dict)

# ajout suppression modification 

dict.update({"unknow":1000})

print (dict)

#suppression
dict.pop("paris")

print(dict)

# utils 

print(dict.keys())

print(dict.get("unknow"))

dict.setdefault("bordeau")

print(dict)
dict.setdefault("anger", "ok")

print(dict)

print ( len(dict))

# pas de tuples car trop simple 
# pas de set car trop complexe pour trouver des cas d'utilisation 