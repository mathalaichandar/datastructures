class LinkedNode(object):
    def __init__(self, value, tail=None):
        self.value = value
        self.next = tail

class QueueLinkedList(object):
    def __init__(self, *start):
        """Demonstrate queue using Linked list in Python."""
        self.head = None
        self.tail = None

        for _ in start:
            append(_)

    def append(self, value):
        """Adds value to last of the list"""
        newNode = LinkedNode(value, None)
        if self.head is None:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        
    def isEmpty(self):
        """Checks whether the list is empty"""
        return self.head == None

    def pop(self):
        """Removes First value from the list"""
        if self.head is None:
            raise Exception("Queue is empty")
        val = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return val
    
    def __iter__(self):
        "Iterator of values in queue"
        n = self.head
        while n != None:
            yield n.value
            n = n.next
    
    def __repr__(self):
        """String Representation of the Queue"""
        if self.head is None:
            return "queue:[]"
        return "queue:[{0:s}]".format(','.join(map(str,self)))


if __name__ == "__main__":
    q = QueueLinkedList()
    q.append(1)
    q.append(2)
    q.append(3)
    q.append(4)
    q.append(5)
    p = q.pop()
    print(p)
    print(q)