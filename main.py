#triple single/double quote converts everything into string
syed='''he said,
i want to go home
i want to enjoy'''
print(syed)


#use of 0,1,2,3,4,...
# splitting of characters
name=("mohsin")
print(name[0])  #m will come (first element)
print(name[1]) #second element
print(name[2]) #third
print(name[3]) #fifth
print(name[4]) #sixth
print(name[5]) #error will come (because only six elements are in name)

#another method (for loop)

#characters in syed
print("using for loop\n")
for characters in syed: #it can also be used for name 
  print(characters)