dictionary = { #This is the information board
  "name": "Martin Joosep",
  "lastname": "Reiljan",
  "age": 17,
  "birth_year": 2005,
  "residence": "Kuressaare",
  "dessert": "Burger"
}

print(dictionary.get('residence')) #It brings residence out of the dictionary.
print(dictionary['residence']) #This prints the residence 

dictionary['dessert'] = 'Burger' #Defines the burger as a dessert.

for k, v in dictionary.items():
    print(k, v)

x = dictionary.get("dessert") #Gets my Dessert value from the Dictionary.
print(x)

keys = dictionary.keys()
print(keys)

keyToFind = 'ID' #Finds my ID

if dictionary.get('ID') == None:
  print('ID Hasnt been found in this dictionary') #Doesn't find it.
else:
  print('ID Has been found in this dictionary') #Does find it.

print("Dictionary size: ", len(dictionary), "elements") #Print's the size of the Dictionary.

print(len(dictionary))

dictionary["height"] = "My height: 185cm" #This is my height
#print(dictionary)

print(dictionary.get("height")) #Prints the height.


del dictionary['birth_year'] #It deletes birth year from the this print.
print(dictionary) #Prints the dictionary.