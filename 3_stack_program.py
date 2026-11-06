"""
3_stack_program
Data structure: Stack (LIFO - last in, first out)
Push every letter of a word, then pop the letters one by one from the top.
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
    """Return the stack as text (bottom ... top), like [S, A, M]."""
    return "[" + ", ".join(items) + "]"


def main():
    word = get_word()
    stack = []                       # the END of the list is the TOP of the stack

    # PUSH: put every letter on top of the stack
    for letter in word:
        stack.append(letter)
    print("\nAdd:", show(stack))

    # POP: remove the top letter until the stack is empty
    while len(stack) > 0:
        removed = stack.pop()        # pop() removes the LAST item (the top)
        print(f"Remove {removed}:", show(stack))

    if len(stack) == 0:
        print("Result: EMPTY")


if __name__ == "__main__":
    main()
