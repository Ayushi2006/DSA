class Graph:
    def __init__(self, v):
        self.v=v
        self.g={}

        for i in range(self, v):
            self.g[i]=[]
    def add_edge(self,u,v,w,directed=False):
        if directed:
            self.g[u]=(v,w)
        else:
            self.g[v]=(u,w)
    def djikstras(self,s):
        distance=[]
        visited={}
        for i in range(self.v):  #initialising the default dist=infinity and not visited
            distance[i]=999
            visited[i]=False
        distance[s]=0
        for i in range(self.v):
            minimum=999
            u=-1
            for i in distance:
                if i < minimum and visited[i]==False:
                    u=i
                    minimum=distance[i]
                    visited[i]=True
                if u==-1:
                    break
                for adj, weight in self.g[u]:
                    if visited[adj]==False and distance[s]+weight<distance[adj]:
                        distance[adj]=distance[s]+weight
        for i in range(len(distance)):
            print(i, distance[i])


v=int(input("Enter the number of veritices:"))
d=int(input("Enter 1 for directed and 0 for undirected:"))
e=int(input("enter number of edges:"))

g=Graph(v)
for i in range(e):
    print(str(i)+"th edge:")
    uu=int(input("U:"))
    vv=int(input("V:"))
    ww=int(input("weight:"))
    if d == 1:
        g.add_edge(uu,vv,w,True)
    else:
        g.add_edge(uu,vv,w)