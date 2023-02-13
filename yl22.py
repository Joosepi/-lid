import random

# Küsime kasutajalt valikut (kivi, paber, käärid)
user_action = input("Sisesta oma valik (kivi, paber, käärid): ")

# Määrame võimalikud valikud
possible_actions = ["kivi", "paber", "käärid"]

# Arvuti teeb juhusliku valiku
computer_action = random.choice(possible_actions)

# Kui kasutaja ja arvuti valikud on samad, on see viik
if user_action == computer_action:
    print(f"Mõlemad valisid {user_action}. viik!")

# Kui kasutaja valis kivi
elif user_action == "Kivi":
    if computer_action == "Käärid":
        print("Kivi smashes Käärid! Sa võitsid!")
    else:
        print("Paber peitab kivi! Sa kaotasid.")

# Kui kasutaja valis paber
elif user_action == "paber":
    if computer_action == "Kivi":
        print("Paber peitab Kivi! Sa võitsid!")
    else:
        print("Käärid lõikab paber! Sa kaotasid.")

# Kui kasutaja valis käärid
elif user_action == "Käärid":
    if computer_action == "paber":
        print("Käärid lõikab paper! Sa võitsid!")
    else:
        print("Kivi purustab Käärid! Sa kaotasid."):