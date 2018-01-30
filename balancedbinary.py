class BinaryNode(object):
    def __init__(self, value):
        self.value =value
        self.left = None
        self.right = None
        self.height = 0
        self.numLeft = 0
        self.numRight = 0

    def adjustCount(self, delta):
        """Adjust numLeft count after value has been added."""
        '''
        if self.left:
            print("Self value {} has left value {}".format(self.value, self.left.value))
            print(value<self.value)
        '''
        if self.left:
            self.numLeft += delta
            self.left.adjustCount(delta)   
        if self.right:
            self.numRight += delta
            self.right.adjustCount(delta)

    def computeHeight(self):
        """Compute height of node in BST"""
        height = -1
        if self.left:
            height = max(height, self.left.height)
        if self.right:
            height = max(height, self.right.height)
        self.height = height + 1
    
    def heightDifference(self):
        """Computes height difference of node's children in BST."""
        leftTarget = 0
        rightTarget = 0
        if self.left:
            leftTarget = 1 + self.left.height
        if self.right:
            rightTarget = 1 + self.right.height
        return leftTarget - rightTarget

    def rotateRight(self):
        """Perform Right Rotation around given node"""
        newRoot = self.left
        grandson = newRoot.right
        self.left = grandson
        newRoot.right = self

        self.computeHeight()
        return newRoot

    def rotateLeft(self):
        """Peerform Left Rotation around given Node"""
        newRoot = self.right
        grandson = newRoot.left
        self.right = grandson
        newRoot.left = self

        self.computeHeight()
        return newRoot

    def rotateLeftRight(self):
        child = self.left
        newRoot = child.right
        grand1 = newRoot.left
        grand2 = newRoot.right
        child.right = grand1
        self.left = grand2

        newRoot.left = child
        newRoot.right = self
        child.computeHeight()
        self.computeHeight()
        return newRoot

    def rotateRightLeft(self):
        child = self.right
        newRoot = child.left
        grand1 = newRoot.left
        grand2 = newRoot.right
        child.left = grand2
        self.right = grand1

        newRoot.right = child
        newRoot.left = self
        child.computeHeight()
        self.computeHeight()
        return newRoot

    def add(self, value):
        """Adds a new node to a tree with value. and rebalances the tree"""
        newRoot = self
        if value <= self.value:
            #Left Subtree
            self.left = self.addToSubTree(self.left, value)
            if self.heightDifference() == 2:
                if value <= self.left.value:
                    newRoot = self.rotateRight()
                else:
                    newRoot = self.rotateLeftRight()
        else:
            #right subtree
            self.right = self.addToSubTree(self.right, value)
            if self.heightDifference() == -2:
                if value > self.right.value:
                    newRoot = self.rotateLeft()
                else:
                    newRoot = self.rotateRightLeft()
        newRoot.computeHeight()
        return newRoot

    def addToSubTree(self, parent, value):
        """Adds value to the parent subtree and returns the node"""
        if parent is None:
            return BinaryNode(value)
        parent = parent.add(value)
        return parent
        
    def remove(self, value):
        """Remove value of self from Binary Tree, Works in conjunction with a method in
        BinaryTree class. only invoked if actually present."""
        newRoot = self
        if self.value == value:
            if self.left is None:
                return self.right
            child = self.left
            while child.right:
                child = child.right
            childKey = child.value
            self.left = self.removeFromParent(self.left,childKey)
            self.value = childKey

            if heightDifference() == -2:
                if self.right.heightDifference() <= 0:
                    newRoot = self.rotateLeft()
                else:
                    newRoot = self.rotateRightLeft()
        elif self.value > value:
            self.left = self.removeFromParent(self.left, value)
            if self.heightDifference() == -2:
                if self.left.heightDifference() <= 0:
                    newRoot = rotateLeft()
                else:
                    newRoot = rotateRightLeft()
        else:
            self.right = self. removeFromParent(self.right, value)
            if self.heightDifference() == 2:
                if self.left.heightDifference() >= 0:
                    newRoot = self.rotateRight()
                else:
                    newRoot = self.rotateLeftRight()

        newRoot.computeHeight()
        return newRoot

    def removeFromParent(self, parent, value):
        """Helper function for remove, Ensures proper behaviour and tree
        has children"""
        if parent:
            return parent.remove(value)
        return None

    def inorder(self):
        if self.left:
            for v in self.left.inorder():
                yield v

        yield self.value

        if self.right:
            for v in self.right.inorder():
                yield v
    
    def __repr__ (self):
        #print("representation: " + str(self.value))
        leftS = ''
        rightS = ''
        if self.left:
            leftS = str(self.left)
            #print("LeftS: " + leftS)
        if self.right:
            rightS = str(self.right)
            #print("RightS: " + rightS)
        return "(L:" + leftS + " " + str(self.value) + " R:" + rightS + ")"

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def __str__(self):
        if self.root:
            return str(self.root)
        
    def add(self, value):
        """Adds value to the binary tree in proper locations 
        Maintains set semantics. """
        if self.root is None:
            self.root = BinaryNode(value)
        else:
            if value in self:
                return false
            self.root = self.root.add(value)
            self.root.adjustCount(+1)
            
    def remove(self, value):
        """Removes a given value from binary tree. Check if contained
        first before actually trying to remove, so we can update propertly"""
        if value in self:
            self.root = self.root.remove(value)
            self.root.adjustCount(-1)

    def getMin(self):
        """Gets minimum value present in BST"""
        if self.root is None:
            raise ValueError("Binary Tree is Empty")
        child = self.root
        while child.left:
            child = child.left
        return child.value

    def getMax(self):
        if self.root is None:
            raise ValueError("Binary Tree is Empty")
        child = self.root
        while child.right:
            child = child.right
        return child.value

    def closest(self, target):
        if self.root is None:
            return None

        node = self.root
        best = node
        distance  = abs(self.root.value - target)
        while node:
            if abs(node.value - target) < distance:
                best = node
                distance = abs(node.value - target)
            
            if target < node.value:
                node = node.left
            elif target > node.value:
                node = node.right
            else:
                return target

        return best.value

    def smallest(self, k):
        """Return kth smallest element in tree. If k greater than number of elements
        return max. if smaller than 0 return min"""
        if self.root is None:
            raise ValueError("Binary search tree is empty")
        
        if k < 0:
            k = 0
        node = self.root
        while node:
            if k == node.numLeft:
                return node.value
            elif k < node.numLeft:
                node = node.left
            else:
                k = k - node.numLeft - 1
                if node.right is None:
                    return node.value
                node = node.right

    def biggest(self, k):
        """Return kth biggest element in tree. If k greater than number of elements
        return max. if smaller than 0 return min"""
        if self.root is None:
            raise ValueError("Binary Tree is Empty")
        if k < 0:
            k = 0
        node = self.root
        while node:
            if k == node.numRight:
                return node.value
            elif k < node.numRight:
                node = node.right
            else:
                k = k - node.numRight - 1
                if node.left is None:
                    return node.value
                node = node.left

    def __contains__(self, target):
        """Checks for a value in binary tree"""
        node = self.root
        while node is not None:
            if target < node.value:
                node = node.left
            elif target > node.value:
                node = node.right
            else:
                return True
        return False

    def __iter__(self):
        if self.root:
            for v in self.root.inorder():
                yield v
    
    def __repr__(self):
        if self.root is None:
            return "binary:()"
        return "binary:" + self.root

if __name__ == "__main__":
    bst = BinaryTree()
    '''
    for _ in range(1000):
        bst.add(_)
    '''
    bst.add(8)
    bst.add(5)
    bst.add(10)
    bst.add(11)
    bst.add(9)
    bst.add(12)
    bst.add(-10)
    bst.add(4)
    bst.add(1)
    bst.add(15)
    bst.add(18)
    bst.add(-15)
    bst.add(-11)

    #print(bst.getMin())
    #print(bst.getMax())
    #print(bst.closest(24))
    print(5 in bst)
    print(bst.smallest(0))
    print(bst.biggest(0))
    print("ROOT: " + str(bst.root.value))
    #print(bst.root.numRight)
    #print(bst.root.numLeft)
    print(bst)

    for _ in bst:
        print(_)
    