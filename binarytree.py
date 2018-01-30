class BinaryNode(object):
    def __init__(self, value):
        self.value =value
        self.left = None
        self.right = None

    def add(self, value):
        """Adds a new node to a tree with value."""
        if value <= self.value:
            #Left Subtree
            self.left = self.addToSubTree(self.left, value)
        elif value > self.value:
            #right subtree
            self.right = self.addToSubTree(self.right, value)

    def addToSubTree(self, parent, value):
        """Adds value to the parent subtree and returns the node"""
        print(parent)
        if parent is None:
            return BinaryNode(value)
        parent.add(value)
        return parent
        
    def remove(self, value):
        """Remove value of self from Binary Tree, Works in conjunction with a method in
        BinaryTree class. only invoked if actually present."""
        if value < self.value:
            #left subtree
            self.left = self.removeFromParent(self.left, value)
        elif value > self.value:
            #Right subtree
            self.right = self.removeFromParent(self.right, value)
        else:
            #if the value to remove is a node
            if self.left is None:
                return self.right
            #Else Find largest value in left subrtree
            child = self.left
            while child.right:
                child = child.right
            childKey = child.value
            self.left = self.removeFromParent(self.left, childKey)
            self.value = childKey
        return self

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
    
class BinaryTree(object):
    def __init__(self):
        self.root = None

    def add(self, value):
        """Adds value to the binary tree in proper locations 
        Maintains set semantics. """
        if self.root is None:
            print("Root Value " + str(value))
            self.root = BinaryNode(value)
        else:
            if value in self:
                return False
            ret = self.root.add(value)
            

    def remove(self, value):
        """Removes a given value from binary tree. Check if contained
        first before actually trying to remove, so we can update propertly"""
        if value in self:
            self.root = self.root.remove(value)

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
        return "binary:" + str(self.root)

if __name__ == "__main__":
    bst = BinaryTree()
    bst.add(8)
    bst.add(5)
    bst.add(10)
    bst.add(11)
    bst.add(9)
    bst.add(12)
    bst.add(-10)
    bst.add(4)
    bst.add(1)
    #print(bst.getMin())
    #print(bst.getMax())
    #print(bst.closest(24))
    for _ in bst:
        print(_)
    print(bst)