class Queue:
    def __init__(self):
        self.entries = []
        self.length = 0
        self.front = 0

    def __str__(self):
        printed = f"<{str(self.entries)[1:-1]}>"
        return printed

    def put(self, item):
        self.entries.append(item)
        self.length = self.length + 1

    def get(self):
        self.length = self.length - 1
        dequeued = self.entries[self.front]
        self.entries = self.entries[1:]
        return dequeued

    def rotate(self, rotation):
        for i in range(rotation):
            self.put(self.get())

    def get_front(self):
        return self.entries[0]

    def size(self):
        return self.length


def test_block():
    queue = Queue()
    queue.put(1)
    queue.put(2)
    print(queue)
    print(queue.get())
    queue.put(3)
    print(queue)
    queue.rotate(1)
    print(queue)
    print(queue.get_front())
    print(queue.size())


if __name__ == "__main__":
    test_block()
