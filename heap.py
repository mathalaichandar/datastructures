"""Impleementing Heap Class"""
class Heap(object):
    def __init__(self, value = None):
        """Constructs List from values"""
        if value == None:
            self.ar = []
        else:
            self.ar = list(value)
        self.n = (len(self.ar))

        start = self.n//2 - 1
        for i in range(start, -1, -1):
            self.heapify(i) 

    def isEmpty(self):
        "Detremine if a heap is empty"
        return self.n == 0
    
    def __len__(self):
        """Returns the size of the heap"""
        return self.n
    
    def pop(self):
        """Return the smallest value and repair the heap"""
        if self.n == 0:
            raise ValueError("Heap is empty")
        value = self.ar[0]
        self.n -= 1
        self.ar[0] = self.ar[self.n]
        self.heapify(0)
        return value

    def add(self, value):
        ''' Add Value to the Heap and Repair Heap'''
        if self.n == len(self.ar):
            self.ar.append(value)
        else:
            self.ar[self.n] = value
        i = self.n
        self.n += 1

        #Correct the structure to root
    
        while i > 0 :
            parent = (i-1) // 2
            if self.ar[i] < self.ar[parent]:
                self.ar[i], self.ar[parent] = self.ar[parent], self.ar[i]
                i = parent
            else:
                break

    def heapify(self, i):
        """Heapify Subarray [i, end]"""
        left = 2*i + 1
        right = 2*i + 2
        #find the smallest element of A[i], A[left], A[right]
        if left < self.n and self.ar[left] < self.ar[i]:
            smallest = left
        else:
            smallest = i
        
        if right < self.n and self.ar[right] < self.ar[i]:
            smallest = right
        else:
            smallest = i
        
        #If smallest is not already the parent then swap
        if smallest != i:
            self.ar[i], self.ar[smallest] = self.ar[smallest], self.ar[i]
            self.heapify(smallest)

    def __repr__(self):
        """Return Representation of the heap"""
        return "heap:[" + ','.join(map(str, self.ar[:self.n])) + "]"