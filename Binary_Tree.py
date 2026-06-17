class BT:
    def __init__(self):
        self.root = None
    class Node:
        def __init__(self, d, p, l, r):
            self.data = d 
            self.parent = p
            self.left = l 
            self.right = r
    def create_node(self,d,p,l=None,r=None):
        n = self.Node(d,p,l,r)
        return n
    def assign_root(self,n):
        if self.root!=None:
            print("Root is already present")
            return None
        self.root = n
    def assign_left(self,parent,left):
        if parent.left != None:
            print("Left exists")
        else:
            parent.left = left
            left.parent = parent
    def assign_right(self,parent,right):
        if parent.right != None:
            print("Right exists")
        else:
            parent.right = right
            right.parent = parent

# preorder
    def preorder(self,root): 
        if root == None:
            return None
        else:
            print(root.data)
            print("left")
            self.preorder(root.left)
            print("right")
            self.preorder(root.right)

# postorder inorder implementation
# left->root->right : postorder
    def postorder(self,root):
        if root==None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data)

    def inorder(self, root):
        if root == None:
            if root == None:
                return
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data)
        

bt = BT()
n = bt.create_node(12,None)
bt.assign_root(n)
n1 = bt.create_node(13,None)
bt.assign_left(n,n1)
bt.assign_left(n,n1)
bt.preorder(n)
bt.postorder()
