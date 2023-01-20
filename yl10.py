name = input("Mis su nimi on?: ")

print("Hommik",name,)

Location = input("Kus sa viibid?: ")

if Location == "Saaremaa":
    print("Väga normaalne ju")

age = int(input("Kui vana sa oled?: "))

if age < 18:
    print("Väga noor, et autot juhtida.")
elif age == 18:
    print("Palju õnne Täisealiseks saamiseks.")
elif age > 18:
    print("Võid autotjuhtida.")