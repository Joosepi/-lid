fruits = ["Õun", "Banana","Watermelon"]

print(fruits)

print("Esimesed puuviljad:", fruits[0])

fruits.append("Mango")
print("Viimane puuvilid:", fruits[len(fruits)-1])

fruits[1] = "Apelsin"
print(fruits)

if "Õun" in fruits:
    print("Õun on.")
else:
    print("Õun pole.")

print("Listides on:", len(fruits),)

fruits.remove("Watermelon")
print(fruits)

fruits.reverse()
fruits.sort()
print(fruits)