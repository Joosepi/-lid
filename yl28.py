# Importida ajafunktsioon ja juhuslik valik
import time
import random

# Küsida kasutaja nime
name = input("Tere, mis on sinu nimi? ")

# Oodata 2 sekundit
time.sleep(2)
# Tervitada kasutajat nimepidi
print("Tere " + name)

# Küsida kasutaja enesetunnet
feeling = input("Kuidas on sul? ")

# Oodata 2 sekundit
time.sleep(2)
# Kui kasutaja vastab, et on hästi, siis öelda, et ka ise tunneb ennast hästi
if "hästi" in feeling:
    print("Ma tunnen ennast hästi!")
# Muul juhul öelda, et on kahju sellest kuulda
else:
    print("Mul on kahju sellest kuulda")

# Oodata 2 sekundit
time.sleep(2)
# Küsida kasutaja lemmikvärvi
favcolour = input("Mis on sinu lemmikvärv? ")

# Loetleda valikus värvid
colours = ["Punane","Roheline","Sinine"]

# Oodata 2 sekundit
time.sleep(2)
# Väljastada juhuslik valik lemmikvärvidest
print("Minu lemmikvärv on " + random.choice(colours))