#ecriture 

with open("hello.txt", "w") as file :
    file.write("Hi!\n")
    file.write("Cc!\n")

#lecture
with open("hello.txt", "r") as file :
    content = file.read()
    print(content)

# ecriture and loops
    
with open("numbers.txt","w") as file:
    for i in range(10):
        file.write(str(i))
    else:
        file.write("\n")

with open("numbers.txt","r") as file:
    print(file.read())


#remove content (all)

with open("numbers.txt","w+") as file:
    file.truncate(0)
    print(file.read())


#interaction with user and files


content = None
while content != "Nothing" : 
    content = input("what to add in my new file")
    with open("clientwish.txt","a") as file: #w it will overwritten "a" => append mode 
        file.write(content)
   