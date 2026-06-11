# LAB EXAM
# ADJACENCY MATRIX
# Graph representation : entry will be 0 or None if no edge exists.

V=int(input("Enter the number of vertices:"))
A=[]

for i in range(V):
    A.append([0]*V)
    
e=int(input("Enter the number of edges:"))
for m in range(e):
    print("Enter ", m+1, " edge")
    i = int(input("edges:"))
    j = int(input("vertices:"))
    A[i-1][j-1] = 1
    A[j-1][i-1] = 1

for i in range(V):
    print(A[i])
