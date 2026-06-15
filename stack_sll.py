class Stack:
    def __init__(self):
        self.top = None  
    class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(f"{data} pushed to stack")

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None
        popped = self.top.data
        self.top = self.top.next
        print(f"{popped} popped from stack")
        return popped

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.top.data

    def display(self):
        current = self.top
        print("Stack elements:")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example usage
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

stack.display()

print("Top element is:", stack.peek())

stack.pop()
stack.display()
