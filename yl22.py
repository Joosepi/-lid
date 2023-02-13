# Juhusliku valiku valimiseks importige arvutisse juhuslik teek
import random

# Valikute loend
options = ["kivi", "paber", "käärid"]

# Funktsioon mängu mängimiseks
def play_game():
    # Arvuti teeb juhusliku valiku
    computer_choice = random.choice(options)

    # Kasutaja teeb valiku
    user_choice = input("Valige kivi, paber või käärid: ")

    # Kontrollige, kes mängu võidab
    if computer_choice == user_choice:
        print("Viik!")
    elif (computer_choice == "kivi" and user_choice == "käärid") or (computer_choice == "paber" and user_choice == "kivi") or (computer_choice == "käärid" and user_choice == "paber"):
        print("Arvuti võitis!")
    else:
        print("Kasutaja võitis!")

# Mängutsükkel mitme mängu mängimiseks
while True:
    play_game()
    play_again = input("Kas soovid veel mängida (jah/ei)? ")
    if play_again.lower() == "ei":
        break

# Hüvastijätu sõnum
print("Lõpetame mängimise, tänan, et mängisite!")