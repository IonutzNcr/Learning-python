#liste

maliste = [1,2,3,4]
malistebordelique = ["a", 3, 400, False, None]

#acceder a une valeur | index = 0 
print (maliste[0])
print (maliste[2])
print (malistebordelique[4])

#modifier une valeur 
maliste[0] = 10

print(maliste[0])

malistebordelique[4] = True

print(malistebordelique[4])

#methodes utiles 

# ajout et suppresision
# ajouter un element à la fin de la liste

maliste.append(5)

#etendre la liste avec une autre liste ou iterable

maliste.extend([6,7,8])

#inserer un element a une position

maliste.insert(0,0)

print (maliste)


#enlever un element

maliste.remove(10)

#len donne la taille de la liste
maliste.pop(len(maliste) - 2) # supprime le l'avant dernier element de la liste 

print(maliste)

#maliste.clear() # enleve tout les element de la liste

#print(maliste)

# recherche et try 
print(malistebordelique)
malistebordelique.reverse()
print(malistebordelique)

# malistebordelique.sort()  sort doesnt work an a list with different types int x str

# print(malistebordelique)

stringlist = ["c", "a", "d"]
stringlist.sort()
print(stringlist)


maliste.sort()

print(maliste)
# copy superficielle? ==> impact when the list contained mutable element like objects or other liste 
stringlisttwo = stringlist.copy()
stringlisttwo[0] = 2

print(stringlist)
print(stringlisttwo)







