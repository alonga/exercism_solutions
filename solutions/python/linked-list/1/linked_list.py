class Node:
    def __init__(self, value, succeeding=None, previous=None):
        self.value = value
        self.next = succeeding
        self.prev = previous


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    # Insert at end (right)
    def push(self, value):
        new_node = Node(value)

        if not self.head:  # list empty
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    # Remove from end (right)
    def pop(self):
        if self.length == 0:
            raise IndexError("List is empty")

        value = self.tail.value

        if self.length == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        self.length -= 1
        return value

    # Insert at start (left)
    def unshift(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.length += 1

    # Remove from start (left)
    def shift(self):
        if self.length == 0:
            raise IndexError("List is empty")

        value = self.head.value

        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

        self.length -= 1
        return value

    # Delete first occurrence of a value
    def delete(self, value):
        if self.length == 0:
            raise ValueError("Value not found")

        current = self.head

        while current:
            if current.value == value:

                # Node is the only element
                if self.length == 1:
                    self.head = self.tail = None

                # Node is the head
                elif current == self.head:
                    self.head = self.head.next
                    self.head.prev = None

                # Node is the tail
                elif current == self.tail:
                    self.tail = self.tail.prev
                    self.tail.next = None

                # Node is in the middle
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

                self.length -= 1
                return

            current = current.next

        # If we reached here → value not found
        raise ValueError("Value not found")
