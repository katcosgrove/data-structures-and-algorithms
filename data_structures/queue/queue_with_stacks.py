class Queue(object):
    def __init__(self):
        self.back = []
        self.front = []

    def enqueue(self, val):
        self.back.append(val)

    def dequeue(self):
        if not self.front:
            while self.back:
                self.front.append(self.back.pop())
        return self.front.pop()
