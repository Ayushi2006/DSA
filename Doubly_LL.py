# define node: data, prev, next
# initialize: head=None
# insert at beginning 
# insert at end
# delete at beginning
# delete at end
# Traverse the list in forward direction

class DLL:
    def __init__(self):
        self.head=None
    class Node:
        def __init__(self,d):
            self.data=d
            self.next=None
            self.prev=None
    def insertAtBeginning(self,x):
        n = self.Node(x)
        if self.head != None:
            self.head.prev = n
            n.next = self.head
        self.head = n

    def traversal (self):
        if self.head is None:
            print("DLL Underflow")
        else:
            temp=self.head
            while temp.next is not None:
                print(temp.data, end="<->")
                temp=temp.next
            print(temp.data)
    def removeAtLast(self):
        if self.head == None:
            print("DLL Underflow") 
        elif self.head.next == None:
            val = self.head
            self.head = None
            print(val.data," deleted")
        else:
            p = self.head
            while p.next!= None:
                p = p.next
            val = p
            p.prev.next = None
            val.prev = None
            print(val.data, "deleted")
    def removeAtBeg(self):
        if self.head is None:
            print("DLL is underlfow")
        else:
            data = self.head
            self.head = self.head.next
            print(data.data)
    def insertAtLast(self,data):
        new_node=self.Node(data)
        if not self.head:
            self.head=new_node
        else:
            p=self.head
            while p.next!=None:
                p=p.next
            p.next=new_node
            new_node.prev = p
    

        
d = DLL()
d.removeAtBeg()
d.removeAtLast()
d.traversal()
d.insertAtBeginning(12)
d.insertAtBeginning(13)
d.insertAtBeginning(22)
d.traversal()
d.removeAtLast()
d.traversal()
d.removeAtBeg()
d.traversal()
d.insertAtLast(29)
d.traversal()
