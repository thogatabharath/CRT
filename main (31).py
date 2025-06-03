class Node:
    def __init__(self):
        self.right=None
        self.left=None
        self.data=None
        
tree=Node()
tree.data=1  #root Node
tree.left=Node()  #creating new node for left
tree.left.data=2  #inserting data in left child
#creating new node for right child
tree.right=Node()
# inserting data in right child
tree.right.data=3
print(tree.data) #root Node
print(tree.left.data) #root child
# right child
print(tree.right.data) #right child
