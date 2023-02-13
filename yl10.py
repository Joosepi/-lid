name = input("Mis on sinu nimi? ")
print("Tere, " + name + "!")

location = input("Kus sa elad? ")
if location == "Saaremaa":
    print("Saaremaa on ilus saar!")

age = int(input("Kui vana sa oled? "))
if age < 18:
    print("Sa oled liiga noor, et sõita.")
elif age == 18:
    print("Õnnitleme teid täiskasvanuks saamise puhul!")
else:
    print("Saate sõita.")