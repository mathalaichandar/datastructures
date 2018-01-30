class CircularBuffer(object):
    def __init__(self, size):
        '''
        Constructs a fixed size buffer
        '''
        self.size = size
        self.buffer = [None]*size
        self.low = 0
        self.high = 0
        self.count = 0
    
    def add(self, value):
        if self.isFull():
            self.low = (self.low + 1) % self.size
            #print("Low {}".format(self.low))
        else:
            self.count += 1
            #print(self.count)
        
        self.buffer[self.high] = value
        self.high = (self.high + 1) % self.size
        #print("High {}".format(self.high))
    
    def remove(self):
        if self.isEmpty():
            raise Exception("Circular Buffer is Empty")
        value = self.buffer[self.low]
        self.low = (self.low + 1) % self.size
        self.count -= 1
        return value

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.size

    def __iter__(self):
        idx = self.low
        num = self.count
        while num > 0:
            yield self.buffer[idx]
            idx = (idx + 1) % self.size
            num -= 1
        
    def __repr__(self):
        if self.isEmpty():
            return 'cb:[]'
        return 'cb:[' + ','.join(map(str,self)) + ']'
