"""EX03 Wordle."""

__author__ = "730573785"


def contains_char(word: str, single_char: str) -> bool:
    """Search for a letter in the given word"""
    assert len(single_char) == 1
    i: int = 0
    while (i < len(word)):
        if (word[i] == single_char):
            return True
        i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Returns an Emoji that tells the user where a character is used"""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    outcome: str = ""
    i: int = 0

    while (i < len(secret)):
        if (guess[i] == secret[i]):
            outcome += GREEN_BOX
        elif (contains_char(secret, guess[i])):
            outcome += YELLOW_BOX
        else:
            outcome += WHITE_BOX
        i += 1
    return outcome


def input_guess(length: int) -> str:
    """Makes sure the length of the guess is correct"""
    guess: str = input(f"Enter a {length} character word: ")
    while (len(guess) != length):
        guess = input(f"That wasn't {length} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop"""
    attempt: int = 1
    secret_word: str = "codes"
    main_guess: str = ""
    success: bool = False

    while (attempt <= 6 and not success):
        print(f"=== Turn {attempt}/6 ===")
        main_guess = input_guess(len(secret_word))
        print(emojified(main_guess, secret_word))
        if main_guess == secret_word:
            success = True
        else:
            attempt += 1

    if success is True:
        print(f"You won in {attempt} turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()