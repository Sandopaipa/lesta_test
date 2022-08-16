class RingBuf:
    def __init__(self, length=1):
        self.data = []
        self.full = False
        self.max = length
        self.cur = 0

    def append(self, item):
        if self.full is True:
            for i in range(0, self.cur - 1):
                self.data[i] = self.data[i + 1]
            self.data[self.cur - 1] = item
        else:
            self.data.append(item)
            self.cur += 1
            if self.cur == self.max:
                self.full = True

    def get(self):
        return self.data

