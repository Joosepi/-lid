# importida re moodul - mitte kasutusel
import re

# defineerime tähed, mida arvutada
letters = "a", "e", "i", "o", "u", "õ", "ä", "ö", "ü"
print(letters)

# küsime kasutajalt sisendit
a = input("Sisesta midagi: ")

# arvutame mitu korda iga täht esineb sisendis
b = a.count("a") + a.count("e") + a.count("i") + a.count("o") + a.count("u") + a.count("õ") + a.count("ä") + a.count("ö") + a.count("ü")

# väljastame tulemuse
print(b)
