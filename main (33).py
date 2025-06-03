class Node:
    def __init__(self,data=None):
        self.right=None
        self.left=None
        self.data=data
        
    def inorder_traversal(self,Node):
        if Node:
            self.inorder_traversal(Node.left)
            print(Node.data,end=" ")
            self.inorder_traversal(Node.right)
            
    def preorder_traversal(self,Node):
        if Node:
            print(Node.data,end=" ")
            self.preorder_traversal(Node.left)
            self.preorder_traversal(Node.right)
           
    def postorder_traversal(self,Node):
        if Node:
            self.postorder_traversal(Node.left)
            self.postorder_traversal(Node.right)
            print(Node.data,end=" ")
            
    def count(self,Node):
        if(Node!=None)
        count+=1
        self.count_of_nodes(left,right)
        
       
    
    
    
tree=Node()
tree.data=1  
tree.left=Node()  
tree.left.data=2 
tree.right=Node()
tree.right.data=3
print(tree.data) 
print(tree.left.data) 
print(tree.right.data) 
tree.inorder_traversal(Node=tree)
tree.preorder_traversal(Node=tree)
tree.postorder_traversal(Node=tree)


