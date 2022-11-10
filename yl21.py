import random

give_number = int(input("viskame täringu. mis arv see võiks olla?\n "))
guess_number = 1
guessList = []
guessList.append(give_number)

täring = random.randint(1,6)
while give_number != täring:
    if give_number > täring:
        give_number = int(input("Vabandust, see vastus on liiga suur! Proovi uuesti!\n "))
        if give_number not in guessList:
            guessList.append(give_number)
    if give_number < täring:
        give_number = int(input("Vabandust, see vastus on liiga väike! Proovi uuesit!\n "))
        if give_number not in guessList:
            guessList.append(give_number)

if give_number not in guessList:
    guessList.append(give_number)
print ("Congratulations, you were right, the answer was {}! It took you {} tries.".format(täring, len(guessList)))