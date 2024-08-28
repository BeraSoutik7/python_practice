a = "hello"
b = "World"

print(a+b) # Contacatenation

print(a*2) # Multiplication

print(a[-1]) # Indexing
print(a[len(a)-1]) # Neg Indexing

#Slicing
 
print(a[1 : len(a)])
print(a[:2])

print (a[-4:])


# Ends with 
c = a.endswith("llo")
print(c)
print(type(a.endswith("llo")))
print(a.endswith("llo"))

#Capitalize

print(a.capitalize())
a =  a.capitalize()
print(a)

# Replace ("Old", "New")

print(a.replace("H","T"))
print(a)

#Find

print (a.find("l")) 

#count

print(a.count("y"))








