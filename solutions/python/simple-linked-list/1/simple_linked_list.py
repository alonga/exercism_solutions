class EmptyListException(Exception):
    """Exception raised when the linked list is empty."""
    def __init__(self, message):
        self.message = message


class Node:
    def __init__(self, value, next_node=None):
        self._value = value
        self._next = next_node

    def value(self):
        return self._value

    def next(self):
        return self._next


class LinkedList:
    def __init__(self, values=None):
        self._head = None
        self._size = 0
        if values:
            for v in values:
                self.push(v)

    def __iter__(self):
        current = self._head
        while current:
            yield current.value()
            current = current.next()

    def __len__(self):
        return self._size

    def head(self):
        if self._head is None:
            raise EmptyListException("The list is empty.")
        return self._head

    def push(self, value):
        self._head = Node(value, self._head)
        self._size += 1

    def pop(self):
        if self._head is None:
            raise EmptyListException("The list is empty.")
        value = self._head.value()
        self._head = self._head.next()
        self._size -= 1
        return value

    def reversed(self):
        new_list = LinkedList()
        for value in self:
            new_list.push(value)
        return new_list
