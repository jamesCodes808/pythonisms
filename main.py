# Iterating through a class using __iter__ and generators

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

# When we create/override the __iter__ for the LinkedList class, we can now iterate through the linked list,
    # with for loops
    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def add_node(self, value):
        new = Node(value)
        if self.head is None:
            self.head = new
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new


if __name__ == '__main__':
    test_ll = LinkedList()
    test_ll.add_node(1)
    test_ll.add_node(2)
    test_ll.add_node(3)

    for value in test_ll:
        print(value)