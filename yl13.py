favorite_animal = input("What is your favorite animal? ")

first_letter = favorite_animal[0]
print("The first letter of your favorite animal is:", first_letter)

animal_list = ["dog", "cat", "bird"]
animal_list.append(favorite_animal)
print("The list of animals:", animal_list)

last_letter_of_last_element = animal_list[-1][-1]
print("The last letter of the last element in the list is:", last_letter_of_last_element)