def main():
    print("This programme will provide the acronym after inputting a phrase.")
    phrase = input("Please enter a phrase to convert : ")
    words = phrase.split()
    acronym = ""

    for word in words:
        acronym += word[0]
    acronym = acronym.upper()
    print(acronym)


main()
