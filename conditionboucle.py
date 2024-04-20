#condition

age = 18

if age < 18 :
    print("mineur")
else:
    print("majeur")


#boucle
#for 
for i in range(3) : #is it printing 3x or 4x ??
    print(i)

#while
x = 0
while x < 3 :
    print("while ",x)
    x = x+1
else:
    print("fin de loop")

#ternaire
status = "mineur" if age < 18 else "majeur"
print("t'es ",status)

#comprehension de liste

mylist = [x*2 for x in range(2)]
print(mylist)

#double loop
mysecondlist = [x*y for x in [1,2,3] for y in [4,1,2]]
print (mysecondlist)

#conditional 
mythirdlist = [x*2 for x in [1,2,3] if x % 2 == 0]
print(mythirdlist)