from collections import deque


class CQueue:

    def __init__(self):
        self.A = []
        self.B = []

    def appendTail(self, value):

        self.A.append(value)

    def deleteHead(self):

        if len(self.B) != 0:
            return self.B.pop()

        else:
            if not self.A: return -1

            while len(self.A) != 0:
                self.B.append(self.A.pop())

        return self.B.pop()
