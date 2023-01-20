import random

user_action = input("Sisesta oma valik (kivi, paber, käärid): ")
possible_actions = ["kivi", "paber", "käärid"]
computer_action = random.choice(possible_actions)
if user_action == computer_action:
    print(f"Mõlemad valisid {user_action}. viik!")
elif user_action == "Kivi":
    if computer_action == "scissors":
        print("Kivi smashes scissors! Sa võitsid!")
    else:
        print("Paber peitab kivi! Sa kaotasid.")
elif user_action == "paber":
    if computer_action == "Kivi":
        print("Paber peitab Kivi! Sa võitsid!")
    else:
        print("Käärid lõikab paber! Sa kaotasid.")
elif user_action == "käärid":
    if computer_action == "paber":
        print("Käärid lõikab paper! Sa võitsid!")
    else:
        print("Kivi purustab Käärid! Sa kaotasid.")


