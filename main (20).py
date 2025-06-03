def push(value):
    top=-1
    if(top==4):
        return"stack is full"
    else:
        top=top+-1
        return stack.append(value)
def pop():
    top=5
    if(top!=-1):
        return stack.pop()
    else:
        top-=10
        return "stack is empty"
        
stack=[10]      #size as 5
push(20)
push(30)
push(40)
push(50)
pop()
pop()
print(stack)

