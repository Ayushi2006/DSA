class GraphList:
    class NodeEdge:
        def __init__(self,data):
            self.edge=data
            self.next=None

    class NodeVertex: 
        def __init__(self,data):
            self.data=data
            self.next_vertex=None
            self.edge_list=None
    # points to first vertex
    def __init__(self):
        self.head=None
    def insert_vertex(self,x=None):
        #insert at last of SLL if graph is not empty 
        # if graph empty head=new vertex
        n=self.NodeVertex(x)
        if self.head == None:
            self.head=n
            return

        temp = self.head
        while temp.next_vertex is not None:
            temp=temp.next_vertex
        
        temp.next_vertex=n    
    
    def find_vertex(self, x):
        temp=self.head
        while temp:
            if temp.data==x:
                return temp
            temp=temp.next_vertex
        return None

    def insert_edge(self,u, v):
        vertex_u=self.find_vertex(u)
        if vertex_u is None:
            print("Vertex not found")
            return
        new_edge=self.NodeEdge(v)

        if vertex_u.edge_list is None:
            vertex_u.edge_list=new_edge
            return
        temp=vertex_u.edge_list
        while temp.next:
            temp=temp.next
        temp.next=new_edge

    def traversal(self):
        temp_vertex=self.head
        while temp_vertex:
            print(temp_vertex.data, "->", end=" ")
            temp_edge=temp_vertex.edge_list

            while temp_edge:
                print(temp_edge.edge, end="")
                temp_edge=temp_edge.next

            print()
            temp_vertex=temp_vertex.next_vertex

    

g = GraphList()

# Insert vertices
g.insert_vertex(1)
g.insert_vertex(2)
g.insert_vertex(3)
g.insert_vertex(4)

# Insert edges
g.insert_edge(1, 2)
g.insert_edge(1, 3)
g.insert_edge(2, 4)
g.insert_edge(3, 2)

# Print graph
g.traversal()

