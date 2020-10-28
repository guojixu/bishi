class MinStack:

    def __init__(self):

        self.stack = []
        self.min_stac = []

    def push(self, val):

        # if len(self.stack) == 0:
        #     self.stack.append(val)
        #     self.min_stac.append(val)
        #
        # elif val <= self.stack[-1]:
        #     self.stack.append(val)
        #     self.min_stac.append(val)
        # elif val > self.stack[-1]:
        #     self.stack.append(val)
        #     self.min_stac.append(self.min_stac[-1])
        self.stack.append(val)

        if (len(self.min_stac) == 0 or val <= self.min_stac[-1]):
            self.min_stac.append(val)

    def pop(self):

        if len(self.stack) == 0:
            return -1
        if self.stack[-1] == self.min_stac[-1]:
            self.stack.pop()
            self.min_stac.pop()
        else:
            self.stack.pop()

    def top(self):

        return self.stack[-1]

    def getMin(self):

        return self.min_stac[-1]
