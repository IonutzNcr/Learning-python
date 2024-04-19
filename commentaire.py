# im a commentaire
print("cool")

#im a docstring 

""" 
Hey is not working why
Ok its working but the color is not good
"""


def addToNumbers() : 
    """
    Take no args 
    Do a simple addition with 1 and 1 
    """
    return 1 + 1 

print(addToNumbers())


print(addToNumbers.__doc__)