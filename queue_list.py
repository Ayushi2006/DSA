# implement queue using a list with enqueue and dequeue operations.
# create a class
class Queue:
    # initialize an empty list
    def __init__(self):
        self.data=[]
    # enqueue operation - front
    def enqueue(self, d):
        self.data.append(d)
    
    # dequeue operation - front
    def dequeue(self):
        if len(self.data)==0:
            print("underflow")
        else:
            return self.data.pop(0)
 
    # return 1st element
    def first_element(self):
        if len(self.data)==0:
            return "underflow"
        return self.data[0]

    # display queue
    def display():
        print("Queue:",l)

while True:
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. First element")
    print("4. Display Queue")
    print("5. Exit")

    ch=int(input("Enter your choice:"))
    if ch=='1':
        n=int(input("Enter element:"))
        Queue.enqueue()
    elif ch=='2':
        Queue.dequeue()
    elif ch=='3':
        Queue.first_element()
    elif ch=='4':
        Queue.display()
    elif ch=='5':
        break
    else:
        print("ERROR! invalid choice.")
