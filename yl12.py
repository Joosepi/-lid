puuviljad = ["Õun", "Banana","Watermelon"]

print(puuviljad)

print("Esimesed puuviljad:", puuviljad[0])

puuviljad.append("Mango")
print("Viimane puuvilid:", puuviljad[len(puuviljad)-1])

puuviljad[1] = "Apelsin"
print(puuviljad)

if "Õun" in puuviljad:
    print("Õun on olemas.")
else:
    print("Õun pole olemas.")

print("Listides on:", len(puuviljad),)

puuviljad.remove("Watermelon")
print(puuviljad)

puuviljad.reverse()
puuviljad.sort()
print(puuviljad)