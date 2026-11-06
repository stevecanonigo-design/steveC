"""
1_array_program
Data structure: Array (Python list)
Add every letter of a word, then remove the letters one by one from the front.
"""


def get_word():
    """Keep asking until the user types letters only (no spaces, not empty)."""
    while True:
        word = input("Enter a word (example: CANONIGO): ").strip().upper()
        if word == "":
            print("Error: the word cannot be empty.")
        elif not word.isalpha():
            print("Error: use letters only (no spaces, numbers or symbols).")
        else:
            return word


def show(items):
    """Return the list as text, like [S, A, M]."""
    return "[" + ", ".join(items) + "]"


def main():
    word = get_word()
    array = []                       # the array (Python list)

    # ADD: put every letter into the array
    for letter in word:
        array.append(letter)
    print("\nAdd:", show(array))

    # REMOVE: take out the first letter until the array is empty
    while len(array) > 0:
        removed = array.pop(0)       # pop(0) removes the first item
        print(f"Remove {removed}:", show(array))

    if len(array) == 0:
        print("Result: EMPTY")


if __name__ == "__main__":
    main()
