"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "370432160"

word_guess: str = input("Enter a 5-character word: ")

if len(word_guess) != 5:
    print("Error: Word must contain 5 characters")
    exit()

character_guess: str = input("Enter a single character: ")

if len(character_guess) != 1:
    print("Error: Character must be a single chracter.")
    exit()

print("Searching for " + character_guess + " in " + word_guess)

total_matches: int = 0

if word_guess[0] == character_guess:
    print(character_guess + " found at index 0")
    total_matches = total_matches + 1

if word_guess[1] == character_guess:
    print(character_guess + " found at index 1")
    total_matches = total_matches + 1

if word_guess[2] == character_guess:
    print(character_guess + " found at index 2")
    total_matches = total_matches + 1

if word_guess[3] == character_guess:
    print(character_guess + " found at index 3")
    total_matches = total_matches + 1

if word_guess[4] == character_guess:
    print(character_guess + " found at index 4")
    total_matches = total_matches + 1

if total_matches == 0:
    print("No instances of " + character_guess + " found in heels")

if total_matches == 1:
    print(str(total_matches) + " instance of " + character_guess + " found in " + word_guess)

if total_matches >= 2:
    print(str(total_matches) + " instances of " + character_guess + " found in " + word_guess)


