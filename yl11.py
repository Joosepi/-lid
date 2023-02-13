# Küsime kasutajalt sisendina stringi
input_string = input("Sisestage string: ")

# Eemaldame selle sisendi algusest ja lõpust tühikud
input_string = input_string.strip()

# Kontrollime, kas string vastab tingimustele
# et selles on vähemalt seitse sümbolit ja et sümbolite arv on paarituarvuline
if len(input_string) < 7 or len(input_string) % 2 == 0:
    print("Sisestatud string ei vasta tingimustele")
else:
    # Leiame keskmised sümbolid
    mid_index = len(input_string) // 2
    mid_characters = input_string[mid_index - 1:mid_index + 2]

    # Väljastame kolm keskmist sümbolit
    print("Keskmised sümbolid:", mid_characters)