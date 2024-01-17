"""Creating a One Shot Wordle!"""

__author__: str = "730573785"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

secret_word: str = "python"
guess: str = input("What is your " + str(len(secret_word)) + "-letter guess? ")

while (len(guess) != len(secret_word)):
    guess: str = input("That was not " + str(len(secret_word)) + " letters! Try again:")

result: str = ""

i: int = 0

while (i < len(secret_word)):
    if (guess[i] == secret_word[i]):
        result = result + GREEN_BOX
    else:
        char_exist: bool = False
        secret_transverser: int = 0
        while (char_exist is False and secret_transverser < len(secret_word)):
            if (guess[i] == secret_word[secret_transverser]):
                char_exist = True
            else:
                secret_transverser += 1
        if (char_exist is True):
            result = result + YELLOW_BOX
        else:
            result = result + WHITE_BOX
    i += 1

print(result)
if (guess == secret_word):
    print("Woo! You got it!")
else:
    print("Not quite. Play again Soon!")
