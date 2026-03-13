class Node:
    def __init__(self,data = None):
        self.value = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.length = 0

    def isEmpty(self):
        return (self.top == None)

    def push(self, data):
        temp = Node(data)
        temp.next = self.top
        self.top = temp
        self.length += 1

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.length -= 1
        return temp.value
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.top.value
    
    def size(self):
        return self.length