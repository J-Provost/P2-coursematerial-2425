class CircularBuffer:
    def __init__(self, n):
        self.max_size = n
        self.buffer = []
        self.start = 0

    def add(self, item):
        if len(self.buffer) < self.max_size:
            self.buffer.append(item)
        else:
            self.buffer[self.start] = item
            self.start = (self.start + 1) % self.max_size

    def __getitem__(self, index):
        if index < 0 or index >= len(self.buffer):
            raise IndexError("Index out of range")
        return self.buffer[(self.start + index) % len(self.buffer)]

    def __len__(self):
        return len(self.buffer)