stack=[]
top=-1

def push(value):
    global top
    stack.append(value)
    top+=1
       
def pop():
    global top
    if top == -1:
        print("stack is empty.Nothing to pop")
        return 
    else:
        stack.pop()
        top-=1
        
def peek():
    if top ==-1:
        return"stack is empty.no top element"
    else:
        return f"top element ={stack[top]}"
        
def display():
    if(top==-1):
        print("empty")
    else:
        for i in range(top,-1,-1):
            print(stack[i])
 
push(10)
push(30)
push(50)
push(70)
pop()
pop()
print(peek())
display()

