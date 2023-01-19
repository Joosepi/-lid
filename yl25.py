diary = {
"Name": "Martin Joosep",
"Lastname": "Reiljan",
"Birth": "2005",
"Location": "Kureaare",
"Favourite dessert": "Hesburger"
}

print(diary.get("Location"))
print(diary["Location"])

diary.update({"Favourite dessert": "melon" })

print(diary.keys())

print(diary.values())

if 'Social Security Number' in diary :
    print("Has Social Security Number")
else:
    print("Doenst have Social Security Number")

print(len(diary))

diary.update({"Tallness": len(diary)})

diary.pop("Birth")

del diary