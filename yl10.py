name = input("Mis su nimi on?: ")

print("Hommik",name,)

elukoht = input("Kus sa viibid?: ")

if elukoht == "Saaremaa":
    print("Väga normaalne ju")

age = int(input("Kui vana sa oled?: "))

if age < 18:
    print("Väga noor, et autot juhtida.")
elif age == 18:
    print("Palju õnne Täisealiseks saamiseks.")
elif age > 18:
    print("Võid autotjuhtida.")