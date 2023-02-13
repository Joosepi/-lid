# Programm täringumänguks
import random

# Kasutaja sisestab oma arvamuse
give_number = int(input("Viskame täringut. Mis arv see võiks olla?\n"))

# Arvamuste nimekiri algab esimese arvamusega
guessList = []
guessList.append(give_number)

# Genereeritakse juhuslik täringu arv
dice = random.randint(1,6)

# Tehakse arvamusi, kuni see ei vasta täringu arvule
while give_number != dice:
    if give_number > dice:
        give_number = int(input("Vabandust, see vastus on liiga suur! Tee uuesti!\n"))
        # Lisatakse arvamus nimekirja ainult siis, kui see pole seal veel
        if give_number not in guessList:
            guessList.append(give_number)
    if give_number < dice:
        give_number = int(input("Vabandust, see vastus on liiga väike! Tee uuesti!\n"))
        # Lisatakse arvamus nimekirja ainult siis, kui see pole seal veel
        if give_number not in guessList:
            guessList.append(give_number)

# Viimane arvamus lisatakse nimekirja
if give_number not in guessList:
    guessList.append(give_number)

# Täringu arv ja mitu arvamust vajas selle leidmiseks
print("Õnnitlused, oled õige! Täringu arv oli {}! See võttis sul {} katset.".format(dice, len(guessList)))
