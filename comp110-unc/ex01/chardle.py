"""EX01 - Chardle - A cute step toward wordle."""

__author__: str = "730573785"

five_character_word: str = input("Enter a 5-character word: ")

if (len(five_character_word) != 5):
    print("Error: Word must contain 5 chracters")
    exit()

single_letter: str = input("Enter a single letter character: ")

if (len(single_letter) != 1):
    print("Error: Character must be a single character.")
    exit()

letter_count: int = 0

print("Searching for " + single_letter + " in " + five_character_word)

if (single_letter == five_character_word[0]):
    print(single_letter + " found at index 0")
    letter_count += 1

if (single_letter == five_character_word[1]):
    print(single_letter + " found at index 1")
    letter_count += 1

if (single_letter == five_character_word[2]):
    print(single_letter + " found at index 2")
    letter_count += 1

if (single_letter == five_character_word[3]):
    print(single_letter + " found at index 3")
    letter_count += 1

if (single_letter == five_character_word[4]):
    print(single_letter + " found at index 4")
    letter_count += 1

if (letter_count == 0):
    print("No instances of " + single_letter + " found in " + five_character_word)

if (letter_count == 1):
    print("1 instance of " + single_letter + " found in " + five_character_word)

if (letter_count == 2):
    print("2 instances of " + single_letter + " found in " + five_character_word)

if (letter_count == 3):
    print("3 instances of " + single_letter + " found in " + five_character_word)

if (letter_count == 4):
    print("4 instances of " + single_letter + " found in " + five_character_word)

if (letter_count == 5):
    print("5 instances of " + single_letter + " found in " + five_character_word)
