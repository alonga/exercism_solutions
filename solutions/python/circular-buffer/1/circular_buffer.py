class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full."""
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty."""
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.read_pos = 0
        self.write_pos = 0
        self.size = 0  # tracks number of valid elements in the buffer

    def read(self):
        if self.size == 0:
            raise BufferEmptyException("Circular buffer is empty")

        data = self.buffer[self.read_pos]
        self.buffer[self.read_pos] = None
        self.read_pos = (self.read_pos + 1) % self.capacity
        self.size -= 1
        return data

    def write(self, data):
        if self.size == self.capacity:
            raise BufferFullException("Circular buffer is full")

        self.buffer[self.write_pos] = data
        self.write_pos = (self.write_pos + 1) % self.capacity
        self.size += 1

    def overwrite(self, data):
        if self.size == self.capacity:
            # Overwrite oldest element — move read pointer forward
            self.buffer[self.write_pos] = data
            self.write_pos = (self.write_pos + 1) % self.capacity
            self.read_pos = (self.read_pos + 1) % self.capacity
        else:
            self.write(data)

    def clear(self):
        self.buffer = [None] * self.capacity
        self.read_pos = 0
        self.write_pos = 0
        self.size = 0
