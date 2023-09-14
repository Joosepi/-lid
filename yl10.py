# Prompt the user to enter their name and store it in the 'name' variable
name = input("Mis on sinu nimi? ")

# Print a greeting message including the user's name
print("Tere, " + name + "!")

# Prompt the user to enter their location and store it in the 'location' variable
location = input("Kus sa elad? ")

# Check if the user's location is "Saaremaa" and provide a specific message if it is
if location == "Saaremaa":
    print("Saaremaa on ilus saar!")

# Prompt the user to enter their age and convert it to an integer
age = int(input("Kui vana sa oled? "))

# Check the user's age and provide different messages based on the age
if age < 18:
    print("Sa oled liiga noor, et sõita.")
elif age == 18:
    print("Õnnitleme teid täiskasvanuks saamise puhul!")
else:
    print("Saate sõita.")
