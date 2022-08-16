from collections import deque


class RingBuf(deque):
    def __init__(self, size=1):
        super(RingBuf, self).__init__(maxlen=size)

