# Write a Python program to implement a circular queue using an array with enqueue and dequeue operations.

"""step 1. initialize: create array of fixed capacity set front = 0, size = 0
step 2. implement operations: enqueue->insert element at rear using circular index, dequeue->remove element from front, first->return front element
step 3. Handle circular movement using modulo %
step 4. Resize array if full."""

class CircularQueue:
    def __init__(self, capacity):  
        self.capacity=capacity
        self.queue=[None]*capacity
        self.front=0
        self.size=0

    def enqueue(self, item):
        if self.size==self.capacity:
            print("Queue is full")
            return
        
        rear=(self.front+self.size)%self.capacity
        self.queue[rear]=item
        self.size+=1
        print(f"{item} inserted")

    def dequeue(self):
        if self.size==0:
            print("Underflow")
            return
        
        removed=self.queue[self.front]
        self.queue[self.front]=None
        self.front=(self.front+1)%self.capacity
        self.size-=1
        print(f"{removed} removed")

    def display(self):
        if self.size==0:
            print("Underflow")
            return
        
        print("Queue:", end=" ")
        for i in range(self.size):
            print(self.queue[(self.front+i)%self.capacity], end=" ")
        print()

cap = int(input("Enter capacity:"))
cq=CircularQueue(cap)

while True:
    print("\n1. Enqueue 2.Dequeue 3.Display 4.Exit")
    choice=int(input("Enter value:"))

    match choice:
        case 1:
            val=int(input("Enter Value:"))
            cq.enqueue(val)
        case 2:
            cq.dequeue()
        case 3:
            cq.display()
        case 4:
            print("Exit")
            break
        case _:
            print("invalid choice")
