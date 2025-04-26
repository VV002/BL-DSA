class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
    
    def add_child(self,data):
        if data == self.data:
            return
        
        elif data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        
        elif data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    def search(self,value):
        if self.data == value:
            return self.data

        elif value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
        
        elif value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False
        
    
    def inorder_traversal(self):
        elements = []

        if self.left: #Left Sub-tree
            elements += self.left.inorder_traversal()
        
        elements.append(self.data)

        if self.right:
            elements+= self.right.inorder_traversal()
        
        return elements
    
    def postorder_traversal(self):
        elements = []
        if self.left: #Left Sub-tree
            elements += self.left.postorder_traversal()
        
        if self.right:
            elements+= self.right.postorder_traversal()
        
        elements.append(self.data)

        return elements

    def preorder_traversal(self):
        elements = []

        elements.append(self.data)

        if self.left: #Left Sub-tree
            elements += self.left.preorder_traversal()
        
        if self.right:
            elements+= self.right.preorder_traversal()

        return elements
    
    def bst_minimum(self):
        temp = self.left
        while temp.left:
            temp = temp.left
        print(temp.data)
    
    def bst_maximu(self):
        temp = self.right
        while temp.right:
            temp = temp.right
        print(temp.data)
    
    def delete(self,value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        return self

def form_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root



def main():
    numbers = [17,4,2,25,56,18,5,3]
    tree = form_tree(numbers)
    print(tree.inorder_traversal())
    print(tree.postorder_traversal())
    print(tree.preorder_traversal())
    tree.bst_minimum()
    tree.bst_maximu()


if __name__ == "__main__":
    main()