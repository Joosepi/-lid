a=input("Number: ")

def upc(a):
    a = str(a)
    counter = 0
    x = 0
    y = 0

    if len(a) < 11:
        a = ("0")*(11-len(a))+a
    for n in a:
        if counter % 2 == 0:
            x += int(n)
        else:
            y += int(n)
        counter += 1
    M = ((x*3)+y) % 10
    if M != 0:
        return 10 - M
    else:
        return 0

print(upc(a))