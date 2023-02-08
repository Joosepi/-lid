import time
import random

name = input("Tere, mis on sinu nimi? ")

time.sleep(2)
print("Tere " + name)

feeling = input("Kuidas on sul? ")

time.sleep(2)
if "good" in feeling:
    print("Ma tunnen ennast hästi!")
else:
    print("Mul on kahju sellest kuulda")

time.sleep(2)
favcolour = input("Mis on sinu lemmikvärv? ")

colours = ["Punane","Roheline","Sinine"]

time.sleep(2)
print("Minu lemmikvärv on " + random.choice(colours))