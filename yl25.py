dictionary = {
  "name": "Martin Joosep",
  "lastname": "Reiljan",
  "age": 17,
  "birth_year": 2005,
  "residence": "Kuressaare",
  "dessert": "Burger"
}

print(dictionary.get('residence'))
print(dictionary['residence'])

dictionary['dessert'] = 'Burger'

for k, v in dictionary.items():
    print(k, v)

x = dictionary.get("dessert")
print(x)

keys = dictionary.keys()
print(keys)

keyToFind = 'ID'

if dictionary.get('ID') == None:
  print('ID Hasnt been found in this dictionary')
else:
  print('ID Has been found in this dictionary')

print("Dictionary size: ", len(dictionary), "elements")

print(len(dictionary))

dictionary = {
  "name": "Martin Joosep",
  "lastname": "Reiljan",
  "age": 17,
  "birth_year": 2005,
  "residence": "Kuressaare",
  "dessert": "Burger"
}

print(dictionary.get("height"))


del dictionary['birth_year']
print(dictionary)