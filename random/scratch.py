class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
# Insert Node
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                    if self.right is None:
                        self.right = Node(data)
                    else:
                        self.right.insert(data)
        else:
            self.data = data

# Print Tree            
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data), 
        if self.right:
            self.right.PrintTree()

# Inorder Traversal    
# Left -> Root -> Right    
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res
        
root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.inorderTraversal(root)) 
       
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
# Insert Node
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                    if self.right is None:
                        self.right = Node(data)
                    else:
                        self.right.insert(data)
        else:
            self.data = data

# Print Tree            
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data), 
        if self.right:
            self.right.PrintTree()

# Preorder Traversal    
# Root -> Left -> Right    
    def preorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preorderTraversal(root.left)
            res = res + self.preorderTraversal(root.right)
        return res
        
root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.preorderTraversal(root)) 

