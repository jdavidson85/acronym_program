print("This programme will provide the acronym after inputting a phrase.")

phrase = input("Please enter a phrase to convert : ")
list_of_words = phrase.split()
add_acronym = ''

for word in list_of_words:
    add_acronym = add_acronym + word[0]

new_acronym = add_acronym.upper()

print(new_acronym)