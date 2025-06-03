class Node:
    def __init__(self,data):
        self.data=data
        self.next=None 
        
class LinkedList:
    def __init__(self):
        self.head=None   #starting point of LL
        
    def insert_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new_node 
            
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end=
            "->")
            temp=temp.next
        print("None")
     
    def add_ll(self):
        temp=self.head
        sum=0
        while temp:
            sum=sum+temp.data
            temp=temp.next
        return sum
        
    def Count(self):
        pass
    
    def insert_begnning(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
       
    def delete_begining(self):
        self.head=self.head.next
    def delete_end(self):
        temp=self.head
        while temp.next.next:
            temp=temp.next
        temp.next=None
        
    
ll=LinkedList()
ll.insert_end(10)
ll.insert_begnning(8888)
ll.display()
ll.insert_end(20)
ll.insert_end(30)
ll.insert_end(40)
ll.delete_begining()
ll.display()
print(" sum of elements in ll is ")
ans=ll.add_ll()
print(ans)