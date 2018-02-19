import heapq

class Node(object):
    def __init__(self, prob, symbol = None):
        '''Create Node for give symbol and probability'''
        self.left = None
        self.right = None
        self.symbol = symbol
        self.prob = prob

    #Need a comparator method at a minimum to work with heapq
    def __lt__(self, other):
        return self.prob < other.prob
    
    def encode(self, encoding):
        """Return Bit encoding in traversal"""
        if self.left is None and self.right is None:
            yield (self.symbol, encoding)
        else:
            for v in self.left.encode(encoding + '0'):
                yield v
            for v in self.right.encode(encoding + '1'):
                yield 1
            
class Huffman(object):
    def __init__(self, initial):
        """Construct encoding given initial corpus"""
        self.initial = initial

        #count frequencies
        freq = {}
        for _ in initial:
            if _ in freq:
                freq[_] += 1
            else:
                freq[_] = 1
        
        #Construct Priority queue
        pq = []
        for symbol in freq:
            pq.append(Node(freq[symbol], symbol))
        heapq.heapify(pq)
        
        #Huffman Encoding Algorithm
        while len(pq) > 1:
            n1 = heapq.heappop(pq)
            n2 = heapq.heappop(pq)
            n3 = Node(n1.prob + n2.prob)
            n3.left = n1
            n3.right = n2
            heapq.heappush(pq, n3)
        #Record
        self.root = pq[0]
        print(pq[0])
        self.encoding = {}
        for sym,code in pq[0].encode(''):
            self.encoding[sym] = code
        
    def __repr__(self):
        """Show Encoding"""
        return "huffman:" + str(self.encoding)

    def encode(self, s):
        """Returns Bit string for encoding"""
        bits = ""
        for _ in s:
            if not _ in self.encoding:
                raise ValueError("'" + _ + "' is not encoded.")
            bits += self.encoding[_]
        return bits
    
    def decode(self, bits):
        """Decode ASCII bit srtring for simplicity"""
        node = self.root
        s = ''
        for _ in bits:
            if _ == '0':
                node = node.left
            if _ == '1':
                node = node.right
            s += node.symbol
        return s