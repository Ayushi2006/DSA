class QSLL:

    class Node:
        def __init__(self, d):
            self.data = d
            self.next = None

    def __init__(self):
        self.f = None
        self.r = None

    def enqueue(self, d):
        n = self.Node(d)
        if self.r is None:
            self.f = self.tail = n
        else:
            self.tail.next = n
            self.tail = n

    def dequeue(self):
        if self.head is None:
            print("Queue is underflow")
            return
        temp = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return temp.data

    def front(self):
        if self.head is None:
            print("Queue is underflow")
        else:
            print(self.head.data)

    def traversal(self):
        if self.head is None:
            print("Queue is Underflow")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, end=" -> ")
                temp = temp.next
            print("None")

q = QSLL()
q.traversal()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.traversal()
