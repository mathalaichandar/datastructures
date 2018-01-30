class LinkedNode(object):
    def __init__(self, value, tail = None):
        self.value = value
        self.next = tail

class LinkedList(object):
    def __init__(self, *start):
        self.head = None

        for _ in start:
            self.prepend(_) #creates a linked list with values if passed while instantiation
    
    def prepend(self, value):
        """Add value to front of Linked List, O(1) - Const time operation """
        self.head = LinkedNode(value, self.head)
    
    def pop(self):
        """ Removes the first element of the List, O(1) - Const time operation """
        if self.head is None:
            raise Exception("Empty List")
        val = self.head.value
        self.head = self.head.next
        return val

    def remove(self, value):
        """ Remove a given value from the list, O(n) - Linear time operation """
        n = self.head
        last = None
        while n != None:
            if n.value == value:
                if last is None:
                    self.head = self.head.next
                else:
                    last.next = n.next
                return True
            last = n
            n = n.next

    def checkInfinite(self):
        """Check whether infinite loops via next"""
        p1 = p2 = self
        if p1 != None and p2 != None:
            if p2.next == None: return False
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2 : return True
        return False

    def __iter__(self):
        n = self.head
        while n != None:
            yield n.value
            n = n.next

    def __repr__(self):
        if self.head is None:
            return "link:[]"
        #return 'link:[' + ','.join(map(str,self)) + ']'
        return "link:[{0:s}]".format(','.join(map(str,self)))