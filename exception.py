#exception with ZeroDivision (chapitre a approfondir plus tard en sachant toutes les exception)

try:
    resultat = 10 / 0
except ZeroDivisionError: 
    print("erreur division par zero")
finally : 
    print("is printed anyway")