"""
4_queue_program
Data structure: Queue (FIFO - first in, first out)
Enqueue every letter of a word, then dequeue the letters one by one from the front.
"""
from collections import deque


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
    """Return the queue as text (front ... back), like [S, A, M]."""
    return "[" + ", ".join(items) + "]"


def main():
    word = get_word()
    queue = deque()                  # deque is a fast queue

    # ENQUEUE: add every letter at the back of the queue
    for letter in word:
        queue.append(letter)
    print("\nAdd:", show(queue))

    # DEQUEUE: remove the letter at the front until the queue is empty
    while len(queue) > 0:
        removed = queue.popleft()    # popleft() removes the FRONT item
        print(f"Remove {removed}:", show(queue))

    if len(queue) == 0:
        print("Result: EMPTY")


if __name__ == "__main__":
    main()
