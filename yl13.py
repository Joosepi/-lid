# Küsime kasutajalt tema lemmiklooma
favorite_animal = input("Mis on sinu lemmikloom? ")

# Leiame esimese tähe
first_letter = favorite_animal[0]
# Väljastame esimese tähe
print("Sinu lemmiklooma esimene täht on:", first_letter)

# Loome loomade nimekirja
animal_list = ["koer", "kass", "lind"]
# Lisa lemmikloom nimekirja
animal_list.append(favorite_animal)
# Väljastame nimekirja
print("Loomade nimekiri:", animal_list)

# Leiame viimase elementi viimase tähe
last_letter_of_last_element = animal_list[-1][-1]
# Väljastame viimase elementi viimase tähe
print("Viimase elementi viimane täht on:", last_letter_of_last_element)