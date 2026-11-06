"""
2_singly_linked_list_program
Data structure: Singly linked list
Add every letter of a word as a node, then remove the nodes one by one from the front.
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


class Node:
    """One node: holds a letter and a link to the next node."""

    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None             # None means the list is empty

    def add_last(self, data):
        """Add a new node at the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:   # walk to the last node
                current = current.next
            current.next = new_node

    def remove_first(self):
        """Remove the first node and return its letter."""
        removed = self.head.data
        self.head = self.head.next            # head now points to the 2nd node
        return removed

    def is_empty(self):
        return self.head is None

    def show(self):
        """Return the list as text, like [S, A, M]."""
        letters = []
        current = self.head
        while current is not None:
            letters.append(current.data)
            current = current.next
        return "[" + ", ".join(letters) + "]"


def main():
    word = get_word()
    linked_list = SinglyLinkedList()

    # ADD: one node for every letter
    for letter in word:
        linked_list.add_last(letter)
    print("\nAdd:", linked_list.show())

    # REMOVE: delete the first node until the list is empty
    while not linked_list.is_empty():
        removed = linked_list.remove_first()
        print(f"Remove {removed}:", linked_list.show())

    if linked_list.is_empty():
        print("Result: EMPTY")


if __name__ == "__main__":
    main()
