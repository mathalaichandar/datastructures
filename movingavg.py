from circularbuffer import CircularBuffer
import math

class MovingAvg(CircularBuffer):
    def __init__(self, size):
        """Stores buffer in given storage"""
        CircularBuffer.__init__(self,size)
        self.total = 0
        self.sumSquare = 0

    def getAverage(self):
        """Returns moving average (zero if no elements)"""
        if self.count == 0:
            return 0
        return self.total / self.count

    def getStd(self):
        """Returns moving Standard Deviation."""
        if self.count == 0:
            return 0
        std = (self.sumSquare - (self.total**2)/self.count)/self.count
        return std

    def remove(self):
        """ Removes Oldest Value from non-empty buffer """
        removed = CircularBuffer.remove(self)
        self.total -= removed
        return removed

    def add(self, value):
        """ Adds value to buffer, overwrite as needed. """
        if self.isFull():
            delta = -self.buffer[self.low]
            deltaSquare = -(self.buffer[self.low]**2)
        else:
            delta = 0
            deltaSquare = 0
        delta += value
        deltaSquare += value ** 2
        self.total += delta
        self.sumSquare += deltaSquare
        CircularBuffer.add(self, value)

    def __repr__(self):
        """String Representation of moving average."""
        if self.isEmpty():
            return "ma:[]"
        return "ma:[" + ','.join(map(str,self)) + "] Avg:" + str(self.getAverage()) + " Std:" + str(self.getStd())


