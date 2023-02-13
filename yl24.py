# Küsime kasutajalt sisendnumberit
a = input("Sisestage number: ")

# Defineerime funktsiooni, mis arvutab antud numberi UPC kontrollkoodi
def upc(a):
    # Teisendame sisendnumberi stringiks
    a = str(a)
    # Alustame loendurit, mida kasutame paari- ja paaritu numbrite eristamiseks
    counter = 0
    # Alustame summa x, millele lisame paari numbrite väärtused
    x = 0
    # Alustame summa y, millele lisame paaritu numbrite väärtused
    y = 0

    # Kui sisendnumber on väiksem kui 11 sümbolit, lisame number ees nullidega
    if len(a) < 11:
        a = ("0")*(11-len(a))+a
    # Loome tsükli, mis käib läbi igat number sisendnumberis
    for n in a:
        # Kui loendur jagub 2-ga, lisame n paari summa x-le
        if counter % 2 == 0:
            x += int(n)
        # Muul juhul lisame n paaritu summa y-le
        else:
            y += int(n)
        # Suurendame loendurit
        counter += 1
    # Arvutame M-i, mis on ((x * 3) + y) % 10
    M = ((x*3)+y) % 10
    # Kui M pole 0, tagastame 10 - M, muidu 0
    if M != 0:
        return 10 - M
    else:
        return 0

# Prindime funktsiooni tulemuse
print(upc(a))
