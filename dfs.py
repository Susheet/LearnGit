from collections import defaultdict
import time
import sys

starttime = time.time()

def dfs_search(tree,start,visited,path,node):
    path.append(start)
    visited[start] = True
    for neighbour_vertice in tree[start]:
        if neighbour_vertice == node:
            print("Node found")
            break
        if visited[neighbour_vertice] == False:
            dfs_search(tree,neighbour_vertice,visited,path,node)
    return path

tree = defaultdict(list)
vertices,edges = map(int,input().split())
for i in range(edges):
    u,v = map(str,input().split())
    tree[u].append(v)
    tree[v].append(u)
        
path = []
visited = defaultdict(bool)
start = 'A'
node = str(input("Enter node to be found:"))
traversed = dfs_search(tree,start,visited,path,node)
# print(traversed)

space = sys.getsizeof(path)

end = time.time()
print(end - starttime,"time complexity")
print(space,"space complexity")