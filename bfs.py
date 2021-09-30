from collections import deque
from collections import defaultdict
import time
import sys

starttime = time.time()

def bfs(tree,start,visited,path):
    queue = deque()
    queue.append(start)
    path.append(start)
    visited[start] = True
    while(len(queue)):
        nodevalue = queue.popleft()
        for neighbour_vertice in tree[nodevalue]:
            # if neighbour_vertice == node:
            #     print("Node found")
            #     break
            if visited[neighbour_vertice] == False:
                path.append(neighbour_vertice)
                queue.append(neighbour_vertice)
                visited[neighbour_vertice] = True
    space = sys.getsizeof(queue)   
    print(space,'space complexity')         
    return path


tree = defaultdict(list)
vertices,edges = map(int,input().split())
for i in range(edges):
    u,v = map(str,input().split())
    tree[u].append(v)
    tree[v].append(u)
    
start = 'A'
path = []
visited = defaultdict(bool)
# node = str(input("Enter node to be found:"))
traversed = bfs(tree,start,visited,path)
print(traversed)


end = time.time()
print(end - starttime)
# print(space,"space complexity")